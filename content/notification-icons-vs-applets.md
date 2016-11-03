Title: Notification Icons vs. Applets
Date: 2004-09-15 09:59
Author: markmc
Tags: GNOME
Slug: notification-icons-vs-applets
Status: published

It saddens me to see people writing applets as notification icons  
because I've been there myself and spent a good deal of time trying to  
get traction on the problem but ended up dropping the ball.

The Network Monitor started out as a notification icon. But I was  
[unhappy](http://mail.gnome.org/archives/desktop-devel-list/2003-June/msg00343.html)  
with that for a number of reasons:

1.  No consensus on what the notification area should be used for.
    Until  
   we have that, I'm worried about serious notification area bloat.
2.  No reasonable way of starting standalone notification icons short
    of  
   "start gnome-netstatus and save your session"
3.  Other less fundamental problems - no keynav, no decent notification  
   icon widget, can't re-arrange icons, problems expanding icons to
    the  
   full panel width ...

I think we got tantalizingly [close  
to
consensus](http://mail.gnome.org/archives/desktop-devel-list/2003-March/msg00351.html)
on the first problem, and `EggStatusIcon` is  
an okay start on a widget, but in the end I ran out of time and turned  
the Network Monitor into an applet.

Granted, I didn't care whether or not the Network Monitor worked in  
KDE. Cross-desktop applets isn't an intractable problem, but just  
lumping everything into the notification area is no way to approach  
it.

Anyway, what I really wanted to mention was that I don't think problem  
(2) above is a [session manager  
problem](http://blogs.gnome.org/nb.cgi/view/markmc/2004/09/15/0). The
notification area itself should manage these icons,  
not the session manager ... if the panel isn't running or the  
notification area isn't on the panel, these icons shouldn't be running,  
right?

At some point we discussed the idea that each notification icon should  
install a .desktop file describing the icon. In the preferences dialog  
you could enable/disable each icon. If the icon is standalone (like  
the Network Monitor) it would have an `Exec` field and the  
notification area would spawn it if enabled. If the icon is part of an  
application (e.g. the epiphany download icon) the notification area  
would only allow the icon to be displayed if its enabled.

All this reminded me that I actually had a good
[argument](http://mail.gnome.org/archives/desktop-devel-list/2003-March/msg00354.html)  
against every application developer's favourite feature - "Minimise to  
Notification Area". Don't argue with a butler analogy!
