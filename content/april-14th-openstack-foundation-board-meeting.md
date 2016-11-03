Title: April 14th OpenStack Foundation Board Meeting
Date: 2013-05-25 14:44
Author: markmc
Tags: OpenStack, OpenStack Foundation Board Meeting
Slug: april-14th-openstack-foundation-board-meeting
Status: published

On April 14, the day before the OpenStack Summit in Portland began, the
OpenStack Foundation Board held an all-day, in-person meeting. Like all
of our board meetings, the
[agenda](https://wiki.openstack.org/wiki/Governance/Foundation/14Apr2013BoardMeeting)
was packed solid.

After our meetings, the goal is for Jonathan to post a summary to the
mailing list (like [this
one](http://lists.openstack.org/pipermail/foundation/2013-February/001364.html))
and I try and follow up with a longer blog post with a bit more
commentary. For a bunch of reasons, we've let things slide this time,
but here's my attempt at a summary anyway. It's been a while since the
meeting, so a lot of the details are pretty vague at this point.

One thing I really liked about the meeting was that we had chairs set up
so that anyone who wished to attend the meeting and listen were welcome
to do so. With so many stackers already in town for the summit, it
really was a great opportunity to open the workings of the board to
anyone interested.

### Transparency Committee

The first meaty item on the agenda was an update from Joshua McKenty on
the progress of the board's [Transparency
Committee](http://lists.openstack.org/pipermail/foundation/2013-February/001362.html).

We began by discussing Nick Barcet's efforts to choose and implement a
document management system for the board. OwnCloud, Google Drive,
Dropbox and github have all been considered. Google Drive and Dropbox
would not be accessible by all board members. It was noted that the
Foundation staff will also require a document management system and we
might be able to use the same system for both use cases. Conclusion was
for Nick and Monty to see if the OpenStack Infrastructure team could
host OwnCloud for this purpose.

Next we discussed the transparency policy which Lauren Sell and Mark
Radcliffe have been working on. The core concern is how to balance the
need for having a culture of transparency and openness with the need for
some information (like legal or personnel matters) to be kept
confidential. The general approach discussed was having the board's
mailing list open, but confidential information would be shared via
private documents in a document management system that could be referred
to in mailing list posts. The distinction between confidential and
embargoed information was discussed and it was agreed that embargoed
information should have a disclosure date associated with it.

There was also a brief discussion on the possibility of having a
transparency ombudsman. This would be a person trusted by the community
with whom complaints related to transparency could be raised. It was
felt this could be a duty of a foundation employee, if that individual
had already established the reputation for trustworthiness and
independence required.

### 2013 Individual Director Elections

Next up, Rob Hirschfeld led a discussion on possible changes to the
election process in time for the 2013 Individual Director elections.

We began by discussing how we would go about making any required changes
to [the
bylaws](https://wiki.openstack.org/wiki/Governance/Foundation/Bylaws).
It was recognized that we would need a firm proposal to be made to the
board in August so that notice could be given in September of a vote in
October in time for the elections in November.

It was also noted that a bylaws change would require a majority vote of
the individual members with a voter turnout of 25%. For reference, we
had a 28% turnout at the [previous
election](https://www.bigpulse.com/pollresults?code=2888d7aPUFe5Euveb5kiYNGT).

We also briefly discussed [the potential
objectives](https://etherpad.openstack.org/2013-Individual-Elections)
for any changes to the elections process but avoided going deep on this
because of the limited time available on the agenda.

### Legal Affairs Committee

Next on the agenda was a discussion (led by me) about the Legal Affairs
Committee.

The main concern I raise was the project (or the "Technical Community
and Committee", as I called it) needed the support of subject matter
experts when dealing with the kind of legal issues regularly encountered
by all open-source projects, particularly in the area of copyright and
licensing. I proposed Richard Fontana's idea that, rather than depending
exclusively on the Legal Affairs Committee or the Foundation's legal
counsel for help with such matters, we would create a legal-discuss
mailing list where any subject matter experts could contribute to
resolving issues raise by the technical community. The idea was that we
would also have a FAQ wiki page to document any conclusions reache on
the list. There was some discussion about whether opinions expressed on
the list could be construed as legal advice and it was agreed to put in
place disclaimers to avoid that perception.

(For the record, we've since created [the legal-discuss mailing
list](http://lists.openstack.org/cgi-bin/mailman/listinfo/legal-discuss)
and [the legal issues
FAQ](https://wiki.openstack.org/wiki/LegalIssuesFAQ).)

We also discussed whether the description of scope of the Legal Affairs
Committee in the bylaws could be improved and whether the strict five
member limit in the bylaws was really such a good idea. It was agreed
that I would work with Alice King to see if we can address those issues.

(Again for the record, Alice and I had a productive discussion and we
put together [the Legal Affairs Committee wiki
page](https://wiki.openstack.org/wiki/Governance/Foundation/LegalAffairsCommittee)
to at least ensure the committee's scope, membership and progress could
be properly documented.)

### Gold Member Applications

Next up, we had presentations from
[Juniper](https://wiki.openstack.org/w/images/4/4a/JuniperGoldApplication.pdf)
and
[Ericsson](https://wiki.openstack.org/w/images/9/94/Ericsson_application_openstack.pdf)
on their applications for Gold Membership. Once the presentations had
been completed, we convened an executive session to discuss the
applications in private.

During the executive session, the board reviewed each application using
the
\[https://wiki.openstack.org/wiki/Governance/Foundation/PotentialMemberCriteria
previously agreed criteria\].

Once the executive session was completed, the board reconvened the
meeting and carried out the official, public vote on the new member
applications. The applications of both Ericsson and Juniper were
approved.

As part of the voting process, some directors chose to publicly restate
their concerns with the applications that had been discussed during the
executive session. One concern raised by Rob Hirschfeld and Joshua
McKenty was that, while both applicants shared their plans for
increasing their OpenStack engagement, it could be argued that future
plans aren't the same as the "demonstrated commitment" talked about in
the membership criteria.

Another concern discussed at length was that applicants could provide
much more in the way of written detail about how they meet the
membership criteria. One take on this was that applicants should be
expected to provide a resume of their involvement with, and commitment,
to OpenStack. Simon Anderson proposed that we form a membership
committee which would mentor applicants and advise them on how to
prepare their application.

In total, discussion of these applications and the process for new gold
members took up 4 hours of the board's time. While this may seem
excessive, it was very apparent that everyone on the board was keen for
the Foundation to have gold members that would help drive OpenStack's
success. With the addition of Ericsson and Juniper, we now have 16 of
the 24 gold member slots filled. As the number of remaining slots
shrink, I think we will see the board having higher expectations of
applications.

### Programs

At this point, the board seemed collectively quite drained of energy and
the agenda had to be significantly reworked because there wasn't much
time remaining.

Monty took the opportunity to briefly discuss an idea he had to
introduce the concept of "programs" in addition to our current concept
of projects. We would use this to recognize efforts like documentation
and CI on equal footing with the integrated projects. Other efforts like
Oslo, TripleO and puppet recipes were also mentioned as potential
programs.

Rather than go into too detailed discussion on the topic, we generally
expressed support for the concept but agreed it needed further
discussion.

### Joint Session

Part of the agenda for the meeting was that members of the Technical
Committee were invited to join the meeting for a joint session. Monty
and I were obviously already present, but Michael Still and Thierry
Carrez also joined. Other TC members had not yet arrived in Portland or
weren't fully aware of the joint session. We had some discussion about
how to have a joint session with better attendance from both groups and
the idea of a joint design summit session at the next summit was mooted.

### User Committee

Tim Bell stepped up next to give an overview of the results of the User
Committee's recently completed survey of OpenStack users.

Tim is presenting these exciting results at the summit, so I won't
repeat them here. However, we did have an interesting discussion about
how representative the survey was of OpenStack deployments. Tim offered
50-75% as his gut feeling for the percentage of deployments covered but
Joshua McKenty reckoned it was probably less than 25%. There was some
discussion about future surveys and the potential for an opt-in usage
stats tracking tool to increase the percentage of deployments we know
about.

### Incubation Update Committee

Next up, Alan Clark presented the [final report of the Incubation Update
Committee](https://wiki.openstack.org/wiki/Governance/Foundation/IncubationUpdate2013).

The board was generally very supportive of the work of the committee,
but it was clear further discussion was required on the topic of Core
status and the board's trademark usage program. Much discussion was had
around the desire for projects like Heat and Ceilometer to be able to
adopt official OpenStack project names (like "OpenStack Measurement" for
Ceilometer) and whether this was all that would be implied by Core
status. However, there is also the question of whether clouds which wish
to use the OpenStack brand should be required to use all Core projects
or whether a trademark program around more targeted interoperability
testing made more sense.

It was agreed that this was an incredibly important and urgent topic but
that we had run out of time at this meeting to make progress on it.
