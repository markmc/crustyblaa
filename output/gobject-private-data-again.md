Title: GObject Private Data (again)
Date: 2006-01-25 13:15
Author: markmc
Category: General
Slug: gobject-private-data-again
Status: published

Aren't discussions via blogs fun? :)

[Federico](http://primates.ximian.com/~federico/news-2006-01.html#25):
two points:

1.  Using the new GObject instance private data API, rather than the
    private data scheme that GNOME hackers have always used, is a small
    optimization in itself - the private data is allocated in the same
    chunk as the object itself.

    As with all optimizations, you weigh up the benefit against the
    code obfuscation. In this case, I don't think the GObject scheme
    makes the code more difficult to understand ... especially since
    it's likely to become as much of a second-nature idiom as the
    old scheme. It's also one less opportunity to leak memory.

2.  Using the GObject scheme, instance private data could have been
    added without the runtime hit you were seeing ... even where the
    object structure couldn't be extended without breaking ABI.

    To do so, you'd just go back to something similar to Owen's initial
    suggestion for how the API should be used - in a static variable,
    you'd store the offset between the address of the object structure
    and the private data and use that offset for efficient access to
    the data. `add_private()` originally returned this offset, but it no
    longer does, so you'd need to calculate the offset in
    `instance_init()` - but it is guaranteed to be constant.

    Granted, that's a *nasty* hack which would genuinely obfuscate the
    code ... but at least it would actually be possible to add private
    data, whereas it wouldn't be possible with the old scheme.

    **Update**: [Tim points
    out](http://blogs.gnome.org/view/markmc/2006/01/25/2#comments) that
    the offset to the private data isn't constant across all instances -
    the offset will be larger for subtypes since the private data is
    allocated after *all* object data.


