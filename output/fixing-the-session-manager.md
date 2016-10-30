Title: Fixing the Session Manager
Date: 2004-09-15 08:31
Author: markmc
Category: General
Slug: fixing-the-session-manager
Status: published

There's lots of talk at the moment about "fixing the session manager",  
a sentiment I agree with, but I worry that if we don't step back and  
look at the big picture a bit we'll screw things up even more.

To me, "Session Management" is all about providing the ability to take  
a snapshot of what you're doing right now, log out and be able to come  
back later, log in and continue where you left off. So if I saved  
the state of my session I'd expect following to be remembered:

-   the applications which are running, and the windows belong to  
   those applications which are open
-   the size and position of all those windows
-   which documents I have open, the position within those  
   documents etc.

Alternatively, people seem to set things up just how they'd like it  
when they log in every morning and take a snaphot of the session at  
that point.

This is the kind of functionality which XSMP was designed for but it  
hasn't yet worked out very well because most applications don't do a  
good job of implementing it and there's not a lot of clarity on how  
session state differs from application state (e.g. when you close your  
browser, should it remember the last position of the window or should  
it only remember that when you save your session?)

Anyway, lets forget about this feature for the moment. We do our best  
to hide it in GNOME because we know its broken and my impression is  
that most people don't bother with it because of its brokeness. I'm  
not too concerned about fixing it right now.

There's this whole other thing the session manager does, though. It  
starts what we think of as the "desktop shell" - the window manager,  
panel, nautilus, screensaver daemon, settings daemon etc. etc. I think  
most user's mental model of the desktop would be that all these  
components make up a single entity in which different applications  
run. Whether the panel is running isn't a part of transient session  
state in the same way as whether the browser is running, its a fixed  
part of the desktop.

Making this distinction gives us the ability to treat the session  
shell and transient session state differently. But to what end? Well,  
there's a number of thing we can do differently if we treat the  
management of the session shell as a different problem:

1.  We stop forcing users to understand that in order to have certain  
   desktop services started at login they must run them and then  
   save the session.
2.  We consolidate all the hard-coded hacks for starting desktop  
   services into a single mechanism whereby desktop services can  
   register themselves with the session manager and asked to be  
   started up based on a user preference.
3.  We remove the possibility of "losing" important parts of the  
   desktop from your session
4.  We can start the session in two stages - the desktop shell  
   followed by the applications, perhaps hiding the entire screen  
   until the desktop has started
5.  We can remove obtuse terms like "Metacity Window Manager", "The  
   Panel", "Nautilus" from the splash screen and just have "Starting  
   GNOME".
6.  Since we won't have to worry about managing legacy applications,  
   we can think about dumping XSMP and coming up with a solution  
   specifically designed for starting the desktop itself

Here's another way to look at it - if you save your session while  
you're running GNOME, wouldn't it make sense that when you log in to  
KDE the same applications are running? If the answer to that is yes, I  
think it shows that the question of activating desktop shell  
components is orthogonal to the question of restoring session state on  
login.
