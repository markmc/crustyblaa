Title: Xen and X Pointer Issues
Date: 2006-09-29 05:46
Author: markmc
Tags: Xen
Slug: xen-and-x-pointer-issues
Status: published

Just back from a nice relaxing holiday and, at first, I was totally
perplexed by all this talk of the [Xen "absolute pointer"
problem](http://zaitcev.livejournal.com/91485.html). "It's just VNC", I
thought, "it can't be that hard. It must be just a simple bug
somewhere".

The background is:

-   In Xen guests we have a "xenfb" driver, which acts just like a
    normal framebuffer device as far as the Xserver is concerned, but
    the contents of the framebuffer is exported to Dom0 via XenBus and
    shared memory.
-   Similarly, we have a "xenkbd" driver, which takes input events from
    Dom0 and makes them available to the Xserver.
-   In Dom0, we have a little daemon which acts as a VNC server. It
    exports the framebuffer contents from the guest and injects input
    events into the guest.

The problem here is that pointer motion events arrive at the Xserver as
if they came directly from hardware. And just like normal mouse events,
they are relative - i.e. you move your mouse up X amount and across Y
amount.

This is unusual, because a VNC server receives motion events with
absolute co-ordinates and can normally warp the pointer to those exact
co-ordinates.

What we have might not be too bad - we might be able to reliably control
the absolute pointer position in X by injecting events with relative
co-ordinates - except that these events are subject to acceleration. If
we try and move the pointer by injecting an event that says "move 100
pixels to the right", the Xserver may accelerate that and move it, say,
200 pixels (with a ratio of 2/1). So,
[Pete's](http://zaitcev.livejournal.com/) first going to come up with a
quick hack to disable acceleration.

It's still stupid to try and move the pointer to an absolute position by
injecting relative pointer motion events, though. The ideal solution is
that the pointer device in the Xen guest behaves just like a grapics
tablet. We would pass the absolute pointer co-ordinates to the guest and
the driver would pass those on to the Xserver as though it was tablet
device.
