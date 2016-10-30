Title: Oct 3rd OpenStack Foundation Board Meeting
Date: 2013-10-03 21:36
Author: markmc
Category: openstack, openstack-foundation-board-meeting
Slug: oct-3rd-openstack-foundation-board-meeting
Status: published

On Oct 3rd, the OpenStack Foundation Board held a two hour conference
call meeting which was open to anyone to join. [The agenda was published
in
advance.](https://wiki.openstack.org/wiki/Governance/Foundation/3Oct2013BoardMeeting)

As usual, this my informal recollection of the meeting. It’s not an
official record, etc. [Jonathan published an official summary on the
foundation mailing
list](http://lists.openstack.org/pipermail/foundation/2013-October/001481.html).

### Preliminaries

Our chairman, Alan Clark began the meeting by holding a roll call. If my
count was correct, we had 21 of the 24 members of the board on the call,
which is a pretty good turnout.

Alan introduced Chris Kemp as a replacement for Devin Carlen who had
been representing Nebula and the Gold Members. Chris briefly explained
that changes in his role at Nebula has left him more time for "strategic
stuff" and is delighted to spend more time with the OpenStack community
and join the board. He thanked everyone for their work in progressing
the foundation to date.

Before getting down to business, we quickly voted to approve [the
minutes of the previous
meeting](https://wiki.openstack.org/wiki/Governance/Foundation/6Aug2013BoardMeeting).

### Executive Director Report

Jonathan Bryce took the floor and gave a really excellent update on the
Foundation's progress.

First off, he described the launch of the [OpenStack Foundation Training
Marketplace](http://www.openstack.org/marketplace/training/) at LinuxCon
in New Orleans. The site now has 12 companies listing training events at
over 30 cities around the world and has seen over 10,000 unique visitors
over the past 2 weeks. He reiterated how one of the Foundation's stated
priorities for this year is to help training providers get the word out
on their education programs and thereby expand the pool of people with
OpenStack skills.

Next up, Jonathan gave an update on preparations for the [OpenStack
Summit in Hong
Kong](http://www.openstack.org/summit/openstack-summit-hong-kong-2013/).
Everything is coming together nicely and the finalized speaking agenda
has now been posted. He explained that, while they had received some 250
submissions for the summit in Portland, there were over 600 submissions
for Hong Kong and yet not many extra speaking slots. The track chairs
had a tough job whittling down the submissions but he thinks the end
result is an agenda packed with great sessions. Jonathan warned that,
unlike previous summits, we have a hard limit on the number of attendees
and the "full access" passes will sell out in the next week or so.

Eileen asked exactly how many full access passes were issued and
Jonathan explained there are 2,000 but that there are many more passes
for the general sessions and expo hall. Joseph asked for some insight
into the demographics of the registered attendees and how it compares to
previous summits. Jonathan felt that we would see a large number of
attendees from the region and that, while some companies may have
reduced their numbers travelling from further afield, there would still
be plenty of representation from all of the companies we are used to
seeing at summits.

The discussion then moved on to looking ahead to 2014 and a sneak peak
of next year's budget. Jonathan explained how 2013 was a great year
financially - particularly because the summits were larger than expected
- and the Foundation goes into 2014 with a healthy budget surplus of
over \$1M. We expect to continue to see large summits and this will lead
to increased revenues and expenses. Jonathan expects the Foundation to
continue to invest in technology and infrastructure over 2014. He
described the Foundation funded projects in 2013 to improve the member
database and tie it to the contributor agree process and an improved
system for handling summit speaker submissions.

Rob Hirschfeld asked whether the Foundation had budgeted for
certification testing infrastructure being proposed as part of the "what
is core" discussion. Josh felt this it not be necessary for the
Foundation to fund this, and there was a brief data tracking and
authentication systems.

Jonathan continued by describing the rapid growth in Foundation staff
during 2013, but that he expects ongoing staffing costs to have mostly
levelled off for 2014. He went on to talk about how he sees the role of
the Foundation over the next year to be around connecting different
parts of the community, helping to gather data on users and deployments
and sharing information with the world about new features in each
release.

One Jonathan had finished, Lew Tucker congratulated Jonathan on the
progress and asked whether a written summary could be prepared for board
members so that we could help get the word out. Josh pointed out that we
were soon due an annual report which would contain much of this
information.

Josh then asked a question about the project budget for gold member fees
and how many new members this assumed would be added in 2014. There was
some confusion on the issue because gold member fees are based on the
member's revenue, but the conclusion was that the addition of 4 new
members was projected. This would bring the total number of gold members
up to 20 out of a total possible 24 members.

### Election Committee Report

Next up, Todd Moore delivered an excellent summary of the discussions
and conclusions of the committee established to consider whether any
changes were need for the individual and gold member director election
systems and what those changes might be.

Todd's report - which will be published in full soon - described how we
considered three separate questions. Firstly, whether and how concerns
about the fairness of the individual member director election system
(particularly the issue of large blocks of affiliated voters) should be
addressed, secondly whether we should consider any rule changes around
foundation employees eligibility for the individual member director
election and, finally, whether the eligibility rules for the 2013 gold
member director elections had been properly enforced.

The last topic was easily dispensed with - Todd and the committee worked
with the foundation staff to verify that all eligibility rules (i.e.
eligibility as a candidate and eligibility to vote) had been properly
enforced.

The first topic proved to be substantially more contentious. The pros
and cons of changing to an STV based election system or tweaking the
rules of the current system to halve (from 8 to 4) the number of votes
which you could allocate to a single candidate were explained in great
detail. Todd explained how the committee felt that changes were not
necessarily warranted but that it would be wise to seriously consider
the option of the "max 4 votes per candidate" tweak.

A motion was proposed to not fundamentally change the voting system and
was almost voted for until it became apparent that Monty wanted to speak
but was unable to come off mute. Once that was sorted out, Monty stated
that the cumulative system was utterly broken and that block voting did,
in fact, influence the outcome of the election. He felt strongly that a
change to STV was needed. The debate then took off in earnest with many
well put points made by various members. I explained how I agreed fully
with Monty but that I was convinced by the "it's working reasonably
well; this doesn't warrant a the disruption of a bylaws change" but that
we needed to be alert to any renewed concern from members after the next
election. In the end the vote was passed with no abstentions and Monty
voting against.

The discussion then moved on to the question of the "only 4 votes per
candidate" tweak. Much of the discussion hinged on whether this tweak
required a bylaws change. The election committee and Jonathan felt that
it was compatible with the "cumulative voting system" language in in
[section 3.9a of the
bylaws](https://wiki.openstack.org/wiki/Governance/Foundation/Bylaws#ARTICLE_III._MEMBERSHIP_MEETINGS)
but legal counsel for the foundation (Mark Radcliffe) disagreed strongly
and felt "cumulative voting" was "binary in the eyes of the law". Since
the committee had suggested this tweak on the understanding that it was
easy to implement, the idea was dropped.

Next, we discussed the second issue - the question of foundation
employees on the board. The committee did not have a consensus
recommendation on this but Todd did summarize the different viewpoints
and arguments. One approach proposed that the executive director would
be granted a new, automatic seat on the board and (because there is a
limit of two members per organization), only one additional foundation
employee could be elected to the board rather than the current limit of
two employees. There was lots of debate and I felt Jonathan's input was
particularly interesting - that he did not see the need for an automatic
executive director seat and he had reservations about restricting
employees from being directors since they could bring invaluable and
passionate input, should the electorate choose to elect them. In the
end, it was felt there was not sufficient cause to warrant a disruptive
bylaws change and the motion was withdrawn.

So, in summary, there will be no election system changes proposed to the
electorate during this cycle. However, the board again re-stated the
importance that all members adhere to the [community code of
conduct](http://www.openstack.org/legal/community-code-of-conduct/)
which states:

> Respect the election process. Members should not attempt to manipulate
> election results. Open debate is welcome, but vote trading, ballot
> stuffing and other forms of abuse are not acceptable.

Finally, the committee took an action item from the board to analyze the
results of the next election and provide the board with a report on the
potential effect of any of the options proposed.

### Wrapping Up

Because of the lengthy debate on the election system, we had run out of
time and the rest of the agenda had to be postponed until the [in person
board meeting in Hong
Kong](https://wiki.openstack.org/wiki/Governance/Foundation/4Nov2013BoardMeeting).

### Edits

-   Changed from "legal counsel for the board" to "legal counsel for
    the foundation". Thanks to Richard Fontana for the correction.
-   Included a reference to the code of comment. Thanks to Rob Esker for
    his question.

