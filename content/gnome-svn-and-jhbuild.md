Title: GNOME SVN and jhbuild
Date: 2007-01-02 07:20
Author: markmc
Category: General
Slug: gnome-svn-and-jhbuild
Status: published

If you're wondering how to move your GNOME
[jhbuild](http://www.jamesh.id.au/software/jhbuild) from CVS now that
the [SVN migration](http://live.gnome.org/SubversionMigration) has
happened ... here's what I had to do.

-   Checkout jhbuild from SVN:

          $> mkdir -p /gnome/head/svn && cd /gnome/head/svn
          $> svn co svn+ssh://markmc@svn.gnome.org/svn/jhbuild/trunk jhbuild
          $> make install

-   Update `~/.jhbuildrc` so that e.g.

          repos['svn.gnome.org'] = 'svn+ssh://markmc@svn.gnome.org/svn/'
          checkoutdir = '/gnome/head/svn'

-   Copy `/gnome/head/cvs/pkgs` to `/gnome/head/svn/pkgs` so that you
    won't have to download as many new tarballs
-   Run `jhbuild build`

Note, this is with the `gnome-2.18` moduleset. Things are still a little
in flux right now.
