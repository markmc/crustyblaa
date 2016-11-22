Title: Sustainable Investment in Open Source
Date: 2016-11-22 11:00
Author: markmc
Tags: OpenStack
Slug: sustainable-investment-in-open-source
Status: published

*This is the prose version of a talk I gave today at OpenStack Day,
France. The [slides are available
here](https://redhat.slides.com/markmc-redhat/sustainable-investment-in-open-source).*

Today, I want to speak about a somewhat subtle, meta-topic. I hope to
share some insight on the question of how a company should think about
its investment in any given open-source project. The reason I think
the subject is important right now is that, as OpenStack follows its
inevitable path through the “hype curve”, we are seeing some major
players in the OpenStack ecosystem have recently re-shaped their
investment in the project. I think there is plenty of opportunity for
companies to take a much more realistic view on this subject, and my
hope is that this will lead to a much more sustainable level of
investment in the project.

# My Story

My views on this question are so heavily influenced by an early
personal experience, that I’m tempted to talk at length about my own
story. But time is short. Very quickly, though, as I was finishing
university, I realized I wanted to focus my career on open-source, and
I was faced with the obvious question of who was going to pay me to
work on open-source? What value would be open-source work bring to my
employer? I spent a lot of time thinking about this, even after I
found myself employed to work full time on open-source.

# My Employer

An interesting thing happened. Because I had spent a good deal of time
thinking about the value of my own open-source work, I was well-placed
to help my employer think about how, where, and why to invest in
open-source projects. It quickly became apparent to me then - and is
still apparent to me now - that this fundamental question is fraught
with difficulty, and most people struggle greatly to answer it.

# Investment vs Business Needs

Over the years, I’ve boiled my answer to this simple-sounding question
to something equally simple - your investment in a project should be
directly related to what the business needs from the project. I think
it’s important to frame it this way, because if the business doesn’t
have a good have a good understanding in the value of an investment,
the business is going to be quick to continue that investment when it
is looking at how to make the best use of its resources.

# Anti-Patterns

What do I mean about an investment that isn’t directly related to the
needs of the business? Let me dig into that a little bit with some
anti-patterns.

## Focus on Features

First, features. Or, [as Thierry Carrez puts it, “tactical
contributions”](https://fnords.wordpress.com/2011/09/28/the-next-step-for-openstack/). Companies
often look at the “what do we need from this project” question through
the lens of feature analysis - what are my requirements? What is missing?

The good thing about contributing features is that it is directly
related to business needs. The thing about your primary focus being on
new feature development is it misses the bigger picture. A community
of developers that is focused only on their own new features is not
going to get anywhere. Who is thinking about the long-term future of
the project? Who is looking at feedback from users? Who is merging the
code for these new features?

All of these types of activities are the basic necessities of any
software project. They are the basis through which new features get
added. You must invest in ensuring that this is happening in this
project whose future you care about.

## The Donation

This anti-pattern is about our choice of language, and how it affects
our thinking. People often talk about “donating” code to a
project. Calling it a donation suggests you have a feeling that
the return on your investment is quite intangible. How long will you
continue with these “donations”?

## For Recognition

Related, it’s often quite clear that a major motivation for companies
investing in open-source is the recognition they receive in doing
so. Certainly, in OpenStack, with Stackalytics we have spawned an
impressively pointless competition between companies for ranking in
contributor statistics. If you give your employees the goal of
achieving a particular ranking in the contributor statistics, you may
achieve this, but what does that really achieve?

The type of business value that it delivers is essentially short-term
marketing value. We don’t want investment in open-source projects to
be made out marketing budgets, since that’s possibly the least
reliable source of funding!

## "100% Upstream"

Not so long ago, when companies were falling over themselves to
demonstrate their commitment to OpenStack, we saw an interesting
phenomenon - the “100% dedicated upstream resource”. These were
individuals and teams at various companies who were employed to
contribute to the project but - as far as I can tell - were
self-directed and deliberately kept isolated from any “downstream”
work.

This is an incredibly alluring opportunity for those involved! The
company is saying that the project is critically important to the
business and whatever you or your team does to help the project be
successful, that’s valuable to the company! Unfortunately, we can see
how these things go in cycles and, at some point, the company will
take a harder look at what this person or team is doing. When that
happens, the likelihood is that the company has very little visibility
into - or understanding of - the work being done and, worse, the
person or team has no experience articulating how the value of the
work is meaningful to the business!

There are some exceptions to this, even within Red Hat. But as a
systematic way of investing in a project … it’s unlikely to be
sustainable.

## Non-Profit Staff

Finally, the culmination of a number of these anti-patterns - the idea
that companies should "donate" to a non-profit organization like the
OpenStack Foundation, have that organization use the donations to
employ staff who are "100% dedicated upstream resources", and the
value to companies ...? The recognition it receives for being such
generous benefactors?

Having some technical staff employed by the non-profit is fine. Some
of my favorite people work for the OpenStack Foundation! My preference
would be for Foundation staff to be in facilitation roles. But
certainly, you would do well to avoid this pattern for the majority of
the contributors on a project.

One example of this is the [Linux Foundation's Core Infrastructure
Initiative](https://www.coreinfrastructure.org/). In the wake of the
OpenSSL Heartbleed vulnerability, the Linux Foundation brought
together funding from a number of companies to invest resources for
key projects like OpenSSL. It's fascinating because here is a project
like OpenSSL that many, many businesses depended on, but few invested
in. What the Linux Foundation has done is positive, but I can't help
feel we have failed as a community if this is the only way to sustain
these projects. You'll notice that Red Hat hasn't joined this
initiative, despite us being supportive of it - we have always
invested in these projects directly, and think that is actually a
healthier model for the future.

# Think Strategically

Ok, so that's a bunch of anti-patterns ... what you generally
shouldn't do. What should you do? Well, you need to think
strategically. You are choosing to have your business depend on
something you don't control, but you should not allow yourself to feel
powerless about how successful that choice will be.

## The Future

Think about the future, the long-term. Given the business choice you
are making, for how long will your business success depend on the
success of the project? Indefinitely? What are you doing to ensure
that success?

One way to think about that would be a worst-case scenario. The
unimaginable happens, and the rest of our community disappears. You
are left almost completely alone maintaining the project. What you
focus on? Obviously, you wouldn't choose to depend on a project where
there is a possibility of that happening, but the thought exercise
does help you think about your priorities.

## Influence

If you are determined to ensure the success of the project, you'll
have your own view of what that success looks like. Are you happy to
hope the community will find a direction that fits your needs, without
any input from community leaders that understand the needs of your
business?

At Red Hat, we talk about wearing "two hats". Given a particular
problem, a particular question of direction, you should have the
ability to understand what's good for the project overall and what's
good for Red Hat. And crucially, you should have a way to reconcile
those two views. This is not a zero sum game. Almost always, you can
find a solution that is good for both the project and Red Hat. Why
would Red Hat want a solution that is harmful to the project?

## Expertise

In order to be successful with any technology, you need to have access
to expertise that understands the technology. There is no better
expertise than the authors or maintainers of the project. These are
the people who understand not just how the technology works now, but
how it evolved there, and how things are likely to change in the
future. They understand the pitfalls, the know the cool new tricks.

You can have access to that expertise by having those experts join
your team. They stop being experts pretty quickly if they stop having
time to work on the project, so their upstream responsibilities should
continue to be a significant proportion of their time. But you'd be
amazed at how their presence on the team can help the whole team be
successful.

# Red Hat's Model

As somewhat of an aside, since this presentation is not a sales pitch,
think about Red Hat's business model, and our proposition to our
customers. Certainly part of the model is that, through our product
subscriptions, the customer is investing in the projects involved and,
by proxy, is safeguarding the future of the project, gaining a level
of influence in the project, and has access to expertise relating to
the project.

# A Measurable Goal

Recently, on Red Hat's OpenStack team, and thanks to the influence of
[Alexis Monville](http://alexis.monville.com/), we've been using the
["Objectives and Key Results"](https://en.wikipedia.org/wiki/OKR)
framework for using well-defined, measurable goals to guide our
teams. We started brainstorming on these OKRs almost a year ago, and
from those early discussions, I wondered “how do we frame an
measurable goal around our investment in upstream?”. What indicator
could we use to know whether we were on the right track, and to ensure
we’d stay on the right track?

## Our Vision

Our first thoughts on this was to look at data like our position in
the contributor statistics, or the number of core contributors, PTLs,
or TC members on our team. None of this sat well with us, though,
because we have seen that these type of goals don’t drive the right
behaviors. When we started drafting a vision statement for each goal,
I wrote:

“Teams of engineers with the required motivation, an understanding of
Red Hat's vision, and empowered with the necessary time,
encouragement, and recognition, working upstream to drive and
influence many diverse parts of OpenStack.”

And there it sat for a while, us all lacking ideas on how to measure
this. Quite recently, Russell Bryant and Doug Hellmann hit on a
promising solution. Survey the team with a small set of questions and
use that sentiment of our measure of success with this goal.

## The Questions

The questions that Russell and Doug developed are:

1. Does your team have effective input into the features accepted and design decisions made upstream?
2. Does your team have effective input into bug fixes and backports made upstream?
3. Does your team have effective input into discussions related to processes, schedules, requirements, infrastructure management, and other decisions made by the upstream OpenStack community in general?
4. What level of investment does your team make in upstream work?

The allowed answers are “not enough”, “just right”, “too much”, and
“don’t know”. We also had a free-form comments section which is
helping us gain insight into the results.

Notice one important aspect of this - we are asking individuals about
the effectiveness of the investment their team is making
upstream. That reflects the vision above.

## The Results

We only recently started running this survey, and we will do one every
release cycle. So far, we’ve had over 70 responses, so that’s a pretty
good start.

![Level of Invesment](http://chart.apis.google.com/chart?cht=p&chs=500x250&chdl=Not+enough%7CAbout+right%7CToo+much%7CDon%27t+know&chl=16.7%25%7C79.2%25&chco=3366CC%7CDC3912%7CFF9900%7C109618&chp=0.436326388889&chtt=Level+of+Investment&chts=000000,24&chd=t:12,57,1,2 "Level of Investment")

The really interesting judgment call we need to make is what
percentage of “just right” answers do we want to aim for? It would
seem misguided to aim for 100% - do we really think that it’s
important that every individual feels we’re striking the right
balance? We’ve arbitrarily chosen 80% as our target, which means we
feel pretty good about where we’re at, but there’s still opportunities
for improvement.

# Sustainability

One thing I’m loving about my job these days is the direct exposure I
have to Red Hat customers who are choosing to invest in
OpenStack. Deciding to build a significant cloud for production use is
a huge decision, and no-one takes it lightly. It’s exciting, and
companies doing this can look forward to a true transformation in how
they think about IT resources. The truly daunting part is the sense of
responsibility that comes with it.

These are long-term choices being made, and they’re being made because
people believe in the future of this project. Red Hat takes the
responsibility seriously by making choices that we hope will ensure
the project has a long, sustainable future.
