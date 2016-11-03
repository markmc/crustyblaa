Title: Fedora 9 Xen pv_ops
Date: 2008-02-11 10:15
Author: markmc
Tags: Xen
Slug: fedora-9-xen-pv_ops
Status: published

For the past couple of weeks, I've been helping out with the [Fedora 9
pv\_ops effort](http://fedoraproject.org/wiki/Features/XenPvops),
specifically helping get the pv\_ops based dom0 kernel going.

Well, following on from [sct getting
dom0](http://berrange.com/personal/diary/2008/02/progress-in-fedora-9-xen-pvops-kernel)
booting, I made a nice breakthrough this morning - a pv\_ops dom0
booting a pv\_ops domU:  
` $> dmesg | grep paravirt Booting paravirtualized kernel on Xen $> virsh create ./test-domu.xml Domain Test created from ./test-domu.xml $> virsh console Test | grep paravirt Booting paravirtualized kernel on Xen`

What's this pv\_ops business all about? Well, as [Dan
explained](http://berrange.com/personal/diary/2007/11/plan-for-xen-kernels-in-fedora-9),
for a long time we've been forward-porting Xensource's (now 2.6.18
based) kernel tree in an effort to try and have our Xen kernel not lag
behind Fedora's bare-metal kernel. Now that the upstream kernel has
gained the ability to run on Xen using pv\_ops (but only as i386 DomU,
currently) we've taken the decision to stop wasting our time forward
porting Xensource's tree and put all our focus into improving the
feature set of pv\_ops based Xen.

pv\_ops itself is a set of hooks in the kernel so that support for
running on different hypervisors can be cleanly added to the kernel,
with the added bonus that the kernel can detect at runtime which
hypervisor it is running on and adapt itself accordingly. This means
that, in the long run, Xen support should be more akin to a device
driver than a huge fork of the kernel.

(Note: for any others who ever to debug Xen's booting of a guest, here's
a [tiny Xen domain
builder](http://www.gnome.org/~markmc/code/test-xen-domain-builder.c))
