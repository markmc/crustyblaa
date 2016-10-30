Title: June 27th OpenStack Foundation Board Meeting
Date: 2013-06-29 16:04
Author: markmc
Category: openstack, openstack-foundation-board-meeting
Slug: june-27th-openstack-foundation-board-meeting
Status: published

On June 27, the OpenStack Foundation Board of Directors met for two
hours via conference call. As usual, the [agenda was published in
advance](https://wiki.openstack.org/wiki/Governance/Foundation/27June2013BoardMeeting)
and the meeting was open to anyone who wanted to observe the
proceedings.

These notes are my perspective of the meeting. Jonathan Bryce [published
an official
summary](http://lists.openstack.org/pipermail/foundation/2013-June/001435.html)
and official minutes will be posted in due course.

### Roll Call and Meeting Confidentiality Policy

As you can imagine, a conference call with 20-30 attendees takes a while
to get going. We began with a roll call and, after perhaps 15 minutes,
were ready to get started.

First item on the agenda was a review of our meeting confidentiality
policy. Directors agree to refrain from commenting on the meeting
proceedings until Jonathan posts his summary. The only official record
of the meeting is Jonathan's summary and the official minutes. Anything
discussed during executive session is confidential. Nothing new here.

### Amendment to our Certificate of Incorporation

Next up was a motion to approve a relatively minor amendment to the
foundation's certificate of incorporation.

The details of the amendment is fairly obscure, but essentially the
Foundation is applying for [U.S. 501(c)
status](https://en.wikipedia.org/wiki/501%28c%29_organization) which
means it will be a tax-exempt, non-profit organization. There are
various different organization types, but the  
two most relevant are 501(c)(3) and 501(c)(6). OpenStack is filing for
501(c)(6) status.

Jonathan explained that, while preparing for this filing, it was noted
that the original certificate of incorporation only allows (on winding
up of the foundation) the foundation's assets to be transferred to a
501(c)(3) organization. This amendment simply allows for the possibility
of transferring assets to 501(c)(6) organizations.

There was some brief discussion clarifying exactly which status we were
filing for and the motion was passed unanimously.

### Transparency Policy

Next up, Lauren Sell explained the context for a formal transparency
policy document which had been circulated to the board members and would
require further discussion before being approved.

Lauren reminded us that at our meeting in April, the Transparency
Working Group presented the principles for a transparency policy. Lauren
had since worked with legal counsel to draft a more formal policy based
on those original principles.

The main question Lauren felt needed to be cleared up was the issue of
document management. The board has (and will continue to have) documents
which must remain confidential. At our April meeting we had agreed that
the OpenStack Infrastructure team would investigate hosting an OwnCloud
instance which would act as our document store. While this was still on
the team's to-do list, it had not been prioritized over other work.

I suggested that, in the team time, we create a new mailing list for the
the board (e.g. foundation-directors?) which would be open to everyone
for read-only subscription and we would use the current mailing list to
share confidential documents. Once the document management system is in
place, we could then shut down the private foundation-board mailing
list.

Rather than discuss in any great detail, it was agreed the Lauren would
start a discussion on the foundation mailing list.

### Summits & Marketing

Next up, Mark Collier and Lauren gave us an update on the Marketing
front and how summit planning is progressing.

Lauren first talked through some excellent slides with a tonne of
details about the Icehouse Design Summit in Hong Kong from Nov 5-8,
2013. This is the first time that the summit will be held at an
"international venue" (an amusing term if you're not U.S. based :) and
we again expect record attendance.

Included in Lauren's slides were some really helpful maps and aerial
shots showing the venue, the geography of Hong Kong and the location of
the recommended hotels. The venue is located near the airport which is a
25 minute train journey from down town Hong Kong. There are a couple of
hotels adjacent to the venue and most of the other recommended hotels
are down town. The foundation staff have worked hard to come up with a
good range of hotel options, including hotels with a rate of under \$150
per night.

In terms of travel advice, it was noted that visitors must have a
passport valid for at least one month after their planned stay and that
flights from SFO to HKG are currently averaging between \$1000 and
\$1400. Jonathan recommends that people book their flights early,
because fares will increase very significantly closer to the event.
Lauren also pointed out that it's sensible to make hotel books now,
since the hotels closest to the venue are already selling out.

Lauren then talked through the planned format for the summit, which has
been heavily influenced by feedback received through the [survey results
from the previous
summit](http://www.openstack.org/blog/2013/06/openstack-summit-survey-results/).

This time around there will be two types of passes. A more affordable
limited access pass will give access to the expo hall, general sessions
and a single track of breakout sessions on Tuesday and Wednesday. The
hope is that this will help control the numbers at the breakout
sessions, but also make the event more accessible to folks who just want
to come along for the first time and learn about OpenStack.

The primary language of the event will be English, but there will be
simultaneous translation into Mandarin in the main hall.

The call for sponsors is already open and we have 21 sponsors to date.
The headline sponsorship sold out in an astonishing 7 minutes.

For the first time, there will be a travel support program designed to
ensure that lack funding won't prevent key technical contributors from
attending the event. Details of this will be announced very soon. We had
a brief discussion about how this program should be run and it was
pointed out that we could learn from similar programs for PyCon and UDS.

In terms of learnings from the previous summit, some of the things the
team will be working hard to improve is the quality of network
connectivity, the size breakout rooms and the variety of beverages and
snacks.

It was noted that feedback from ATCs who completed the survey was 2.5:1
in favour of keeping the design summit collocated with the conference.
In Hong Kong, the design summit rooms will be well separate from the
breakout session rooms, ATC status will be properly indicated on name
badges and it will be much more clear on the schedule which sessions are
part of the design summit and which are breakout sessions.

After some interesting discussion about the plans for Hong Kong, Lauren
gave a brief overview of how plans are proceeding for the 2014 summits.
The spring summit is planned for the week of May 14 with Atlanta and
Chicago under consideration. The autumn/fall summit will be one of the
first two weeks of November with Paris and Berlin currently under
consideration. Decisions on the venues for both these summits are
expected to be made soon.

Finally, Lauren ran through some updates on the progress of the
[marketing
community](http://wiki.openstack.org/Governance/Foundation/Marketing)
more generally. Version 1 of the OpenStack [marketing
portal](http://www.openstack.org/marketing) has been made available. The
[mailing
list](http://lists.openstack.org/cgi-bin/mailman/listinfo/marketing) is
gaining new subscribers all the time. The monthly meetings are also
seeing growing numbers attending.

### Patent Cooperation Proposal

Next on the agenda was a presentation from several members of the [Legal
Affairs
Committee](https://wiki.openstack.org/wiki/Governance/Foundation/LegalAffairsCommittee)
on the three options they recommend the foundation should consider for
increased cooperation on patent sharing or cross-licensing between
foundation members.

Frankly, I don't really have the energy to try and summarise these
proposals in great detail, so this is short ... however, this is
certainly a complex and important topic.

The Apache License v2.0 has a patent provision which means you grant a
license to any of your patents which are infringed upon by any
contributions you make. If any licensee of the software claims that the
software infringes on their patent, then they lose any patent rights
granted to them under the license.

Two options were presented to the board for how we might encourage
further sharing of patents related to OpenStack between the companies
involved. The idea is that we could put OpenStack in a better defensive
position by sharing a wider range of applicable patents.

The first option proposed was to closely copy [Google's Open Patent
Non-Assertion Pledge](http://www.google.com/patents/opnpledge/pledge/).
The idea is that companies involved in OpenStack would pledge to not
assert specific sets of relevant patents against OpenStack users.

The alternative option proposed was the adoption of an [OIN-style patent
cross-licensing
scheme](http://www.openinventionnetwork.com/patents.php). The primary
difference of this scheme is that an actual patent license is granted to
users, rather than just a non-assertion pledge.

The slides outlining these options will be posed to the foundation wiki
page. It is hoped the board will be in a position to come to a decision
on this in November.

### Closing Topics

Alice King is stepping down from her role on the Legal Affairs
Committee, so the board voted to approve a motion to appoint Van
Lindberg to the committee.

Rob Hirschfeld gave an update on his work to bring about a productive
discussion on the question of "what is core?". Rob has held a couple of
meetings with other board members and drafted six position statements
which he hopes will drive the discussion towards a consensus-based
decision. Rob wishes the board to come to a good level of consensus on
these position statements before opening the discussion up to the rest
of the community.

Finally, there was a brief discussion about training and how members of
the User Committee are actively working on training materials.
