Title: Runtime Linker Voodoo
Date: 2004-04-06 21:33
Author: markmc
Tags: Fedora, Programming, GNOME
Slug: runtime-linker-voodoo
Status: published

Kjartan pointed out a report of a gnome-session security vulnerability  
to me earlier today. Now, it turns out to actually only be a  
vulnerability in a script supplied with certain distributors' packages,  
but that's not the interesting part.

The script contained something like this:

      export LD_LIBRARY_PATH=/opt/gnome/lib:$LD_LIBRARY_PATH

and the "vulnerability" was apparently that if *\$LD\_LIBRARY\_PATH*  
was originally unset, then you get  
*LD\_LIBRARY\_PATH="/opt/gnome/lib:"*.

I couldn't for the life of me understand why it was actually a  
vulnerability in the first place. It gnawed at me all day. After a bit  
of poking at the runtime linker code in glibc though I realized that  
setting *\$LD\_LIBRARY\_PATH* like that is effectively the same as  
setting it to *LD\_LIBRARY\_PATH="/opt/gnome/lib:./"*. The problem is  
clear then - an attacker can use it to force a rogue, untrusted  
library to be loaded that could do nasty things.

So, this whole *LD\_LIBRARY\_PATH=":"* causing "./" to be added to  
the runtime linker's search path thing came as a big suprise to me and  
to some others. I'd never heard of before, but it seems known to at  
least some people and is "expected behavior". What worries me here is  
that its likely most attackers know to look out for this and most  
developers don't.

My long search for a normative reference for this behaviour failed. If  
anyone knows where it comes from, I'm dead curious. I expect Ulrich  
knows, though :-)

Another interesting thing to play with:

    $> LD_DEBUG=help /lib/ld-linux.so.2
    Valid options for the LD_DEBUG environment variable are:
     
      libs        display library search paths
      reloc       display relocation processing
      files       display progress for input file
      symbols     display symbol table processing
      bindings    display information about symbol binding
      versions    display version dependencies
      all         all previous options combined
      statistics  display relocation statistics
      help        display this help message and exit

I read a [paper  
from Ulrich](http://people.redhat.com/drepper/dsohowto.pdf) some time
ago that gave lots of details on how to write  
shared libraries such that the runtime linker can more efficiently  
resolve symbols etc. *LD\_DEBUG=statistics*, among other things,  
is useful there. I'd love to see someone with the time and interest  
looking into this and analyzing GNOME libraries to see where we can  
make improvements.
