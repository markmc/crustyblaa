Title: June 20th OpenStack Foundation Board Meeting
Date: 2017-06-20 11:00
Author: markmc
Tags: OpenStack, OpenStack Foundation Board Meeting
Slug: june-20-openstack-foundation-board-meeting
Status: published

The [OpenStack Foundation Board of
Directors](https://www.openstack.org/foundation/board-of-directors/)
met for a [two hour conference call on
Tuesday](https://wiki.openstack.org/wiki/Governance/Foundation/20June2017BoardMeeting). The
usual disclaimer applies - this my informal recollection of the
meeting. It’s not an official record. Jonathan Bryce has [posted an
official summary of the
meeting](http://lists.openstack.org/pipermail/foundation/2017-June/002495.html).

## Interoperability Working Group Update

After the usual formalities of a roll call and approving [the previous
meeting
minutes](https://wiki.openstack.org/wiki/Governance/Foundation/7May2017BoardMinutes),
the board heard from Egle Sigler, Mark Voelker, and Chris Hoge of the
[Interoperability Working
Group](https://wiki.openstack.org/wiki/Governance/InteropWG).

The topics of the discussion are laid out in (the working group's
board
report)[https://docs.google.com/document/d/1Ftw2tHn9l3oOlBhYMRrdVWcRfyk9tqGaTkfX3FVHdfo]
with Egle covering the upcoming 2017.08 guideline, Mark covering the
proposal for extension programs, and Chris covering version 2.0 of the
interop schema.

The (extension programs proposal)[https://review.openstack.org/472785]
resulted in the most discussion. Mark described how the proposal
explains how the OpenStack Powered trademark programs work today, the
history of those programs, and how the additional programs would work.

The first type of program is a "vertical" program - examples given
include "OpenStack Powered for NFV" or "OpenStack Powered for
Containers". These would add requirements for additional capabilities
specific to these use cases, provided those capabilities are already
widely deployed in the context of those use cases.

The second type of program is an "add-on" program - for example,
"OpenStack Powered DNS". This would require capabilities specific to
that service, and ensure interoperability between implementations of a
given service. It is anticipated that individual project teams would
be responsible for definining the interop requirements.

Anni asked how these programs would relate to the idea of
"constellations" as a way of describing OpenStack components, but the
working group didn't see any immediate overlap with that idea.

I raised a concern that if obscure projects are free to define add-on
programs of their own, it could dilute the value of the OpenStack
Powered programs overall. However, it was clarified that, while the
individual project teams could define interop requirements, each
individual new program would require board approval.

Anni also raised a concern that vertical programs should not be
exclusive - i.e. it should be possible for a single product to qualify
for all vertical programs at once, so these programs need to not have
conflicting requirements. The working group agreed with this, and
explained that they had already taken this feedback into account.

Finally, the working group explained that their goal is for the board
to approve this framework at our Fall meeting.

## Membership Changes

The last topic for the board to consider was some membership changes
and applications. Put simply, Canonical wished to move from being a
Platinum member to being a Gold member, and Ericsson wished to apply
for Canonical's Platinum member slot.

Chris Price presented Ericsson's case for Platinum
membership. Interestingly, this was the second time that Ericsson had
applied for Platinum membership in the past year. The previous time,
at (the March 9 board
meeting)[https://crustyblaa.com/march-9-2017-openstack-foundation-board-meeting.html],
Ericsson and Huawei applied for the slot left vacant by HPE. Huawei
was successful with their application that time around.

Chris explained Ericsson's vision for OpenStack, and how they plan to
continue developing and driving forward the OpenStack ecosystem. He
also explained Ericsson's role in working with adjacent communities
like OpenDaylight and OPNFV, as well as their role in related
standard's bodies.

Next up, Mark Baker described how Canonical felt that with several
"industry giants" looking to take up Platinum membership, that the
right thing for a smaller entity like Canonical to do from a community
perspective, was to take a step back and allow others with greater
resources to take their Platinum member slot. However, he also
emphasized how OpenStack remains at the core of Canonical's business.

After some brief questions, the board went into executive session and,
on return, both applications were approved.

## Next Meeting

The board's next meeting is a 2 hour conference call on Tuesday,
August 22. Our next in-person meeting will be in Denver on Sunday,
September 10.
