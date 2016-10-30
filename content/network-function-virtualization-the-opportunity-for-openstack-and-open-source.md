Title: Network Function Virtualization - The Opportunity for OpenStack and Open Source
Date: 2014-10-02 20:28
Author: markmc
Category: openstack
Slug: network-function-virtualization-the-opportunity-for-openstack-and-open-source
Status: published

This week's [launch of
OPNFV](https://www.openstack.org/blog/2014/09/telcos-mobilizing-to-drive-nfv-adoption/)
is a good opportunity to think about a simmering debate in the OpenStack
developer community for a while now - what exactly does NFV have to do
with OpenStack, and is it a good thing?

My own “journey” on this started exactly one year ago today when I
visited a local Red Hat partner to talk about OpenStack and, towards the
end of our Q&A, I was asked something like “will OpenStack support
NFV?”. I’d never heard of the term and, when the general idea was
explained, I gave a less than coherent version of “OpenStack implements
an elastic cloud for cattle; this sounds like pets. Sorry”. After the
meeting, the person who asked the question forwarded me an NFV
whitepaper from October 2012 and, glancing through it, most of it went
right over my head and I didn’t see what it had to do with OpenStack.

Since then, Chris Wright has been patiently talking me through this
space and gently trying to get me over my initial skepticism. Chris
would say that our conversations has helped him refine how he explains
the concepts to open-source developers, and I think he really nailed it
in his keynote at the Linux Foundation’s Collaboration summit in April.

\[embed\]https://www.youtube.com/watch?v=SAimeBttapA\[/embed\]

In his keynote, Chris talks about the benefits of collaboration in
open-source and walks through all of the various aspects of how the
networking industry is changing, and how open-source is playing a key
part in all of those changes. He covers, and simplifies:

-   Taking the current architecture of proprietary, expensive, complex,
    difficult to manage forwarding devices (like routers) and how SDN
    (Software Defined Networking) aims to “put an API on it”. This is
    what’s meant by “disaggregation of the control plane and data
    plane” - that forwarding devices become devices which are controlled
    by open standards, and allows your distributed system of forwarding
    devices to be controlled and automated.
-   NFV (Network Function Virtualization) as a shift in the telco
    data-center world which embraces many of the lessons that the
    elastic infrastructure cloud has taught the IT industry. More on
    that below.
-   Changes in the “data plane” world, where we’re starting to see the
    network device market mimic the x86 server market such that these
    devices can be “white box” servers running open-source software.
    Again that disaggregation word, but this time it’s about
    “disaggregation of hardware and software” and how the software part
    can be open-source implementations of optimized packet-forwarding
    capabilities which we’re used to seeing implemented in expensive and
    proprietary hardware appliances.

But let’s focus here on NFV.

I real don’t know much about the telco industry, but what Chris has me
imagining now is data-centers full of proprietary, black-box hardware
appliances which are collectively know as “network functions” or “middle
boxes”. These boxes are used for everything from firewalls, NAT, deep
packet inspect (DPI), the mobile packet core, etc. These are software
applications trapped in hardware. They’re expensive, proprietary, slow
to roll-out, don’t always scale well and are hindering telco service
providers as they attempt to react to a rapidly changing market.

NFV is about completely re-thinking the architecture of these
data-centers. This is the telco industry re-imaging their data centers
as elastic infrastructure clouds running their “network functions” as
virtualized, horizontally scalable applications on these clouds. The
exciting - simply stunning - aspect of all of this for me as an
open-source advocate, is that the telco industry is settling on a
consensus around an architecture involving open-source generally and
OpenStack specifically.

Say that again? These huge telcos want to rebuild their entire data
centers with OpenStack and open-source? Yes.

If, like me, you want to see open-source change the IT world into one
where we all embrace the opportunity to collaborate in the open, while
still successfully building building businesses that serve our users’
needs … then this sounds pretty cool, right?

If, like me, you want to see OpenStack as the standard platform from
which many of the worlds’ elastic infrastructure clouds are built ...
then this sounds like a no-brainer, right?

Well, the thing we need to bear in mind is that these applications (i.e.
network functions) are pretty darn specialized. They need to have a high
level of performance, determinism and reliability. But that does not
necessarily mean they are “pets” and missing one of the key points of an
elastic cloud.

Let’s take the reliability requirement - when these network functions
are implemented as horizontal scale-out applications, they will look to
achieve high levels of reliability in the same way that typical cloud
applications do - with each tier of the application spread across
multiple failure domains, and by spreading application load
horizontally. Telcos will just want to take this further, with faster
and more deterministic response to failures, while also avoiding any
compromise to application's performance. For example, you’ll see a lot
of interest in how instances are scheduled to take to into account
affinity and anti-affinity within an instance group.

The performance requirement is largely about high-performance packet
processing. How to get a packet off the network, into a VM, processed
quickly and back out again on the network. One of the techniques being
pursued is to give VMs direct physical access to the network via SR-IOV
which, in turn, means the compute scheduler needs to know which physical
networks the NICs on each compute node has access to.

The deterministic requirement is about predictable performance. How to
avoid the vagaries of the hypervisor and host OS scheduler affecting
these performance-sensitive applications? You’ll see work around
allowing operators to define flavors, and application owners to define
image properties, which between them control things like vCPU topology,
vCPU to pCPU pinning, the placement of applications in relation to NUMA
nodes and making huge pages available to the applications. Compare to
Amazon’s memory-optimized and compute-optimized flavors, and imagine
this being taken a step further.

Oh, and another requirement you’ll see come up in this space a lot is …
IPv6 everywhere! I’m certainly down with that.

Want to learn more about the work involved? See [the OpenStack NFV
team's amazing wiki page](https://wiki.openstack.org/wiki/Teams/NFV)
which goes into excruciating detail.

The more you dig into the specifics of what we’re talking about here,
start breaking this down into tangible concepts without all the acronyms
and buzzwords, you start to realize that this really is the telco world
embracing everything that OpenStack is all about, but just pushing the
envelope a bit with some requirements which are a pretty natural
evolution for us, but we might not otherwise have expected to come about
for some time yet.

I guess the summary here is that if you're skeptical, that's cool ...
you're not alone. But please do take the time to see through the
complexity and confusion to the simple fact we're poised to be a key
part in turning the telco data-center, and how this is just another
exciting part of [our goal to "to produce the ubiquitous Open Source
Cloud Computing platform"](https://wiki.openstack.org).
