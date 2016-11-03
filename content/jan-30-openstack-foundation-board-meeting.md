Title: Jan 30 OpenStack Foundation Board Meeting
Date: 2014-02-07 16:41
Author: markmc
Tags: OpenStack, OpenStack Foundation Board Meeting
Slug: jan-30-openstack-foundation-board-meeting
Status: published

The [OpenStack Foundation Board of
Directors](https://www.openstack.org/foundation/board-of-directors/) met
for a two hour conference call last week. This was the first meeting of
the board since the recent
[Individual](http://lists.openstack.org/pipermail/foundation/2014-January/001616.html)
and
[Gold](http://lists.openstack.org/pipermail/foundation/2014-January/001615.html)
member director elections.

As usual, this my informal recollection of the meeting. It’s not an
official record, etc.

Your trusty reporter had just arrived in Brussels for FOSDEM and got to
stay in his hotel room for this meeting rather than sampling Belgian's
fine beers. Oh, the sacrifices we make! :-P

### Preliminaries

As usual, calling the meeting to order was a challenge and it was at
least 15 minutes after the scheduled start before we completed the roll
call.

Next, Alan welcomed our new directors:

-   Yujie Du
-   Alex Freedland
-   Vish Ishaya
-   Imad Sousou

and thanked our outgoing directors:

-   Nick Barcet
-   Hui Cheng
-   Joseph George
-   Lauren Sell

as well as thanking those directors who served on the board for part of
2013:

-   Devin Carlen
-   Jim Curry
-   John Igoe
-   Kyle MacDonald
-   Jon Mittelhauser

### Policies, Communication Channels and Meetings Schedule

Since it's a new year, we took the opportunity to review the various
policies which apply to board members.

Josh went over our [transparency
policy](http://www.openstack.org/legal/transparency-policy/) mentioning
that the board endeavours to be as transparent as possible, with board
meetings open to the public, a summary of meetings posted to the
foundation list and directors encouraged to use the foundation mailing
list for discussions. Sub-committees of the board are expected to be
similarly transparent, with wiki pages and public mailing lists. Some
caveats to this policy are that board members are not allowed to make
public comments about the board meeting until after Jonathan has posted
his summary (or 72 hours have passed), members should not discuss
executive sessions and the distribution of some non-public documents may
have to be limited to directors.

Alan also mentioned our [Code of
Conduct](https://wiki.openstack.org/wiki/Governance/Foundation/CodeOfConduct)
and encouraged directors to read it carefully. Finally, Jeff from DLA
Piper walked us through our [antitrust
policy](https://wiki.openstack.org/wiki/Governance/Foundation/AntitrustPolicy)
where he emphasised the importance of avoiding even the perception that
board members are coming together to advance the interests of some
companies over others. Members should restrict themselves to
pro-competitive collaboration.

Next, we quickly reviewed the various channels for communication that
directors need to be aware of - webex for conf calls, the foundation and
foundation-board mailing lists, the \#openstack-board and
\#openstack-foundation IRC channels, informal etherpads that we use
during board meetings and the various committee mailing lists.

Finally, we discussed the upcoming board meetings - an all-day
face-to-face meeting in Palo Alto on March 4, a 2 hour conference call
on April 3, an all-day face-to-face meeting in Atlanta on May 11 in
advance of the Atlanta summit and another face-to-face on July 21 at
OSCON.

The subject of the timing of the Atlanta face-to-face was raised again.
May 11 is also Mother's Day (in the US and some other countries) which
is a nasty conflict for many board members. However, a poll amongst
board members had already established that no better time around the
summit could be found, so we are proceeding with the meeting on May 11.
The question was raised about whether future board meetings should be
scheduled to not align with our summits, but the objection to this idea
was that it puts too much of a time and budget strain on those members
who have to travel a long distance for the meetings.

### Status Reports From Committees

Finally, time to move on to some more meaty topics! A member of each
committee of the board was asked to provide a status update and plans
for the year ahead.

Alan first described the work of the [compensation
committee](https://wiki.openstack.org/wiki/Governance/CompensationCommittee)
who are responsible for defining and evaluating the goals and
performance of the Executive Director. In summary, the committee
concluded that Jonathan met his 2013 goals and new goals have been set
for 2014.

Next up, Sean Roberts talked about the finance committee. This committee
works with the foundation staff on financial budgeting and accounting.
Sean described the foundation's IRS filing and that the foundation's
2012 financial audit has been completed and deemed clean (with a note
that the foundation is "operating on a cash basis"). The foundation's
application for 501(c)(6) is progressing with the IRS asking for some
clarifications which were returned to them in December. The committee
meets monthly to review any discrepancies above 10%, but there have been
no such issues so far. Essentially, everything is in excellent shape.

Tim Bell talked through the latest from the [user
committee](https://wiki.openstack.org/wiki/Governance/Foundation/UserCommittee).
Tim mentioned the user survey that was published at the Hong Kong summit
and how the committee has asked the TC for input on the kind of feedback
that would be useful for developers. The committee is preparing to run
another survey in advance of the Atlanta summit. Tim also mentioned that
the user committee is running a couple of small, focused "operator
mini-summits" over the next few months to bring operators together to
share their feedback. Tim described the challenge running the committee
with a small number of core volunteer members so as to ensure the
privacy of survey results while also encouraging volunteers to help with
tasks like turning survey feedback into blueprints for new features.

Van Lindberg gave an update on the [legal affairs
committee](https://wiki.openstack.org/wiki/Governance/Foundation/LegalAffairsCommittee).
He emphasised that the committee is not counsel for the foundation or
the board, but rather a group which makes recommendations to the board
on IP policy. He recapped on some of the patent policy recommendations
from last year, for example that the foundation should join OIN. There
was a brief mention of the fact that all the committee members are
currently lawyers and the by-laws limits the number of members to five.
He also mentioned that the DefCore committee has a related sub-committee
examining possible by-laws changes.

Todd described the [elections
committee](https://wiki.openstack.org/wiki/Governance/Foundation/ElectionsCommittee),
that is was formed in February 2013 with 8 members and the goal to
consider possible changes to the individual member election process. The
committee is currently considering proposing a change to either
Condorcet or STV and held a town-hall meeting in Hong Kong on the
subject. Todd noted that the meeting was lightly attended and there
generally has been rather low participation in the process. The main
hurdle to getting such a change passed is that a majority of at least
25% of our individual members would need to vote for the by-laws change
and the turnout for the previous election was only 17%. However, in July
we will be able to begin making inactive members ineligible for voting
and this should help us achieve the required turnout.

Rob gave an update from the DefCore committee\[5\] which is considering
changes to the requirements for commercial implementations of OpenStack
who wish to use the OpenStack trademark. The committee is currently
working to identify a set of must-pass tests and the functional
capabilities which these correspond to. Rob mentioned that some projects
currently have no or minimal test coverage and, as a result, their
capabilities could not be considered for inclusion in the requirements.
Rob also mentioned a "programs vs projects" issue which had been
identified during the committee discussions and that a meeting with the
TC would be required to resolve the issue. I proposed that Rob and Josh
could join the TC's IRC meeting to discuss the issue.

Finally, Simon gave a brief overview of the work of the gold member
application committee. This committee helps prospective gold members
prepare their application such that it fully anticipates all the
questions and concerns the board may have about the application.

### Wrapping Up

While there were some small number of other items on the agenda, we had
run out of time at this point. In the short time available, we had
covered a broad range of topics but hadn't really covered new ground.
This meeting was mostly about rebooting the board for 2014.
