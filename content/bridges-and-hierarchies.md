Title:
Date: 2016-12-05 12:00
Author: markmc
Tags: OpenStack
Slug:
Status: draft

I care about OpenStack, and open-source more generally. I spend a lot
of time thinking and worrying about the culture of our community. I
have some insights I’d like to share, and some of them are
frustratingly inconclusive. However, since I’m not contributing to the
project any more, the window of time where anyone should listen to me
on this topic is rapidly shrinking!

# Non-Hierarchical Collaboration

I’m a big fan of [Eben Moglen](http://moglen.law.columbia.edu/). If
you’re not familiar with him, he’s a highly respected lawyer who has
worked in the area of free software since representing the creator of
PGP, Phil Zimmermann, in the mid 90s. I saw him [speak at a Red Hat
summit back in
2006](https://archive.org/details/EbenMoglenKeynote2006RedHatSummit),
and was blown away by his sheer professorial stage presence and his
ability to provide a much broader context for some things I care
deeply about.

Anyway, I saw [Eben keynote again at linuxconf.au last
year](https://www.youtube.com/watch?v=OAKRdZLU7AU), and one phrase he
used really jumped out to me. He was talking about [“non-hierarchical
collaboration”](https://www.youtube.com/watch?v=aOcpDsDSWY0&t=10m45s). That
this was the model for a 21st century organization.

The full context deserves to be quoted. He says:

> People began to understand what distinguishes 21st century social
> organizations from 20th century ones. Industrial society loved
> hierarchy. It had to love hierarchy. The metaphors, the army of the
> unemployed or the industrial workforce. Hierarchy was intrinsic to
> 20th century organizations at their strongest. As was secrecy, or at
> least obscurity.
>
> The ways in which we have done what we have done came to be an
> important lesson in how 21st century organizations work. They are
> distinguished by three elements - transparency, participation, and
> non-hierarchical collaboration.

And he later goes on to talk about how a community should be porous,
so anyone can join. And how it was really only with the onset of real
distributed version control that we were able to achieve truly
collaborative, non-hierarchical, self-government in the free and
open-source software world.

Non-hierarchical collaboration. Frustratingly, while this term
resonates strongly with me, it is pretty useless when describing how
open-source works to the casual observer. What is more hierarchical
than a BDFL and sub-lieutenants?

# The Failure of Agile

Now, bear with me for a second while I appear to completely switch
topic to Agile software development … why I’m talking about this will
become clear later.

Andy Hunt, one of the co-authors of the Agile Manifesto in 2001, wrote
a blog post titled [“The Failure of
Agile”](http://blog.toolshed.com/2015/05/the-failure-of-agile.html). Of
course, this spread around like wildfire, with many people seemingly
only reading the title.

There is some awesome insights in this blog post, however. Andy
complains that the term “agile” has lost its intended meaning, and has
become synonymous with a set of prescriptive, static rules and
practices surrounded by an entire industry of zealous advocates.

I think it’s worth quoting some of his points. He says:

> The word “agile” has become sloganized; meaningless at best,
> jingoist at worst. We have large swaths of people doing “flaccid
> agile,” a half-hearted attempt at following a few select software
> development practices, poorly. We have scads of vocal agile
> zealots—as per the definition that a zealot is one who redoubles
> their effort after they've forgotten their aim.

You can sense Andy’s frustration here. He clearly hasn’t forgotten
what he and others hoped the industry would achieve if guided by the
principles of the Agile Manifesto. He goes on to talk about why he
takes issue with how “Agile” is implemented.

> When you are first learning a new skill—a new programming language,
> or a new technique, or a new development method—you do not yet have
> the experience, mental models, or ability to handle an abstract
> concept such as “inspect and adapt.” Those abilities are only
> present in practitioners with much more experience, at higher skill
> levels.
>
> The only way for beginners to be effective is to follow simple,
> context-free rules; rules of the form: ”When this happens, do that.”
> And since agile methods conveniently provide some concrete practices
> to start with, new teams latch on to those, or part of those, and
> get stuck there.
>
> So instead of looking up to the agile principles and the abstract
> ideas of the agile manifesto, folks get as far as the perceived iron
> rules of a set of practices, and no further.
>
> And if you only pick a handful of rules that you feel like
> following, and ignore the hard ones, then you’ve got it made! You
> are ”doing agile” if anyone asks, and you can focus your energy on
> enforcing a small set of largely useless rules.

Wow! He doesn’t pull his punches.

The point he’s making is that expert agile practitioners should have
the skills necessary to operate at the level of the abstract ideas and
principles of the agile manifesto. Only following rules, guidelines,
and processes right up to the point where their experience and
intuition tells them that something different is required to achieve
those higher level ideals.

There’s a danger that - with all the focus on the simple, context-free
rules - that even experienced practitioners never graduate their
skill-level to this level of mastery. And he uses the [“Dreyfus model
of skill
acquisition”](https://en.wikipedia.org/wiki/Dreyfus_model_of_skill_acquisition)
to explain this key difference between novices and masters.

An agile master is not just someone who knows the minutia of various
agile practices. They are instead people who can draw on their
experience, situational awareness, and understanding of the context to
adapt or re-think processes where necessary.

# Resonates

And so as I think about the OpenStack community, these two insights
resonate with me.

If non-hierarchical collaboration is the ideal, what is it, and are we
achieving that ideal in OpenStack? If not, how can we get there? What
would the guiding principles for non-hierarchical contribution be?

And then, while we may want simple, context-free rules for newcomers
to the OpenStack community, how do we avoid getting stuck in the rut
created by these rules and processes. How do we ensure that members of
this community continuously increase their skill levels to go beyond
slavishly following these context-free rules, and instead have a
higher level of intuition and situational awareness about the
collaboration model we’re trying to achieve.

# Values

We, in OpenStack, have a manifesto of openness that we like to refer to:

1. Open Source
2. Open Design
3. Open Development
4. Open Community

and we also have these principles

1. The community controls the design process.
2. The technical governance of the project is a community meritocracy.
3. This will always be truly free software.
4. All project meetings are held in public IRC channels and recorded.

That’s all awesome, but they seem fairly basic. If I was to call out
some other things I value in an open community I’d say:

1. Diverse interests, but a shared vision, based on consensus.
2. “Individuals and interactions, over processes and tools”.
3. Leadership through empowerment, empathy, and trust.
4. Every advance must ultimately iterate from the bottom up. Baby steps.

I’m going to take each of those one at a time, and look at each value
through the lens of OpenStack, GNOME, and the Linux kernel. I’m
picking those because I’m familiar (or, at least, was intimately
familiar in the past) with GNOME and Linux because, well, everyone
loves to talk about the kernel.

## Diverse Interests, but a Shared Vision, Based on Consensus

We have an incredible diversity of interests in OpenStack. We have
contributors interested in compute, networking, storage, identity,
monitoring, orchestration, etc. We have people interested in
operations, developer infrastructure, testing, documentation, library
APIs, REST API design, and more. We have people interested in specific
use cases like public cloud, or private clouds in the enterprise, or
NFV. And we have people interested in integrating different
technologies behind our abstractions. With the arrival of the “Big
Tent” governance change, we’re now welcoming more and more interest
groups under the OpenStack umbrella.

The key to making such a diverse mix of interests is to walk the
balance between allowing different interest groups to work
independently, while also encouraging them to break out of their silos
and collaborate where joint effort is required for the success of the
project as a whole. We do pretty well at this in the sense that the
need for broad interest-spanning initiatives are needed.

What  I worry we’re stepping back from - or at least not pushing
aggressively - is areas where broad consensus across the project would
be beneficial. For example, the Integrated Release and the related
discussions about incubating and graduating projects, surfaced great
conversations about what the community vision for an OpenStack cloud
was. Not the minimal set of requirements for commercial
implementations of OpenStack, but rather an idealized vision for the
future of OpenStack clouds. Should an OpenStack cloud include an
orchestration API, a monitoring API, a messaging API? These
discussions are really tough, but building consensus is naturally
tough and that’s why we talk about “rough consensus and running
code”. If we run from these discussions, we run the risk of having no
shared vision for what we’re building.

With the integrated release gone, we must look for different avenues
for consensus building. Project tags may present some opportunity for
that, but we should think more creatively. Perhaps we could have an
upstream deployment tool with a set of reference architectures, and we
would build consensus into what goes into those reference
architectures? Or perhaps we put some governance in place for what
gets deployed in trystack.org so that it represents a community
consensus? Or ...?

In GNOME, the release team defines its mission as follows:

> The GNOME project is primarily united around a single effort -- the
> creation of the GNOME desktop experience. This effort focuses on a
> tightly-integrated desktop environment based on the GNOME Shell
> running on a GNU-based operating system with a Linux kernel. Above
> all else, our interest is to create a cohesive product. Uses of our
> technologies in other environments are welcome, but are considered
> secondary concerns.

It clearly states what the focus of the GNOME project is - that is a
tightly integrated desktop based on GNOME shell running on
Linux. Everything else is welcome, but secondary. Do you imagine this
consensus was easy to build? Far from it! But how awesome is it that
there’s a mission that can unite the project while still embracing a
wider diversity of interests. You can see that a version controlled
artifact is used to document the consensus, and that subjective
decision making criteria is also documented.

The work done under the GNOME Desktop umbrella is put to use in a
massively diverse set of use cases. Many applications and other
desktop environments are built on gtk+, there are many desktop
environments derived from GNOME, and you see devices like OLPC and
Endless Mobile heavily based on GNOME. All of that work is embraced in
different ways under GNOME, but yet the community can still build
consensus on a shared vision for things like what applications should
be included by default, to things like UX guidelines that say that OK
buttons should be avoided and the primary button in a dialog should be
on the right hand side.

In the kernel community, there is clearly a massive diversity of
interests. The many drivers, filesystems, subsystems, etc. are all
areas where developers can work in specialized silos. And clearly,
Linux is used in many diverse contexts.

However, and partly because all code lands in the one tree with Linux
making the final call, there actually is an awful lot of consensus
building going on. The kdbus patch isn’t going to be merged until and
unless some sort of consensus is reached, and that consensus is
arbitrated by Linus. The kdbus discussion is a good example of a very
broad subjective design discussion that is drawing input from a very
broad set of kernel contributors. It’s certainly not the case that
kernel developers can ignore everything going on outside their
individual silos if they want to be successful.

## “Individuals and interactions, over processes and tools”

I love this line from the Agile manifesto. It screams pragmatism. The
kind of pragmatism that is learned from painful experiences where a
focus on tools and processes completely took over from the task of
getting useful work done.

The thing is, we have plenty of tools and processes in OpenStack. We
love them. To implement a feature in OpenStack, you now have to file a
blueprint, write a spec, wait, work through much discussion about your
feedback, preferably your feature would be seen as a “project
priority” for this release, then you submit the code in gerrit once
the spec is improved, include the right tags in your commit message,
use the correct coding style, ensure that you have test coverage for
your feature and the tests are passing, then wait for someone to come
along and review it.

I think we have some great tools - gerrit, Zuul, etc. And I think
we’ve matured a lot as a community such that design decisions are
documented, we do test more of our code, we are diligent about code
reviews. But when it takes someone like Vish Ishaya months to get a
simple Nova networking bug fix merged, can we really say we favor
individuals and interactions over processes and tools?

As we talked about previously, if expert practitioners in our
community have the situational awareness and context to understand why
certain processes or tools exist, then those masters should feel
empowered to aggressively short-cut processes and tools where they
aren’t necessary to achieve the most desirable outcome in a particular
situation.

I’m going to avoid drawing any analogies to GNOME and Linux in this
context, because I think the next “value” actually has a lot in common
with this one.

## Leadership through empowerment, empathy, and trust.

In a non-hierarchical organization, leadership is not about control,
direction setting, rubber-stamping, and safeguards. Instead, it’s
about empowering people to achieve their potential. It’s about
empathizing with the interests, needs, and concerns of those around
you who have the potential to get useful stuff done. It’s about
trusting those people, safe in the knowledge that they are acting in
good faith and genuine mistakes can be recovered from.

In OpenStack, whether you know it or not, you are empowered. You can
absolutely join the OpenStack developer community and make a big
impact. I know this, because I did it. At my first design summit, I
was told directly by Thierry that a community maintained stable branch
for OpenStack was unworkable, and by Vish that OpenStack projects
would probably never standardize on a configuration file format. From
my perspective, I was entirely confident that I could persuade anyone
in the community of the value of both of these. They just needed
someone to step up and do the work, and I knew that could be me. I
didn’t need anyone to empower me, because I knew from experience that
a healthy open-source community didn’t need ideas like this to be
agreed upon by everyone in advance. When people hear “rough consensus
and running code”, they often put too much emphasis on the "consensus"
part whereas the "running code" part is equally important. If you show
up and do the work, someone better have a very good reason for getting
in your way.

The thing is, while I needed little in the way of empowerment, that’s
not true of most people. I had hoped to empower others by setting an
example. Once I showed through my own work how easy it is to get
useful work done, surely others would quickly follow that example?
I’ve since learned from other OpenStack leaders - like my good friend
Doug Hellmann - that empowering leadership can involve putting far
more work into setting up a structure and framework that really draws
people into contributing to useful efforts.

In many areas of OpenStack, our leadership’s empathy is reduced to an
all time low. My theory on this is that as the pressure piles on,
there’s a corresponding reduction in empathy. And make no mistake,
OpenStack leaders are under immense pressure.

Likewise, we often struggle to show the trust in each other that’s
appropriate in a non-hierarchical organization. To pick a random
example, the Neutron project wanted to experiment with a different
model for organizing its governance. My understanding is that the the
attitude from some TC members was “hell no, you can’t deviate from our
community norms”. I don’t have a strong view on the specific idea
proposed by the Neutron project, but I do feel strongly that projects
and individuals should be trusted to experiment with new
approaches. In Python, there’s a maxim called EAFP - “it’s easier to
ask forgiveness than permission” - but we don’t see an awful lot of
that OpenStack.

My first real encounter with open-source was when I contributed some
small patches to GNOME’s CORBA ORB. The maintainer of the project -
[Michael Meeks](https://people.gnome.org/~michael/) - asked me to go
ahead and commit them. When I explained I didn’t have a CVS account,
he said he’d chase down getting one created. [That evening his blog
said](https://people.gnome.org/~michael/blog/2001-06-18.html):

> Mark McLoughlin started sending me nice patches for ORBit2 - wow,
> what a hero, this is cool.

So, here was one of GNOME’s long-time project leaders, receiving some
tiny patches from a “nobody” and quickly giving him CVS commit access
to the entire GNOME CVS repository. It was clear to me that I should
only commit patches which I was confident of to this particular
project, and that Michael would be watching over my shoulder as I
committed changes. A couple of days later he asked me to ensure that
the tests were passing before I committed because they were currently
broken, but admitted that maybe the issue was his fault. Hours later
he followed up to apologize that the issue was indeed his
fault. Within a week, Michael was suggesting that I take over work on
what seemed to me to be a mind-bogglingly ambitious plan that he was
2/3rds finished with so that he could move on to something else. A few
weeks after those first patches, Michael officially made me a
co-maintainer of the project.

It’s hard to overstate how much of an impact this made on me as a
young university student about to graduate and start his first
full-time job. To be so quickly embraced by Michael as a peer that
believed I could do great things for the project was amazing. This is
what non-hierarchical, empowering, trusting leadership means to
me. It’s quite hard to define exactly what it is, but it’s a million
miles away from what I could have expected from starting to work on a
software project in a traditional, hierarchical organization. It’s
also sadly an awfully long way from what I expect most newcomers to
OpenStack experiences.

## Every advance must ultimately iterate from the bottom up

I believe that every advance in an open-source project starts with an
individual doing the work to push an idea forward. Perhaps it’s not
directly applicable, but I do like this quote:

> “Every revolution was first a thought in one man's mind” - Ralph
> Waldo Emerson

In OpenStack, the notion that our contributors can be directed from
some sort of central authority is increasingly gaining hold. One
particularly intriguing exchange in an email thread went as follows:

> "we don't have direct control over the contributors' activities"

> "OpenStack is not an amateurish project done by volunteers in their
> free time."

In one sense, the “amateurish” retort is simply a factual
statement. Most OpenStack developers are employed, so by definition
are not working in their free time. Ignoring the “amateurish” slur
against other projects, the fact is that employed or not, contributors
essentially are volunteering for different initiatives. To varying
extent, employers are directing the work of their employees, but as a
non-hierarchical organization, all contributors wind up looking very
much like volunteer contributors as they work on a project. Their time
cannot be counted on, they can not be ordered to ordered to follow a
certain direction, and they must be encouraged to continue their
contribution.

["Healthy communities operate on trust built between
individuals"](https://mail.openvswitch.org/pipermail/ovs-dev/2016-February/308952.html).

