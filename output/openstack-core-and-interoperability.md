Title: OpenStack "Core" and Interoperability
Date: 2013-10-30 21:49
Author: markmc
Category: openstack
Slug: openstack-core-and-interoperability
Status: published

I've been following the ["what is core?"
conversation](http://robhirschfeld.com/2013/07/22/kicking-off-core/)
since the ["Incubation Update"
committee](https://wiki.openstack.org/wiki/Governance/Foundation/IncubationUpdate2013)
completed its work some time ago. I'm really happy to see Rob, Alan and
others put so much work into moving this along, but each time I try to
catch up on progress I find myself a little bewildered.

Since it's going to be a big topic during [next week's board
meeting](https://wiki.openstack.org/wiki/Governance/Foundation/4Nov2013BoardMeeting),
I figured I'd try to get my thoughts together here.

### What's it all About?

Even the question bothers me - "what is core?". Why is that an important
question?

One reason for its importance is that the bylaws say:

> The Core OpenStack Project means the software modules \[...\] for
> which an OpenStack trademark may be used

In other words, Heat can't call itself "OpenStack Orchestration" unless
the Board of Directors approve Heat as part of "The Core OpenStack
Project". If that was all this was about, I'd be like "hell yes! Heat
should be known as OpenStack Orchestration!". But, it's clearly not just
about this, so I tend to ignore this aspect. I don't actually think much
of what is being discussed is all that relevant to this particular
issue.

So, what else is this all about? Well, one clue is the emphasis on
testing in [Rob's list of "10 core
positions"](http://robhirschfeld.com/2013/08/13/openstack-core-positions/).

> OpenStack Core means passing all “must-pass” tests

This is an example of where I get really confused. Maybe I'm just
getting hung up on language. I think we're talking about cloud
providers, distributions, vendors, deployers, etc. self-certifying
themselves using a test suite in order that they can use the OpenStack
trademark. But are we talking about labelling these self-certified
clouds as "Core"? Aren't we making this all very confusing by using the
term "Core" both to describe the self-certified clouds/products and also
to describe the subset of OpenStack they are required to include? I'd
phrase this as:

> The OpenStack Core definition includes a list of tests which certified
> clouds must pass

Anyway, I'm not going to nitpick my way through all of this. I *think* I
understand the intent here, but I like to approach this from an entirely
different angle.

### A Market of Interoperable OpenStack Providers

(Yes, that is Simon Wardley's terminology)

We all know that one of the basic goals of OpenStack is for there to be
a bunch of public clouds available to users around the world and that
interoperability between these public OpenStack clouds will make it
easier for users to switch cloud providers and encourage competition
between these providers.

To my mind, that's what this whole "what is core?" conversation is
really about. We want to use an OpenStack trademark program to help
build this marketplace by enforcing interoperability between clouds
which use the OpenStack trademark.

(And yes, I understand that the "what is core?" discussion is also
related to questions like what is required of an OpenStack distribution.
I'm focusing on the question of public cloud interoperability because I
think it's the most important. IMHO, the whole conversation is pointless
unless it moves this particular topic along quickly.)

To do that, we need to define which APIs these clouds must expose, or as
Rob puts it - which use cases these clouds must support. To take a
simple example, should these clouds be required to expose the Glance API
for uploading images?

And here's where I get confused again. Why are we talking about "what is
core?" when we could simply say "which APIs are required to be exposed
by certified OpenStack clouds?". Again, I'm trying not to be a pedant,
but the way the question is framed leaves me unsure whether we're really
all talking about the same thing.

I think the focus should be on immediate baby-steps towards
kick-starting this marketplace. One simple question - if and when we
certify the first batch of interoperable clouds, would we rather have a
smaller number of big clouds included or a large number of smaller
clouds? In terms of resource capacity provided by this marketplace, I
guess it's more-or-less the same thing.

Let's assume we absolutely want (at least) a small number of the bigger
providers included in the program at launch. Let's say "small number"
equals "Rackspace and HP". And let's assume both of these providers are
very keen to help get this program started. Isn't the obvious next
baby-step to get representatives of those two providers to figure out
exactly what level of interoperability they already have and also what
improvements to that they can make in the short term?

If we had that report, we could next do a quick "sniff test" comparing
this to many of the other OpenStack clouds out there to make sure we
haven't just picked two clouds with an unusual set of compatible APIs.
Then the board could make a call on whether this represents a reasonable
starting point for the requirements of OpenStack clouds.

No, this isn't perfect. But it would be a genuine step forward towards
being able to certify some clouds. We would have some data on
commonalities and have made a policy decision on what commonalities are
required. It would be a starting point.

### OpenStack Compatible?

The next big decision for the board is whether a cloud which uses the
OpenStack trademark must actually be a deployment of OpenStack's code.
Is this a question of "OpenStack clouds" or "OpenStack compatible
clouds"?

I do think it would be damaging to OpenStack if this marketplace took
off and was dominated by providers which don't use or contribute to
OpenStack. But, [as Rob
says](http://robhirschfeld.com/2013/07/22/making-openstack-meaningful/),
the trademark isn't the only way of avoiding this situation - there's
also our "velocity and culture".

I struggle to see how trademark requirements around the use of OpenStack
code would work. How do you define which code must be used? Must that
code be used unmodified? If not, how much can you change? What does it
even mean to "use" a piece of code? That user requests must be executed
using that code? Maybe this would just be a "yes, we use and contribute
to OpenStack" good faith statement which the Foundation would make a
judgment call on? If so, how do we ensure transparency and fairness
around how that call is made?

If this question proves to be a stumbling block, I'd prefer to see an
"OpenStack compatible cloud" trademark program established quickly.
Getting these interoperability guarantees in place for our users takes
priority over ensuring that certified providers actually use and
contribute to OpenStack.

### Conclusion of Sorts

I think our immediate concern should be kicking off a trademark program
for certifying interoperability between OpenStack clouds. I'm frustrated
whenever I think this "what is core?" discussion is tackling questions
which aren't immediate blockers to making progress on this program.

The board has to make (or oversee the making of) some policy questions.

Firstly, what APIs are required in OpenStack™ clouds? I'd favour
starting to answer this by first looking at the current interoperability
levels between existing clouds.

Secondly, whether and how we insist on the use of OpenStack code in
OpenStack™ clouds. If this turns out to be a difficult problem, then I
think we should just start with an "OpenStack™ compatible cloud"
program.
