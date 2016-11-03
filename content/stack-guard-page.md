Title: Stack Guard Page
Date: 2005-05-11 16:41
Author: markmc
Tags: Fedora, Programming
Slug: stack-guard-page
Status: published

The most interesting little tidbit I learnt from the memory usage  
debugging
[yesterday](http://blogs.gnome.org/nb.cgi/view/markmc/2005/05/10/0) was  
about the "stack guard page". Look at this bit in the strace:

    mmap2(NULL, 10489856, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7219000
    mprotect(0xb7219000, 4096, PROT_NONE)   = 0
    clone(child_stack=0xb7c194c4, flags=CLONE_VM|...) = 2282

What's going on here is that libc is mapping an area for the thread's  
stack, just before spawning thread. The interesting bit is that, using  
`mprotect()`, it also changes the permissions on the first page  
(the page at the top of the stack) such that any instruction which  
attempts to write to the page will cause a segmentation fault.

That's your stack guard page; it means that your infinitely recursing  
function won't go off an scribble over its neighbouring thread's stack,  
it'll just segfault like a good little thread.

(In true pthreads tradition, you can even configure the size of  
this guard area - see the pthread\_attr\_setguardsize() manpage)
