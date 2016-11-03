Title: Async I/O and Python
Date: 2013-06-04 16:28
Author: markmc
Tags: OpenStack, Python
Slug: async-io-and-python
Status: published

When you're working on OpenStack, you'll probably hear a lot of
references to 'async I/O' and how eventlet is the library we use for
this in OpenStack.

But, well ... what exactly is this mysterious 'asynchronous I/O' thing?

The first thing to think about is what happens when a process calls a
system call like write(). If there's room in the write buffer, then the
data gets copied into kernel space and the system call returns
immediately.

But if there isn't room in the write buffer, what happens then? The
default behaviour is that the kernel will put the process to sleep until
there is room available. In the case of sockets and pipes, space in the
buffer usually becomes available when the other side reads the data
you've sent.

The trouble with this is that we usually would prefer the process to be
doing something useful while waiting for space to become available,
rather than just sleeping. Maybe this is an API server and there are new
connections waiting to be accepted. How can we process those new
connections rather than sleeping?

One answer is to use multiple threads or processes - maybe it doesn't
matter if a single thread or process is blocked on some I/O if you have
lots of other threads or processes doing work in parallel.

But, actually, the most common answer is to use non-blocking I/O
operations. The idea is that rather than having the kernel put the
process to sleep when no space is available in the write buffer, the
kernel should just return a "try again later" error. We then using the
select() system call to find out when space has become available and the
file is writable again.

Below are a number of examples of how to implement a non-blocking write.
For each example, you can run a simple socket server on a remote machine
to test against:

    $> ssh -L 1234:localhost:1234 some.remote.host 'ncat -l 1234 | dd of=/dev/null'

The way this works is that the client connects to port 1234 on the local
machine, the connection is forwarded over SSH to port 1234 on
some.remote.host where ncat reads the input, writes the output over a
pipe to dd which, in turn, writes the output to /dev/null. I use dd to
give us some information about how much data was received when the
connection closes. Using a distant some.remote.host will help illustrate
the blocking behaviour because data clearly can't be transferred as
quickly as the client can copy it into the kernel.

### Blocking I/O

To start with, let's look at the example of using straightforward
blocking I/O:

    import socket

    sock = socket.socket()
    sock.connect(('localhost', 1234))
    sock.send('foo\n' * 10 * 1024 * 1024)

This is really nice and straightforward, but the point is that this
process will spend a tonne of time sleeping while the send() method
completes transferring all of the data.

### Non-Blocking I/O

In order to avoid this blocking behaviour, we can set the socket to
non-blocking and use select() to find out when the socket is writable:

    import errno
    import select
    import socket

    sock = socket.socket()
    sock.connect(('localhost', 1234))
    sock.setblocking(0)

    buf = buffer('foo\n' * 10 * 1024 * 1024)
    print "starting"
    while len(buf):
        try:
            buf = buf[sock.send(buf):]
        except socket.error, e:
            if e.errno != errno.EAGAIN:
                raise e
            print "blocking with", len(buf), "remaining"
            select.select([], [sock], [])
            print "unblocked"
    print "finished"

As you can see, when send() returns an EAGAIN error, we call select()
and will sleep until the socket is writable. This is a basic example of
an event loop. It's obviously a loop, but the "event" part refers to our
waiting on the "socket is writable" event.

This example doesn't look terribly useful because we're still spending
the same amount of time sleeping but we could in fact be doing useful
rather than sleeping in select(). For example, if we had a listening
socket, we could also pass it to select() and select() would tell us
when a new connection is available. That way we could easily alternate
between handling new connections and writing data to our socket.

To prove this "do something useful while we're waiting" idea, how about
we add a little busy loop to the I/O loop:

            if e.errno != errno.EAGAIN:
                raise e

            i = 0
            while i < 5000000:
                i += 1

            print "blocking with", len(buf), "remaining"
            select.select([], [sock], [], 0)
            print "unblocked"

The difference is we've passed a timeout of zero to select() - this
means select() never actually block - and any time send() would have
blocked, we do a bunch of computation in user-space. If we run this
using the 'time' command you'll see something like:

    $> time python ./test-nonblocking-write.py 
    starting
    blocking with 8028160 remaining
    unblocked
    blocking with 5259264 remaining
    unblocked
    blocking with 4456448 remaining
    unblocked
    blocking with 3915776 remaining
    unblocked
    blocking with 3768320 remaining
    unblocked
    blocking with 3768320 remaining
    unblocked
    blocking with 3670016 remaining
    unblocked
    blocking with 3670016 remaining
    ...
    real    0m10.901s
    user    0m10.465s
    sys     0m0.016s

The fact that there's very little difference between the 'real' and
'user' times means we spent very little time sleeping. We can also see
that sometimes we get to run the busy loop multiple times while waiting
for the socket to become writable.

### Eventlet

Ok, so how about eventlet? Presumably eventlet makes it a lot easier to
implement non-blocking I/O than the above example? Here's what it looks
like with eventlet:

    from eventlet.green import socket

    sock = socket.socket()
    sock.connect(('localhost', 1234))
    sock.send('foo\n' * 10 * 1024 * 1024)

Yes, that does look very like the first example. What has happened here
is that by creating the socket using eventlet.green.socket.socket() we
have put the socket into non-blocking mode and when the write to the
socket blocks, eventlet will schedule any other work that might be
pending. Hitting Ctrl-C while this  
is running is actually pretty instructive:

    $> python test-eventlet-write.py 
    ^CTraceback (most recent call last):
      File "test-eventlet-write.py", line 6, in 
        sock.send('foo\n' * 10 * 1024 * 1024)
      File ".../eventlet/greenio.py", line 289, in send
        timeout_exc=socket.timeout("timed out"))
      File ".../eventlet/hubs/__init__.py", line 121, in trampoline
        return hub.switch()
      File ".../eventlet/hubs/hub.py", line 187, in switch
        return self.greenlet.switch()
      File ".../eventlet/hubs/hub.py", line 236, in run
        self.wait(sleep_time)
      File ".../eventlet/hubs/poll.py", line 84, in wait
        presult = self.do_poll(seconds)
      File ".../eventlet/hubs/epolls.py", line 61, in do_poll
        return self.poll.poll(seconds)
    KeyboardInterrupt

Yes, indeed, there's a whole lot going on behind that innocuous looking
send() call. You see mention of a 'hub' which is eventlet's name for an
event loop. You also see this trampoline() call which means "put the
current code to sleep until the socket is writable". And, there at the
very end, we're still sleeping in a call to poll() which is basically
the same thing as select().

To show the example of doing some "useful" work rather than sleeping all
the time we run a busy loop greenthread:

    import eventlet
    from eventlet.green import socket

    def busy_loop():
        while True:
            i = 0
            while i < 5000000:
                i += 1
            print "yielding"
            eventlet.sleep()
    eventlet.spawn(busy_loop)

    sock = socket.socket()
    sock.connect(('localhost', 1234))
    sock.send('foo\n' * 10 * 1024 * 1024)

Now every time the socket isn't writable, we switch to the busy\_loop()
greenthread and do some work. Greenthreads must cooperatively yield to
one another so we call eventlet.sleep() in busy\_loop() to once again
poll the socket to see if its writable. Again, if we use the 'time'
command to run this:

    $> time python ./test-eventlet-write.py 
    yielding
    yielding
    yielding
    ...
    real    0m5.386s
    user    0m5.081s
    sys     0m0.088s

you can see we're spending very little time sleeping.

(As an aside, I was going to take a look at gevent, but it doesn't seem
fundamentally different from eventlet. Am I wrong?)

### Twisted

Long, long ago, in times of old, [Nova switched from twisted to
eventlet](https://code.launchpad.net/~termie/nova/eventlet_merge/+merge/43383)
so it makes sense to take a quick look at twisted:

    from twisted.internet import protocol
    from twisted.internet import reactor

    class Test(protocol.Protocol):
        def connectionMade(self):
            self.transport.write('foo\n' * 2 * 1024 * 1024)

    class TestClientFactory(protocol.ClientFactory):
        def buildProtocol(self, addr):
            return Test()

    reactor.connectTCP('localhost', 1234, TestClientFactory())
    reactor.run()

What complicates the example most is twisted protocol abstraction which
we need to use simply to write to the socket. The 'reactor' abstraction
is simply twisted's name for an event loop. So, we create a on-blocking
socket, block in the event loop (using e.g. select()) until the
connection completes and then  
write to the socket. The transport.write() call will actually queue a
writer in the reactor, return immediately and whenever the socket is
writable, the writer will continue its work.

To show how you can run something in parallel, here's how to run some
code in a deferred callback:

    def busy_loop():
        i = 0
        while i < 5000000:
            i += 1
        reactor.callLater(0, busy_loop)

    reactor.connectTCP(...)
    reactor.callLater(0, busy_loop)
    reactor.run()

I'm using a timeout of zero here and it shows up a weakness in both
twisted and eventlet - we want this busy\_loop() code to only run when
the socket isn't writeable. In other words, we want the task to have a
lower priority than the writer task. In both twisted and eventlet, the
timed tasks are run before the  
I/O tasks and there is no way to add a task which is only run if there
are no runnable I/O tasks.

### GLib

My introduction to async I/O was back when I was working on GNOME
(beginning with GNOME's CORBA ORB, called ORBit) so I can't help
comparing the above abstractions to GLib's main loop. Here's some
equivalent code:

    /* build with gcc -g -O0 -Wall $(pkg-config --libs --cflags glib-2.0) test-glib-write.c -o test-glib-write */

    #include <errno.h>
    #include <fcntl.h>
    #include <stdio.h>
    #include <string.h>
    #include <unistd.h>
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <netinet/in.h>

    #include <glib.h>

    GMainLoop    *main_loop = NULL;
    static gchar *strv[10 * 1024 * 1024];
    static gchar *data = NULL;
    int           remaining = -1;

    static gboolean
    socket_writable(GIOChannel   *source,
                    GIOCondition  condition,
                    gpointer      user_data)
    {
      int fd, sent;

      fd = g_io_channel_unix_get_fd(source);
      do
        {
          sent = write(fd, data, remaining);
          if (sent == -1)
            {
              if (errno != EAGAIN)
                {
                  fprintf(stderr, "Write error: %s\n", strerror(errno));
                  goto finished;
                }
              return TRUE;
            }

          data = &data[sent];
          remaining -= sent;
        }
      while (sent > 0 && remaining > 0);

      if (remaining <= 0)
        goto finished;

      return TRUE;

     finished:
      g_main_loop_quit(main_loop);
      return FALSE;
    }

    static gboolean
    busy_loop(gpointer data)
    {
      int i = 0;
      while (i < 5000000)
        i += 1;
      return TRUE;
    }

    int
    main(int argc, char **argv)
    {
      GIOChannel         *io_channel;
      guint               io_watch;
      int                 fd;
      struct sockaddr_in  addr;
      int                 i;
      gchar              *to_free;

      for (i = 0; i < G_N_ELEMENTS(strv)-1; i++)
        strv[i] = "foo\n";
      strv[G_N_ELEMENTS(strv)-1] = NULL;

      data = to_free = g_strjoinv(NULL, strv);
      remaining = strlen(data);

      fd = socket(AF_INET, SOCK_STREAM, 0);

      memset(&addr, 0, sizeof(struct sockaddr_in));
      addr.sin_family      = AF_INET;
      addr.sin_port        = htons(1234);
      addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);

      if (connect(fd, (struct sockaddr *)&addr, sizeof(addr)) == -1)
        {
          fprintf(stderr, "Error connecting to server: %s\n", strerror(errno));
          return 1;
        }

      fcntl(fd, F_SETFL, O_NONBLOCK);

      io_channel = g_io_channel_unix_new(fd);
      io_watch = g_io_add_watch(io_channel,
                                G_IO_OUT,
                                (GIOFunc)socket_writable,
                                GINT_TO_POINTER(fd));

      g_idle_add(busy_loop, NULL);

      main_loop = g_main_loop_new(NULL, FALSE);

      g_main_loop_run(main_loop);
      g_main_loop_unref(main_loop);

      g_source_remove(io_watch);
      g_io_channel_unref(io_channel);

      close(fd);

      g_free(to_free);

      return 0;
    }

Here I create a non-blocking socket, set up an 'I/O watch' to tell me
when the socket is writable and, when it is, I keep blasting data into
the socket until I get an EAGAIN. This is the point at which write()
would block if it was a blocking socket and I return TRUE from the
callback to say "call me again when the socket is writable". Only when
I've finished writing all of the data do I return FALSE and quit the
main loop causing the g\_main\_loop\_run() call to return.

The point about task priorities is illustrated nicely here. GLib does
have the concept of priorities and has a "idle callback" facility you
can use to run some code when no higher priority task is waiting to run.
In this case, the busy\_loop() function will \*only\* run when the
socket is not writable.

### Tulip

There's a lot of talk lately about [Guido's Asynchronous IO Support
Rebooted (PEP3156)](http://www.python.org/dev/peps/pep-3156/) efforts
so, of course, we've got to have a look at that.

One interesting aspect of this effort is that it aims to support both
the coroutine and callbacks style programming models. We'll try out both
models below.

Tulip, of course, has an event loop, time-based callbacks, I/O callbacks
and I/O helper functions. We can build a simple variant of our
non-blocking I/O example above using tulip's event loop and I/O
callback:

    import errno
    import select
    import socket

    import tulip

    sock = socket.socket()
    sock.connect(('localhost', 1234))
    sock.setblocking(0)

    buf = memoryview(str.encode('foo\n' * 2 * 1024 * 1024))
    def do_write():
        global buf
        while True:
            try:
                buf = buf[sock.send(buf):]
            except socket.error as e:
                if e.errno != errno.EAGAIN:
                    raise e
                return

    def busy_loop():
        i = 0
        while i < 5000000:
            i += 1
        event_loop.call_soon(busy_loop)

    event_loop = tulip.get_event_loop()
    event_loop.add_writer(sock, do_write)
    event_loop.call_soon(busy_loop)
    event_loop.run_forever()

We can go a step further and use tulip's Protocol abstraction and
connection helper:

    import errno
    import select
    import socket

    import tulip

    class Protocol(tulip.Protocol):

        buf = b'foo\n' * 10 * 1024 * 1024

        def connection_made(self, transport):
            event_loop.call_soon(busy_loop)
            transport.write(self.buf)
            transport.close()

        def connection_lost(self, exc):
            event_loop.stop()
     
    def busy_loop():
        i = 0
        while i < 5000000:
            i += 1
        event_loop.call_soon(busy_loop)

    event_loop = tulip.get_event_loop()
    tulip.Task(event_loop.create_connection(Protocol, 'localhost', 1234))
    event_loop.run_forever()

This is pretty similar to the twisted example and shows up yet another
example of the lack of task prioritization being an issue. If we added
the busy loop to the event loop before the connection completed, the
scheduler would run the busy loop every time the connection task yields.

### Coroutines, Generators and Subgenerators

Under the hood, tulip depends heavily on generators to implement
coroutines. It's worth digging into that concept a bit to understand
what's going on.

Firstly, remind yourself how a generator works:

    def gen():
        i = 0
        while i < 2:
            print(i)
            yield
            i += 1

    i = gen()
    print("yo!")
    next(i)
    print("hello!")
    next(i)
    print("bye!")
    try:
        next(i)
    except StopIteration:
        print("stopped")

This will print:

    yo!
    0
    hello!
    1
    bye!
    stopped

Now imagine a generator function which writes to a non-blocking socket
and calls yield every time the write would block. You have the
beginnings of coroutine based async I/O. To flesh out the idea, here's
our familiar example with some generator based infrastructure around it:

    import collections
    import errno
    import select
    import socket

    sock = socket.socket()
    sock.connect(('localhost', 1234))
    sock.setblocking(0)

    def busy_loop():
        while True:
            i = 0
            while i < 5000000:
                i += 1
            yield

    def write():
        buf = memoryview(b'foo\n' * 2 * 1024 * 1024)
        while len(buf):
            try:
                buf = buf[sock.send(buf):]
            except socket.error as e:
                if e.errno != errno.EAGAIN:
                    raise e
                yield
        quit()

    Task = collections.namedtuple('Task', ['generator', 'wfd', 'idle'])

    tasks = [
        Task(busy_loop(), wfd=None, idle=True),
        Task(write(), wfd=sock, idle=False)
    ]

    running = True

    def quit():
        global running
        running = False

    while running:
        finished = []
        for n, t in enumerate(tasks):
            try:
                next(t.generator)
            except StopIteration:
                finished.append(n)
        map(tasks.pop, finished)

        wfds = [t.wfd for t in tasks if t.wfd]
        timeout = 0 if [t for t in tasks if t.idle] else None

        select.select([], wfds, [], timeout)

You can see how the generator-based write() and busy\_loop() coroutines
are cooperatively yielding to one another just like greenthreads in
eventlet would do. But, there's a pretty fundamental flaw here - if we
wanted to refactor the code above to re-use that write() method to e.g.
call it multiple times with  
different input, we'd need to do something like:

    def write_stuff():
        for i in write(b'foo' * 10 * 1024 * 1024):
            yield
        for i in write(b'bar' * 10 * 1024 * 1024):
            yield

but that's pretty darn nasty! Well, that's the whole idea behind [Syntax
for Delegating to a Subgenerator
(PEP380)](http://www.python.org/dev/peps/pep-0380/). Since python 3.3, a
generator can now yield to another generator using the 'yield from'
syntax. This allows us to do:

    ...
    def write(data):
        buf = memoryview(data)
        while len(buf):
            try:
                buf = buf[sock.send(buf):]
            except socket.error as e:
                if e.errno != errno.EAGAIN:
                    raise e
                yield

    def write_stuff():
        yield from write(b'foo\n' * 2 * 1024 * 1024)
        yield from write(b'bar\n' * 2 * 1024 * 1024)
        quit()

    Task = collections.namedtuple('Task', ['generator', 'wfd', 'idle'])

    tasks = [
        Task(busy_loop(), wfd=None, idle=True),
        Task(write_stuff(), wfd=sock, idle=False)
    ]
    ...

### Conclusions?

Yeah, this is the point where I've figured out what we should do in
OpenStack. Or not.

I really like the explicit nature of Tulip's model - for each async
task, you explicitly decide whether to block the current coroutine on
its completion (or put another way, yield to another coroutine until the
task has completed) or you register a callback to be notified of the
tasks completion. I'd much prefer this to rather cavalier "don't worry
your little head" approach of hiding the async nature of what's going
on.

However, the prospect of porting something like Nova to this model is
more than a little dauting. If you think about the call stack of an REST
API request being handled and ultimately doing an rpc.cast() and that
the entire call stack would need to be ported to 'yield from' in order
for us to yield and handle another API request while waiting for the
result of rpc.cast() .... as I said, daunting.

What I'm most interested in is how to [design our new messaging
API](https://wiki.openstack.org/wiki/Oslo/Messaging) to be able to
[support any and all of these models in
future](http://lists.openstack.org/pipermail/openstack-dev/2013-May/009784.html).
I haven't quite figured that out either, but it feels pretty doable.
