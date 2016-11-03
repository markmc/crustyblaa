Title: Voodoo
Date: 2004-02-28 20:58
Author: markmc
Tags: GNOME, Programming
Slug: voodoo
Status: published

I hate now knowing how things work. Especially things that I  
rely on heavily as a hacker. But I love it when I get a chance  
to finally figure out how the damn thing works and it turns out  
to be beautifully simple.

This week I found that I had to debug a small part of libtool's  
behaviour. It had always worked for me before and I had assumed  
it worked a certain way, but in this case it just wasn't  
working properly. I could feel myself breaking out in a cold  
sweat. *Don't make me debug libtool! Please God, noooo...*

But the clouds parted. And it was simple.

When you build an executable, and it links against a library  
in the same module, you need some way to be able to run that  
uninstalled executable with the uninstalled library. So,  
libtool puts a script where you think your uninstalled  
executable should be and here's what it does

-   When you run the script for the first time, it re-links  
   your executable with `--rpath $path-to-lib/.libs` and  
   places that executable in `.libs/lt-myexec`.
-   That causes the linker to to put a `DT_RPATH` ELF  
   attribute in the executable which tells the dynamic loader  
   where to looks for libraries. (See the ld.so manpage)
-   And finally, the script just runs the modified executable.

For example:

      $> ls -l .libs/*gdk-pixbuf-csource
      -rwxrwxr-x    1 markmc   markmc      51262 Feb 26 11:28 .libs/gdk-pixbuf-csource
      $> ./gdk-pixbuf-csource
      Usage: gdk-pixbuf-csource [options] [image]
      $> ls -l .libs/*gdk-pixbuf-csource
      -rwxrwxr-x    1 markmc   markmc      51262 Feb 26 11:28 .libs/gdk-pixbuf-csource
      -rwxrwxr-x    1 markmc   markmc      51294 Feb 28 15:48 .libs/lt-gdk-pixbuf-csource
      $> objdump -p .libs/gdk-pixbuf-csource | grep RPATH
      $> objdump -p .libs/lt-gdk-pixbuf-csource | grep RPATH
        RPATH       /gnome/head/cvs/gtk+/gdk-pixbuf/.libs:/gnome/head/INSTALL/lib
      $> ldd .libs/gdk-pixbuf-csource | grep gdk_pixbuf
              libgdk_pixbuf-2.0.so.0 => /gnome/head/INSTALL/lib/libgdk_pixbuf-2.0.so.0 (0x0087d000)
      $> ldd .libs/lt-gdk-pixbuf-csource | grep gdk_pixbuf
              libgdk_pixbuf-2.0.so.0 => /gnome/head/cvs/gtk+/gdk-pixbuf/.libs/libgdk_pixbuf-2.0.so.0 (0x004a0000)

Not exactly, earth shattering. But nice to know.
