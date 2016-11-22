Title: November 17th OpenStack Foundation Board Meeting
Date: 2016-11-21 09:00
Author: markmc
Tags: OpenStack, OpenStack Foundation Board Meeting
Slug: november-17-openstack-foundation-board-meeting
Status: published

I had [previously posted summaries of most board
meetings](https://crustyblaa.com/tag/openstack-foundation-board-meeting.html),
but had stopped doing this when I was appointed as Red Hat's
representative on the board. Lately, I've sensed folks at Red Hat
becoming more interested in the workings of the Foundation, so I
figured it might be useful to start doing this again.

The [OpenStack Foundation Board of
Directors](https://www.openstack.org/foundation/board-of-directors/)
met for a two hour conference call last week. The usual disclaimer
applies - this my informal recollection of the meeting. It’s not an
official record.

### Gold Member Applications

The first half of the meeting was given over to an Executive Session,
after which the board voted to [approve China Telecom, Inspur, and ZTE
as Gold
Members](http://www.openstack.org/news/view/284/investment-in-openstack-accelerates-as-foundation-welcomes-china-telecom-inspur-and-zte-as-gold-members)
of the Foundation.

This completes the handling of the 7 Gold Member applications that
were presented to the board at the [October 24
meeting](https://wiki.openstack.org/wiki/Governance/Foundation/24Oct2016BoardMeeting)
in Barcelona. 99Cloud, China Mobile, City Networks, and Deutsche
Telecom were approved at that meeting.

For the first time, the Foundation now has reached the maximum of [24
Gold Members](https://www.openstack.org/foundation/companies). We will
only be able to consider applications for new Gold Members if an
existing member departs, or if we go through a difficult process to
change the limit in [our
bylaws](http://www.openstack.org/legal/bylaws-of-the-openstack-foundation/).

### User Committee Proposal

Next up, Edgar Magana updated the board on some [proposed changes to
the User
Committee](https://docs.google.com/document/d/1QmLOeseAkjBWM_TXsUeKBErNaSHnuZp81II0T71ARfo)
that was first discussed at the October meeting.

Currently the bylaws describe the User Committee is an "advisory
committee" of three members appointed by the Board and TC, which
prepares regular reports for the Board and TC. The idea with this
proposal is to make the User Committee a parallel entity to the TC,
with its members chosen through an election of Active User
Contributors (AUC).

The bylaws changes outline how the User Committee has at least five
members, that elections of Active User Contributors (AUCs) are held
every six months, an affiliation limit for members of the UC, how AUC
status is determined, and more.

The hope is that feedback will be collected as comments in the
[proposal
document](https://docs.google.com/document/d/1QmLOeseAkjBWM_TXsUeKBErNaSHnuZp81II0T71ARfo)
and that the Board will vote on the proposal during our December 6
meeting. A vote of the Board is sufficient to enact the changes.

One point of discussion was whether bylaws changes are necessary at
all. The hope when the bylaws were originally drafted was that the
User Committee would have plenty of lattitude to evolve via changes to
[the UC
charter](http://www.openstack.org/legal/bylaws-of-the-openstack-foundation/). Edgar
made the point that the key change is for the UC to become a parallel
entity to the TC rather than an advisory committee to the Board and
TC.

### "Futures" Discussion

Next, Toby Ford gave a presentation on a topic he had proposed along
with Imad Sousou, Allison Randal, and Mark Baker. Toby introduced the
topic by saying that as any project evolves and matures, it is
important to reflect on competitive threats and the need to evolve the
project.

Toby talked about a wide set of competitive threats to OpenStack from
the container ecosystem (including Kubernetes and Mesos), to other
storage implementations, to various projects in the Telco world
([OpenVIM](https://github.com/nfvlabs/openvim),
[E2](https://blog.acolyer.org/2016/06/17/e2-a-framework-for-nfv-applications/),
[3GPPP](http://www.3gpp.org/)), and the obvious challenge of AWS,
Azure, and Google with AWS revenue over $10B.

Toby moved on to talk about "the good and the bad of the Big Tent",
describing the need for a balance between diversity and innovation
versus consolidation and refactoring. Toby made the case that we're
seeing a lot of expansion in the Big Tent, but not consolidation and
refactoring. He expressed particular concern about how and whether
core projects will be able to evolve, especially if the Big Tent does
not allow for competitors to existing projects.

Toby then put on his "AT&T hat" and talked about the challenges for
OpenStack from an AT&T perspective - the need to get to a control
plane that scales to 10k servers, the problem of managing over 100
different production sites, the challenge of more and more happening
"at the edge" with 5G, innovation happening in the networking space
and how it relates to OpenStack, and the unsolved problem of keeping a
production environment current with latest OpenStack releases.

To wrap up his presentation, Toby listed a few "possible
recommendations" the Board could make to the technical community - (1)
allow core projects to have competition within the Big Tent, (2) a
mechanism to incubate new approaches, and (3) a mechanism to
reationalize, clean up, or refactor.

What followed was a pretty lively discussion that covered much ground,
over and beyond the concerns raised by Toby. While the success of
OpenStack in bringing together such a diverse set of interests was
acknowledged, there was a definite frustration that some form of
necessary change is failing to emerge naturally, and whether it falls
on the Board to try to at least try to clearly articulate the problem
at a strategic level.

Jonathan tried to focus the conversation by giving his perspective
that the Big Tent concerns had tied down until "recent comments in the
media", and that is probably a distraction from the concerns people
are expressing about core projects like Nova and Neutron. He was at
pains to say that this isn't about project teams doing bad work - we
continue to make huge progress in each release, and valuable work is
being done. However, we're definitely seeing frustration from some
quarters that it is difficult to influence the community with their
ideas.

Jonathan warned that talking too much in the abstract creates the risk
that the discussion will go around in circles. Despite this, the
discussion never did go into any particular detail on where we've
witnessed the problems we were discussing. From my own perspective, it
was clear that much of frustration was as a result of how the
[Ciao](https://clearlinux.org/ciao) and
[Gluon](https://wiki.openstack.org/wiki/Gluon) projects have been
received, but we're failing to learn anything significant from those
experiences by not talking about them in detail.

By the end of the discussion, we had agree to collaborate on a
concrete description of specific problem areas, the questions they
raise, and some possible solutions. The hope is that we would complete
this before our December meeting, and we may then plan a longer
meeting (possibly face-to-face, possibly with the TC) to dig into
this.
