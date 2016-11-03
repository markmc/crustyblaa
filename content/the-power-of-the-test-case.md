Title: The Power Of The Test Case
Date: 2004-06-10 19:34
Author: markmc
Tags: GNOME
Slug: the-power-of-the-test-case
Status: published

Thanks to Tim Waugh, before we even started, we knew one of the
stumbling  
blocks for this terminal services thing was going to be VNC's ZRLE
encoding.  
You see, in order to make the hot-desking thing work you need to be
able  
to transfer a VNC client between two VNC servers without the client
knowing  
about it.

What makes the ZRLE encoding difficult is that it compresses the pixel  
stream using zlib and this introduces state into the VNC stream. A
rectangle  
of encoded pixel data now depends on the pixels that went before. So
when,  
you transfer a client between servers, the new server either needs to
know  
the state of the zlib stream or you need to allow the new server to
start  
with a clean slate somehow.

A glance at the zlib [docs](http://www.gzip.org/zlib/manual.html)  
and the *Z\_FULL\_FLUSH*/*Z\_FINISH* *deflate()* flags jumped out  
of me. Sweet, this is going to be trivial, says he. Like a good
engineer,  
I started writing a [  
test case](http://www.gnome.org/~markmc/code/test-zlib.c) to prove the
idea. The solution wasn't as obvious as I'd hoped,  
though, and I found myself knee deep in docs, rfcs and the *inflate()*/  
*deflate()* code. Unfortunately, I had to actually **understand**  
what the hell was going on. The horror!

Plugged the code into Xvnc and tried it out. Broken. Dramatically
broken. Debug,  
tweak, test. Still broken. And on it went. Eventually, hours later, I
went back  
to my test case and discovered that it actually wasn't working. It was
sneakily  
pretending to be working. But it wasn't. Trivial fix and all is well.

You can save so much time by figuring stuff out in a small test case
rather  
than trying to figure it out in the context of a huge mass of code with
a million  
and one other things happening. I know this to be true, and as time goes
on  
I'm learning just how true it is. But you still find yourself launching
headlong  
into problems thinking "it looks trivial, in the same time I'd write a
test case  
I'll have the thing fixed" and only hours and hours later do you get a
clue  
and start writing a test case. I get the feeling Owen always reaches
straight  
for a test case. Maybe that's his secret :-)

Anyway, I've moved on to adding TLS/SSL support Xvnc and vncviewer now.
And,  
yes, I'm going to go through all this "state flushing" pain again. Fun  
all the way, I tell ya ... Now, where's my test case?

On the plus side, I've had to take loads of breaks from this stuff
today,  
and I've been cooking. Had a gorgeous  
[ratatouille](http://en.wikipedia.org/wiki/Ratatouille) for lunch  
and some [chilli](http://en.wikipedia.org/wiki/Chili_con_carne)  
is bubbling away as I type.
