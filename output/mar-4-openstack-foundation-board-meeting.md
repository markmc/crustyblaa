Title: Mar 4 OpenStack Foundation Board Meeting
Date: 2014-03-12 00:52
Author: markmc
Category: openstack, openstack-foundation-board-meeting
Slug: mar-4-openstack-foundation-board-meeting
Status: published

On March 4th, the [OpenStack Foundation Board of
Directors](https://www.openstack.org/foundation/board-of-directors/) met
for an [all-day, in-person
meeting](https://wiki.openstack.org/wiki/Governance/Foundation/4Mar2014BoardMeeting)
at DLA Piper's office in Palo Alto, California. This my informal
recollection of the meeting. It’s not an official record, etc.

Some 20 of the 24 board members managed to make the meeting in person
with Todd and Tristan joining over the phone. Yujie Du and Chris Kemp
were unable to attend.

As usual our teleconferencing capabilities were woefully inadequate for
those hoping to contribute remotely. However, this time Rob and Lew
joined a Google Hangout with video cameras trained on the meeting. One
would hope that made it a little easier to engage with the meeting, but
we didn't really have any feedback on that.

Before we got started properly, Alan took some time to recommend
["Startup Boards: Getting the Most Out of Your Board of
Directors"](http://www.amazon.com/Startup-Boards-Getting-Board-Directors/dp/1118443667)
to the directors (based, in turn, on Mark Radcliffe's recommendation) as
a book which could provide some useful background on the
responsibilities of directors and what it takes to make a successful
board.

\[Update: Josh points out we also approved the minutes of the previous
meeting\]

### Executive Director Update

Our first meaty topic was one of Jonathan's regular updates.

Jonathan talked about the continued tremendous growth in interest around
the project will all the foundation staff's key metrics (e.g. website,
developers, twitter, youtube, etc.) at lease doubling in 2013. One
interesting aspect of this growth is that the China, India and Japan
regions all grew their share of website traffic and this lead to a
discussion around whether having the last summit in Hong Kong directly
contributed to this shift.

Our community is growing too. We now have over 15,000 individual members
of the foundation, over 2,000 contributors to the project over its
lifetime and over 400 unique contributors to the project each month.

The mention of 15,000 individual members lead to a somewhat lengthy
discussion about the fact that [individual membership may be
terminated](http://www.openstack.org/legal/individual-member-policy/)
under the following clause of the bylaws:

> failure to vote in at least 50% of the votes for Individual Members
> within the prior twenty-four months unless the person does not respond
> within thirty (30) days of notice of such termination that the person
> wishes to continue to be an Individual Member

Jonathan explained how shortly after the foundation was launched, over
6,000 people signed up as individual members. Only 1,500 or so of those
initial members have since voted in elections, so we could potentially
be looking at removing somewhere in the region of 6,000 members in 2014.
This reduced membership will facilitate bylaws changes by making it
easier (or even possible) to reach the [quorum necessary under clause
9.2(a)](http://www.openstack.org/legal/bylaws-of-the-openstack-foundation/):

> requires an affirmative vote of a majority of the Individual Members
> voting as provided in Article III, but only if at least 25% of the
> Individual Members vote

Some discussion points around this included whether a future bylaws
change should reduce the quorum requirement to something like 10%, that
terminated members can re-register but would then have to wait 180 days
in order to be eligible for voting and that project contributors need to
be foundation members but some contributors may not be in the habit of
voting and may have their membership terminated.

Jonathan moved on with his slide deck and briefly mentioned some of the
foundation's new supports like Oracle and Parallels. He also talked
about OpenStack is increasingly fulfilling its role as a platform and is
being put to work for many diverse use cases. He also included a slide
with many positive media and analyst quotes about the project like
"Industry support has coalesced around OpenStack".

Jonathan then moved on to the foundation's budget, describing it as an
\$8M budget which turned out to be \$11M. Income was up, but expenses
were kept in line such that \$2.5M could be put in the bank. He
expressed particular pride that 18 months ago the foundation was just
starting with no money and already had built up a significant buffer
which would allow us all to feel confident about the foundation's
future, even in more turbulent or unpredictable times.

Finally, Jonathan review the foundation staff's priorities for 2014:

1.  Improve the software - whether that be continued investment by the
    foundation in the software development process or organizing
    activities which bring user feedback into the project
2.  Improve interoperability between OpenStack-powered products and
    services
3.  Grow the service provider global footprint, with a specific mention
    for interest from telco operators at Mobile World Congress around
    OpenStack and NFV

### DefCore Update

Next up, Rob and Josh provided an update on the progress of the DefCore
committee, requesting a checkpoint from the board as to whether there
was consensus that the current approach should continue to be pursued.

Rob started by reviewing [the purpose of DefCore and the approach taken
to date](https://wiki.openstack.org/wiki/Governance/CoreDefinition). He
explained that the committee is mandated to look at ways of governing
commercial use of the OpenStack trademark and that some issues are
deliberately being punted on for now, e.g. an API interoperability
trademark and changes to the bylaws.

Josh took over and reviewed the [currently agreed-upon
criteria](https://etherpad.openstack.org/p/DefCoreTestCriteria) that
will be used when evaluating whether a given capability will be required
in order to use the trademark, e.g.

1.  Stable - required to be stable for &gt;2 releases
2.  Complete - should be parity in capability tested across extension
    implementations
3.  Discoverable - e.g. can be found in Keystone and via service
    introspection
4.  Widely Deployed - favor capabilities that are supported by multiple
    public cloud providers and private cloud products
5.  Tools - supported by common tools
6.  Clients - part of common libraries
7.  Foundation - required by other must-have capabilities
8.  TC Future Direction - reflects future technical direction
9.  Documented - expected behaviour well documented
10. Legacy - previously considered must-have
11. Cluster - tests are available for this capability?
12. Atomic - unique capability that cannot be built out of other
    must-have capabilities
13. Non-Admin - capability does not require administrative rights

Next, Rob, Josh and Troy walked the board through a [draft spreadsheet
evaluating potential capabilities against those
criteria](https://docs.google.com/spreadsheet/ccc?key=0Av62KoL8f9kAdFo4V1ZLUFM0OHlrRnFpQUkxSHJ5QWc&usp=drive_web#gid=6).

Much of the subsequent discussion revolved around various board members
being very eager to get wider feedback on the ramifications of this
process, particularly around identifying the most thorny and
controversial results. Concerns were expressed that the process has been
so involved and detailed that few people are well appraised of where
this is headed and may find some of the results very surprising.

Rob & Josh felt that this spreadsheet approach means that we can solicit
much more targeted and useful feedback from stakeholders. For example,
if a project feels one of its capabilities should be must-have, or a
cloud provider is surprised that a capability it doesn't yet provide is
seen to be must-have, then the discussion can be around that specific
capability, whether the set of criteria and weighting used for
evaluation are appropriate, and whether the capability has been
correctly evaluated against those criteria.

Finally, Rob & Josh explained the proposed approach for collecting the
test results which would be used for evaluating trademark use
applications. The idea (known as TCUP, or "tea-cup", for "test collect,
upload and publish") currently being developed in the [refstack repo on
stackforge](https://github.com/stackforge/refstack) would allow people
to download a docker container image, add your cloud credentials and
endpoint URL, run the container which would then execute the tests
against the endpoint and upload the results.

\[Update: Josh points out that data uploaded via TCUP will "be treated
as confidential for the time being"\]

### Driver Testing

Next, Boris Renski took the floor to talk about Nova, Neutron and Cinder
driver testing particularly with a view to how it might relate to
trademark usage. This relates to [his blog post on the
topic](http://www.mirantis.com/blog/openstack-will-open-source-vendor-certifications/)
some weeks ago.

There were two main observations about changes happening in the
technical community - (1) that projects were demanding that vendor
maintainers provide reliable third-party automated testing feedback in
gerrit patch reviews and (2) that manually maintained, often
out-of-date, "driver compatibility matrices" in the OpenStack wiki may
soon be replaced by dashboards showing the results of these third-party
automated testing systems.

Boris wished to leave that technical work aside (since it is not the
board's domain) and focus the discussion on whether the board would
consider a new trademark program such that vendors who's drivers pass
this automated testing would be allowed the use of a trademark such as
"Built for OpenStack".

The debate quickly got heated and went off in several different
directions.

Part of the discussion revolved around the automated testing
requirements projects were placing on projects, how that worked in
practice, the ramifications of that, how deprecating drivers would work,
whether a driver being in-tree implied a certain level of quality, etc.
I felt the board was really off in the weeds on a topic that is under
the authority of the individual projects and the TC. For example, it was
easy to forget during the discussion that PTLs ultimately had the
discretion to waive testing requirements for individual drivers.

Another surprising element to this was parallels being drawn with the
overlap between the [OpenStack Activity
Board](http://activity.openstack.org/dash/browser/) and
[Stackalytics](http://www.stackalytics.com). Some board members felt
that Mirantis's work on Stackalytics had deliberately duplicated and
undermined the Activity Board effort, and that the same thing was
happening here because this driver testing dashboard naturally
(according to those board members) belongs under the DefCore/Refstack
efforts. Boris acknowledged he "had his wrist slapped over Stackalytics"
and was attempting to do the right thing here by getting advance buy-in.
Others felt that the two efforts were either unrelated or that competing
efforts can ultimately lead to a better end result.

Another thread of the discussion was that Boris's use of, or allusion
to, the special term "certification" automatically strayed this topic
into the area of the OpenStack brand and that it was inappropriate to
speculate that the foundation would embark on such a program before the
board had discussed it.

In the end, the board directed that Jonathan should work with Boris and
Rob on a plan to collect any automated test results out there and,
secondly, work with the DefCore legal subcommittee to explore the
possible use of the trademark in this context.

### Operator's Feedback

Tim Bell took the floor next to talk the board through [feedback from
OpenStack
operators](https://etherpad.openstack.org/p/operators-feedback-mar14)
collected at the OpenStack Operators Mini Summit the previous day.

The etherpad linked above perhaps provides a better summary than I can
give, but some of the highlights include:

-   The notion that operators should be able to provide feedback on
    blueprints as they are drafted, to help get operational insights to
    developers early on in the development process
-   Some observations on the stability (or lack thereof) of some of the
    core OpenStack components
-   The importance of a solid upgrades story was re-iterated
-   Some great feedback on TripleO
-   The split between teams doing CI/CD and those consuming releases
-   How to encourage operators to file more bugs upstream
-   Lots, lots more

This feedback was well received by the board and triggered a bunch of
discussions and questions.

As a final point, Josh raised some concerns about how the invitee list
was drawn up and how he felt it would have been appropriate for vendors
(like Piston) to recommend some of their customers to be invited. Tim
felt this was an unfair criticism and that the user committee had worked
hard to seed the limited seating event with a diverse set of invitees
before opening it up to the public.

### Emerging Use Cases - NFV

Finally, with limited time remaining, Toby Ford from AT&T briefed the
board on Network Function Virtualization (NFV) as an emerging use case
for OpenStack which is heavily tied to SDN (Software Defined Network).
He described how AT&T have set themselves a mission to:

> Simplify, open up, and scale our Network to be more agile, elastic,
> secure, cost effective and fast by (a) moving from hardware centric to
> software centric, (b) separating the control plane and data plane and
> (c) making the network more programmable and open

Toby did a great job of walking through this complex area, leaving me
with the understanding that there is a massive shift in the networking
industry from hardware appliances to scale-out software appliances
running on virtualized commodity hardware.

There appears to be consensus in the networking industry that OpenStack
will be the management and orchestration platform for this new world
order, but that there is a serious need for telcos and networking
vendors to engage more closely with OpenStack in order to make this
happen.

### Wrap Up and Evening Event

Alan then wrapped up the meeting a little early after talking through
the schedule for our next meetings with a conf call on April 3 and an
in-person meeting on May 11.

The board then moved on to a local restaurant for dinner. Before and
after dinner, I had some great conversations with Tim, Monty, Van and
Troy. Funnily enough, because of the layout of the tables and the noise
in the restaurant, it was only really possible to talk to the person
sitting directly opposite you and so I found myself having an exclusive
2 hour dinner date with Boris! At one point, after Boris knocked a glass
of wine over me, I joked that I should tweet "Red Hat and Mirantis
tensions finally bubble over to physical violence". But, in all honesty,
these in-person, informal conversations around the board meetings are
often far more effective at enabling shared understanding and real
collaboration than the 20+ person meetings themselves. Such is the
nature of the beast, I guess.
