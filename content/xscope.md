Title: xscope
Date: 2005-07-28 17:55
Author: markmc
Category: General
Slug: xscope
Status: published

[xscope](http://www.keithp.com/cvs/xscope) is so damn useful.

Here's a
[patch](http://www.gnome.org/~markmc/code/xscope-support-shape-extension.patch)
to make it support the SHAPE extension. It'd be really good to get this
thing into freedesktop.org and so people can hack on it to make it sane.

I should try out [Soeren's gtk xscope
wrapper](http://mail.gnome.org/archives/gnome-hackers/2003-August/msg00026.html).

I'm not sure what's the best way to build the thing, but if you check it
out from keithp's CVS and do:

    $> imake -I/cvs/xorg/config/cf
    $> make

then it seems to build just fine if you remove the `malloc()` prototype
in `common.c`. Of course, if you have a space between the `-I` and the
path to the xorg build on the imake command line, then you could find
yourself spending a long time trying to figure out wtf is wrong.

Oh, yeah, one final tip. xscope is a proxy Xserver. So, when you connect
your app to xscope, Xlib goes looking in `~/.Xauthority` for an xauth
cookie to use when authenticating. Because xscope has a different
display number from the parent display, though, you need to use xauth to
setup the cookie for this display number too. So, assuming the parent
display is `:0` and xscope is `:1`, you can do:

    $> xauth list | grep '/unix:0' | while read display proto cookie; do xauth add ${display%0}1 $proto $cookie; done

</p>

