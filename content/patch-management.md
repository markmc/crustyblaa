Title: Patch Management
Date: 2006-04-25 05:45
Author: markmc
Category: General
Slug: patch-management
Status: published

As part of the work I've started doing on [Stateless
Linux](http://fedoraproject.org/wiki/StatelessLinux), I've found myself
hacking on [device-mapper](http://sources.redhat.com/dm/)'s snapshot
support. It's actually been really good fun to do a bit of kernel
hacking again after such a long time ... and this time I feel like I
actually have some clue what I'm doing.

I'm really behind the times when it comes to all the new fangled
revision control systems out there like bzr, git, mercurial, svn etc. -
cvs and manual patch mangling is all I know.

So, when [agk](http://www.kernel.org/pub/linux/kernel/people/agk)
pointed me at [quilt](http://savannah.nongnu.org/projects/quilt/), I was
a bit dubious at first but gave it a shot. It turned out to be a really
simple and useful way of maintaining your own
[patchset](http://www.gnome.org/~markmc/code/dm-patches/) in parallel
with an upstream codebase.

Even though it's a really simple tool, it seems to me to have some of
the important advantages of other systems like distributed offline
branches and change sets. If I had time to hack on GNOME again, I'd use
quilt a lot for offline branches alongside CVS. It's given me an
appetite for looking at other systems too.
