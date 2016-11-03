Title: May 11 OpenStack Foundation Board Meeting
Date: 2014-05-17 14:52
Author: markmc
Tags: OpenStack, OpenStack Foundation Board Meeting
Slug: may-11-openstack-foundation-board-meeting
Status: published

The OpenStack Foundation Board of Directors [met
in-person](https://wiki.openstack.org/wiki/Governance/Foundation/11May2014BoardMeeting)
in advance of the OpenStack Summit in Atlanta. This my informal
recollection of the meeting. It’s not an official record, etc.

Unlike previous meetings held in advance of summits, this meeting only
ran from 09:00 to 14.30 at which time we switched venue for the [first
ever joint board of directors and technical committee
meeting](https://wiki.openstack.org/wiki/Governance/Foundation/11May2014JointMeeting).

I'm about to head off on vacation for a week, so I figured I'd do my
best to briefly cover some of the topics covered during the meeting.

### Jonathan's Update

After the usual preliminaries, we began the meeting with Jonathan Bryce
(in his role as Executive Director) giving the board an update from the
Foundation's perspective.

One of the more interesting slides in Jonathan's updates is always the
latest statistics showing community and ecosystem growth. We now have
over 355 companies supporting the foundation, over two thousand total
contributors and almost five hundred active contributors every month.
Over 17,000 commits were merged during the Icehouse release cycle, an
increase of 25% from Havana. This level growth is just phenomenal.

Jonathan also talked about the growth in visitors to the openstack.org
website and made some interesting observations about the geographical
spread of the visitors. The top 4 countries seen in the stats are the
U.S., India, China and France. That France figures so highly in the
stats is a good sign in advance of the summit in Paris in November.

Next, Jonathan moved on to talk about the week ahead in Atlanta. Once
again, we're seeing a huge increase in the level of interest in the
event with over 4,500 attendees compared to the roughly 3,000 attendees
in Hong Kong. Running an even of this size is a massive undertaking and
Jonathan mentioned one crazy statistic - the foundation had over 23,000
pieces printed for the event and had to spread those orders over three
printing companies in order to be able to do it.

A big emphasis for the week was an increased focus on users and
operators. And, interestingly, there were roughly 800 developers and 700
operators signed up for the event. All were agreed that it's a very
healthy sign to see so many operators attend.

One comment from Jonathan triggered some debate - that the event was
turning into a broader cloud industry event rather than strictly limited
to just OpenStack. Some board members raised a concern that the event
shouldn't become completely generic and the focus should always be on
OpenStack and its ecosystem. Jonathan clarified that this is the intent.

Jonathan also talked about the geographical diversity of attendees at
the summit. People were coming from over 55 countries, but 81% attendees
were from the U.S. In contrast, in Hong Kong, the percentage of US
attendees were more like 40% and Jonathan felt that this showed the
importance of regularly holding summits outside of the U.S.

### Finances

Jonathan also walked the board through and update on the foundation's
financial position. Operating income was 3% above their predictions and
expenses was down 7%. This has left the foundation with \$7.8M in the
bank, as part of Jonathan's goal to build up a substantial war-chest to
ensure the foundation's stability even in the event of unforseeable
events.

The summit in Atlanta was predicted to make a loss of \$50k but was on
track to make a profit. And yet, while it was predicted to be a \$2.7M
event, it was turning out to be a \$4M event. The situation will be very
different in Paris because of different cost structures and the event is
expected to make a loss. While on the topic, some board members
requested that the board be more closely involved in choosing the
location of future summits. Jonathan was happy to facilitate that and
expected to be able to give the board an update in July.

Jonathan next gave a detailed update on the foundation's application for
US federal tax exempt status. He explained that while we are Delaware
incorporated, non-stock, non-profit foundation we have not yet been
granted 501(c)(6) status by the IRS. After providing the IRS with
additional information in November, the IRS returned an initial denial
in March and the foundation filed a protest in April.

The objections from the IRS boil down to their feeling (a) that the
foundation is producing software and, as such, is "carrying on a normal
line of business", (b) that the foundation isn't improving conditions
for the entire industry and (c) that the foundation is performing
services for its members. Jonathan explained why the foundation feels
those objections aren't warranted and that the OpenStack foundation is
fundamentally no different from other similar 501(c)(6) organizations
like the Linux Foundation. He explained that other similar organizations
were going through similar difficulties and he feels it is incumbent on
the foundation to continue to challenge this in order to avoid a
precedent being set for other organizations in the future. Overall,
Jonathan seemed confident about our position while also feeling that the
outcome is hard to predict with complete certainty. This conversation
continued for some time and, because of the interest, the board moved to
establish a committee to track the issue consisting of the existing
members of the finance committee along with Eileen, Todd and Sean.

### Trademark Framework

Jonathan moved on to give an update on some changes the foundation have
made around the trademark programs in place for commercial uses of the
mark. The six logos previously used were causing too much confusion so
the foundation has merged these into "Powered By OpenStack" and
"OpenStack Compatible" marks.

There followed some debate and clarifications were given, before some
members expressed concern that the board had not been adequately
consulted on the change. That objection seemed unwarranted to me given
that Jonathan had briefed the board on the change in advance of
implementing it.

Staying on topic of trademark programs, Boris took the floor and gave an
update on the DriverLog work his team has been working on. He request
the board use the output of DriverLog to enforce quality standards for
the use of the OpenStack compatible mark in conjunction with Nova,
Neutron and Cinder drivers. There was rather heated debate on the
implications of this, particularly around whether drivers would be
required to be open-source and/or merged in trunk.

Several board members objected to the fact that this proposal wasn't on
the agenda and the board hadn't been provided with supporting materials
in advance of the meeting. Boris committed to providing said material to
the board before revisiting the issue.

### Defcore

Next up, Rob and Josh gave an update on the progress of their DefCore
initiative. Rather than attempt to repeat the background here, it's
probably best to [read Rob's own
words](http://robhirschfeld.com/category/clouds/openstack/defcore/).

Once the background was covered, the board spent some time considering
[the capabilities scoring
matrix](https://docs.google.com/spreadsheet/ccc?key=0Av62KoL8f9kAdFo4V1ZLUFM0OHlrRnFpQUkxSHJ5QWc&usp=drive_web#gid=6)
where each capability (concretely, capabilities are groups of Tempest
tests) is scored against 12 selection criteria. This allows the
capabilities to be ranked so that the board can make an objective
judgment on which capabilities should be considered "must have". There
appeared to be generally good consensus around the approach, but a
suggestion was made to consider more graduated scoring of the criteria
(e.g. 1-5 rather than 0 or 1).

The conversation moved on to the subject of "designated sections".
During the conversation, the example of Swift was used and Josh felt the
technical committee's feedback indicated that either Swift in its
entirety should be a designated section or that none of Swift would be
considered binary. Josh also felt that the technical community (either
the TC or PTLs) should be responsible for such decisions but I felt that
while the TC can provide input, trademark policy decisions must
ultimately be made by the board lest we taint the technical communities
technical decision making by requiring significant political and
business implications to be considered.

One element of clarity that emerged from the discussion was the simple
point that "must have" tests were intended to drive interoperability
while designated sections were intended to help build our community by
requiring vendors to ship/deploy certain parts of the codebase and, by
implication, contribute to those parts of the codebase.

As time ran short, the board voted to approve the selection criteria
used by the DefCore committee. A straw-poll was also held to get a feel
for whether board members saw the need for an "OpenStack compatible"
mark in addition to the "OpenStack powered" mark. All but three of the
board members (Monty, Todd and Josh) indicated their support for an
additional "OpenStack compatible" mark.

### Win The Enterprise

Briefly, Imad introduced the "Win the Enterprise" he an his team were
kicking off with a session during the summit. The goal is to drive
adoption of OpenStack in the enterprise by analyzing the technical and
business gaps that may be hindering such adoption and coming up with an
action plan to address them.

Feedback from board members was quite positive, with the discussion
centered around how the group would measure their success and how they
would ensure they operated in the most open and transparent way
possible.

There was also some discussion about the need for more product
management input to the project along with an additional focused effort
on end-users of OpenStack clouds.

### Wrapping Up

After the meeting drew to a close, board members joined members of the
technical committee for a joint meeting. I'm hoping one of the awesome
individuals on the technical committee will write a summary of that
meeting!

This was a hugely draining week for many of us at Red Hat. As I prepare
to completely switch off for a week, allow me to pass on [this sage
advise from Robyn
Bergeron](https://twitter.com/robynbergeron/status/466678776168865792):

[![Keep Calm and Ride The Drama
Llama](http://sd.keepcalm-o-matic.co.uk/i/keep-calm-and-ride-the-drama-llama.png)](http://www.keepcalm-o-matic.co.uk/p/keep-calm-and-ride-the-drama-llama/)
