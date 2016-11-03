Title: February 12th OpenStack Foundation Board Meeting
Date: 2013-02-15 17:06
Author: markmc
Tags: OpenStack, OpenStack Foundation Board Meeting
Slug: february-12th-openstack-foundation-board-meeting
Status: published

Yesterday was the first in-person meeting of the 2013 Foundation Board.
We met at Rackspace's offices in San Francisco at Jim Curry's
invitation. The meeting also coincided with the Foundation staff all
getting together in-person for the first time. With so many OpenStack
people converging on the one place, it was quite funny to randomly run
into various people at the Courtyard Marriott around the corner.

The meeting kicked off at 10am after some informal introductions. For
me, it was a case of playing a "hey, are you Tristan?"/"No, I'm Sean"
guessing game. Monty brought his usual wackiness to the ocassion by
handing out beads and wearing a luminous, sparkling orange fedora with
bright blue flashing LEDs. It's Mardi Gras time!

### Formalities

The first item on the agenda was a formal role call. 5 board members
couldn't attend and Tim Bell was on the phone. Also attending were
Jonathan Bryce and Mark from the Foundation staff. Mark Radcliffe, our
outside council, was on the phone.

From that start, it was obvious that it was going to be extremely
difficult for those dialled into the meeting to be able to participate
effectively. This is definitely something we will continue to struggle
with and, as one of the few who had to travel halfway around the world
for the meeting, I can certainly sympathise with those on the phone.

As a further formality, Alan Clark reviewed some of the existing board
policies:

-   that observers are allowed at board meetings, except in the case of
    executive sessions
-   that board members wouldn't blog or tweet until after an official
    summary of the meeting had been posted to the foundation list

There was some discussion about how executive discussions should be
handled. How we can describe what the topic of any executive sessions
were and perhaps also publicly hold any votes arising from those
sessions.

Rob Hirschfeld proposed that our general decision making process should
involve first coming to an agreement on the criteria for making the
decision and then applying the criteria. The idea was that this process
would avoid some circular debates and save time.

### User Committee

Next up, Ryan Lane presented an update on the progress of the User
Committee. He described the mandate of the committee as "fighting for
the users". The initial goals of the committee are to define their
charter and a set of categories of users. Ryan encouraged the board to
review and [comment on the Google Doc they had
prepared](https://docs.google.com/document/d/1yD8TfqUik2dt5xo_jMVHMl7tw9oIJnEndLK8YqEToyo/edit).

Much discussion was had about how to gather data about our users.
Options included a CRM system, user polls, anonymous usage reporting
tools, aggregating statistics to protect the innocent and the like. This
is clearly going to be a very hot topic for the committee.

During the discussion, Josh McKenty posted [a blueprint for how a opt-in
tracking
system](https://blueprints.launchpad.net/oslo/+spec/opt-in-stats-tracking)
might work.

We also had an interesting debate about the committee should move
forward with adding more members to the committee. The committee's own
proposal for this was to be democratic and have elections for
representatives from different geographies or categories of users. Quite
a few board members raised concerns about this approach and asked the
committee members to press forward quickly and appoint a diverse set of
members with minimal bureaucracy.

Once Ryan had finished, the board expressed their thanks and support for
the efforts of the committee. Ryan was asked to stay and observe the
board meeting, but Ryan preferred to go and get some "real work" done.
That's the spirit!

If you want to follow the progress of the user committee, the best way
is to [subscribe to user-committee@lists.openstack.org mailing
list](http://lists.openstack.org/cgi-bin/mailman/listinfo/user-committee).
Ryan would be happy to share his slide deck if you email him.

### Legal Affairs Committee

Alice King and Nissa Strottman took the floor and presented the work of
the Legal Affairs Committee on the whole area of patents and risk
mitigation.

Alice and Nissa first talked the board through some background on
patents. They described the "risk landscape" in terms of competing
companies suing and counter-suing each other for infringement (Alice had
an awesome diagram of ["who's suing who in the mobile
industry"](http://www.textually.org/textually/archives/2010/10/06/mobilelawsuits.png)
which got a good laugh from everyone) but also, perhaps more
importantly, the threat of Non Practicing Entities or "patent trolls".

We talked in some detail about the Patent Grant in the Apache License
and how it does a lot to mitigate the risks but doesn't completely
eliminate them. In particular, it does little to help with the threat of
NPEs. An interesting debate followed about various nuances of the Apache
License definitions and how they relate to OpenStack.

Alice and Nissa described approaches taken by other communities - e.g.
OIN, GPLv3, Open Compute and Eclipse - and also how an additional
contributor agreement could be adopted by the project to further help.
Brian Stevens talked about how the OIN works and how it isn't strictly
limited to Linux. It was noted that many of the larger members of the
Foundation are also members of OIN. Eileen Evans described how the
adoption of a new contributor agreement would be a massive bureaucratic
challenge for some of the larger companies involved in the project.

A point on one of the slides that a more robust patent policy would
remove a barrier to OpenStack's adoption triggered some discussion about
whether patent risk is in fact hindering OpenStack's adoption. The
consensus seemed to be that this wasn't seen as a huge issue and how, in
fact, OpenStack is in as good a position as most any other open-source
project. While it's important for the Foundation to do due diligence on
this matter, it's also important that we don't overstate the actual
risk.

Another topic discussed was the question of "defensive publication" of
ideas generated by the developer community so that they are properly
documented in a way that is accessible to lawyers who wish to
demonstrate prior art. Various ideas were suggested about how blueprints
could form the basis for such an approach and how to do this without
placing the burden on the developers.

It's amusing the way we wind ourselves in knots over these things and
generally come to the conclusion that the issues are difficult, but that
things are working pretty well as they currently stand.

Finally, with limited time available, we picked up again on some of the
discussion from the previous board meeting about the scope, name and
makeup of the committee. Some board members seemed fine with how things
currently stand while others reiterated the issues previously discussed.

Anyone interested in the legal affairs committee should talk to Alice
King about how to get involved. She would be happy to share her slides
with those interested.

### Lunch

At this point, it was time to break for lunch. Most board members stayed
for the lunch provided on-site and had productive, informal discussions
while eating.

Monty, Nick Barcet and I attended a Technical Committee meeting over IRC
while also eating and chatting with the rest of the board. That's
multi-taksing! Amazingly every single member of the TC attended the
meeting and we voted unamimously to [update the Incubation Process as
recommended by the IncUp
committee](http://lists.openstack.org/pipermail/openstack-tc/2013-February/000119.html).
Such a level of TC consensus is completely unprecedented and took a
tonne of work to achieve. Kudos to Thierry for herding the cats on this.

### Financial Report

Sean Roberts presented a report on the work of the Financial Oversight
committee and we discussed the progress on completing the Foundation's
first financial audit and the updated financial forecast for the year.

The topic was so uncontroversial (you could even say boring) that we
didn't even take much in the way of notes on it. There was unanimous
agreement that this is how it should be and we'd be doing something
wrong if the topic was "interesting". The board praised the committee
and the staff for their dilligence in doing everything to make sure the
Foundation's financial affairs were beyond question.

### Transparency

Josh McKenty was next up presenting [his proposal for a Transparency
Policy](https://etherpad.openstack.org/TransparencyPolicy) for the board
and his wanting volunteers to form a committee to finalize the details.

He described the committee's goal as:

> To improve transparency and foster collaboration between the
> foundation members and members of the board, technical committee, user
> committee and other committees. Specifically, to draft statements and
> prototype systems changes for board review and approval.

A large part of the discussion was around trying to quantify the problem
we'retrying to solve and understanding how we'd achieve closure on it.
The board doesn't want to be consumed with this indefinitely, so how
will we know when it's simply a case of "you can't please everyone".

We wrapped this up by gathering volunteers for the committee:

-   Nick Barcet
-   Jonathan Bryce
-   Alan Clark
-   Eileen Evans
-   Tristan Goode
-   Rob Hirschfeld
-   Kyle MacDonald
-   Joshua McKenty
-   Mark McLoughlin
-   Lauren Sell

### Director's Report

Next up, Jonathan provided an awesome update on the Foundation's
progress and plans. It's clear an awful lot of time and thought went
into this super-helpful and encouraging update.

One of Jonathan's slides showed some mind-blowing statistics detailing
the growth of the developer community, user community and ecosystem. The
statistics on the number of patches merged every month were really
stunning and the board praised the success of the project's
infrastructure team in enabling this level of activity.

Jonathan talked to his hiring plan and introduced the latest Foundation
employees. We're executing almost to the plan and there are two
positions still to fill - another infrastructure engineer and another
community manager.

There was a brief discussion of the updated budget. The summary is that
slightly more money is both coming in and going out than planned, giving
a positive net effect. A motion was passed to approve the new budget.

The discussion moved more to event planning and marketing matters and
Lauren Sell filled the board in on a lot of the details in this area.

Planning of the Havana summit was well in hand and it was noted that the
choice of venue means that costs will rise more linearly with attendance
than previous summits. Lauren discussed the venue selection process for
the October 2013 summit which should come to a conclusion soon. Future
summits were discussed with general agreement that a two year cycle
should be rougly East Coast US, Asia, West Coast US and Europe. Several
board members expressed a desire to get started on the selection process
for the October 2014 summit since the size of the event means that
suitable locations get booked up very far in advance.

Lauren also [described her efforts to bring the various marketers
at](http://wiki.openstack.org/Governance/Foundation/Marketing) dozens of
OpenStack companies together with some of the same principles that drive
the collaborative software development process. She has created a
[mailing
list](http://lists.openstack.org/cgi-bin/mailman/listinfo/marketing)
which already has almost 100 members and holds a regular phone meeting
of the group. The goal is to have all those involved in marketing
OpenStack to be highly co-ordinated and "on message".

Finally, Lauren quickly presented an independent study she had just
received on OpenStack's marketing impact relative to other open-source
projects and industry players. The results of the study were simply
stunning and most of us appeared to be struggling to believe them.
However, even if the statistics on OpenStack are massively inflated,
we're still hugely being successful. Lauren, Mark and Jonathan have
already worked with the authors of the report to find any data that
could undermine the conclusions and will continue to do so.

Jonathan and Lauren can be contacted directly for the materials they
presented to the board.

### Strategy Session

Jonathan moved on to kick off a strategy session where board members
would have an opportunity to put their thinking hats on and brainstorm
together. He teed up the discussion by presenting his thesis that
OpenStack was building a "platform ecosystem" with huge potential for
network effects that would result in OpenStack being the dominant cloud
platform in the market place.

We then moved onto having a short exercise where we used sticky-notes to
throw out our ideas in three areas - "interoperability", "reference
architectures" and "engaging users". Once the ideas had been gathered,
we split into breakout groups to discuss ideas for each of those areas.

Rather than trying to capture all of the ideas and action items from the
discussions here, it's perhaps easier to call out some highlights:

-   We're going to explore the use of Tempest as an API compatibility
    testing tool which can be pointed at an OpenStack instance. The idea
    is that anyone who wants to license the OpenStack trademark would
    request a test run which would result in a scorecard. At every
    release, the board would update the  
   results required for each OpenStack mark so that obtaining a
    trademark license simply becomes a matter of fixing any failing
    tests which are required for the desired mark.
-   We're going to explore the definition of reference architecture
    "flavours" and how these reference architectures could be defined
    and maintained. The initial idea is that Heat templates could be
    used as a deployable reference architecture definitions.
-   In terms of engaging users, we decided that trystack.org and
    deployment tracking tools were crucial.

### Election Process Committee

Todd Moore raised the question of whether allowing Foundation staff to
run for the Individual Member Director elections was a waste of a board
seat since staff members are so involved in the Foundation anyway. The
question of potential conflicts of interest was also raised. There was
no time to debate this question so the board resolved to reconstitute
the Election Process Committee to consider this question and the general
question of the eligibility to run and vote for these board seats.

The committee will consist of Todd as chair and the 8 individual board
members.

### Evening Event

We wrapped up at 6pm sharp and headed over to a nearby restaurant with
all of the Foundation staff members. Far from simply being a social
event, it was incredible to see 30+ focused and committed folks spend
over 4 hours going from conversation to conversation about how to
continue OpenStack's success into the future. For me personally, those
conversations alone were enough to justify the effort it took to get to
the meeting.
