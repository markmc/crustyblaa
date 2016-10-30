Title: GObject Private Data
Date: 2006-01-25 03:35
Author: markmc
Category: General
Slug: gobject-private-data
Status: published

[Federico:](http://primates.ximian.com/~federico/news-2006-01.html#24)
the combination of a "\*priv" field and GObject private data is the best
way to go:

    struct _PangoFcFont
    {
       ...
       gpointer priv;
       ...
    };

    #define PANGO_FC_FONT_GET_PRIVATE(obj) ((PangoFcFontPrivate *) ((PangoFcFont *) obj)->priv)

    static void
    pango_fc_font_class_init (PangoFcFontClass *class)
    {
      ...
      g_type_class_add_private (object_class, sizeof (PangoFcFontPrivate));
    }

    static void
    pango_fc_font_init (PangoFcFont *fcfont)
    {
      fcfont->priv = G_TYPE_INSTANCE_GET_PRIVATE (fcfont, PANGO_TYPE_FC_FONT, PangoFcFontPrivate)
    }

Indeed, that's [why `g_type_get_private()` was
added](http://mail.gnome.org/archives/gtk-devel-list/2003-January/msg00004.html).
You get the best of both worlds - the convenience of a priv pointer with
the fact that the private data is allocated in the same chunk as the
object itself, without the inefficiency of calling `get_private()` a lot
or the extra static variable in [Owen](http://www.fishsoup.net/blog)'s
original proposal.
