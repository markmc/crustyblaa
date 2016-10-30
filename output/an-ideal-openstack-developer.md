Title: An Ideal OpenStack Developer
Date: 2014-06-06 14:49
Author: markmc
Category: openstack
Slug: an-ideal-openstack-developer
Status: published

*(This is a prose version of a talk I gave at OpenStack meetups in
Israel and London recently. Apologies for the wordiness.)*

In a recent update Jonathan gave to the Board of Directors, we described
how OpenStack has had 2,130 contributors to date and 466 of those are
active on a monthly basis. That’s an incredible statistic. There’s no
doubt OpenStack has managed to attract an unusual number of contributors
and, for such a complex project, made it relatively easy for them to
contribute.

However, this isn’t just a numbers game. I often hear mutterings that a
much smaller, focused group could achieve the same velocity that
OpenStack is achieving. In some sense that’s true, but I think that the
diversity of interests and priorities is the energy that a community
like OpenStack thrives on.

The question then is how to improve the overall quality of our large
number of contributors. In order to do that, we need to be able to set
expectations. What do we expect and value from our contributors?

What I’m going to attempt to do here is define The Prototypical
OpenStack Developer. The ideal that we should aspire to. The standard
that all contributors should be held to.

(But … bear with me here. I’m being a little tongue-and-cheek.)

Ok. Where do we start? How do we begin to forge this hero from the raw
resources we are presented with?

Let’s start with the basics. The breadth and depth of knowledge you need
on a variety of computing topics.

On **virtualization**, you could start with KVM. You should know about
CPU extensions such as Intel’s VT-x and I/O virtualization with VT-d and
PCI SR-IOV. Some knowledge of the history of software based
virtualization and paravirtualization would be nice context too. Now
understand the responsibilities of the KVM kernel module versus the
userspace component, qemu. How does qemu emulate various devices? How
does live migration work? How does a hypervisor use page table flags to
track dirty pages during a migration?

And there’s probably little point in understanding all of this without
understanding the x86 architecture in some detail. Understanding how it
compares to RISC architectures would be no harm. Memory segmentation,
MMUs, page tables are all fun topics. You really can’t get into this
without learning a bit of assembly, at least the basic idea. The history
of x86, from real/protected mode to modern day PAE or x86-64 are all
important to understand. Ignore Itanium, though. It’s not enough to just
understand the CPU, though, you need to go beyond and think about how
that CPU interacts with peripherals using DMA and buses like PCI.

And, honestly, if you go this far you may as well understand basic
digital systems theory, like how you can construct a counter or register
from a set of basic logic gates ...

Woah, I think I’ve digressed a little. That’s virtualization. Do the
same for **storage and networking**. I’ll leave that as an exercise for
the reader.

That’s just the concept behind the basic resources managed by OpenStack,
though. It’s a pretty complicated **distributed system**, so it’s pretty
essential you do some reading on that topic. What do terms like “quorum”
and “consensus” mean? Why do people describe the Paxos algorithm as
“quicksort of distributed systems”? What do people mean when they
describe OpenStack as a “shared nothing” architecture, and are they
crazy? How would you describe OpenStack’s approach to fault tolerance?

And obviously related to all of this is the need for deep knowledge of
**databases and messaging systems**. We seem to have a large number of
ex-MySQL consultants on this project, but don’t let that be an excuse.
You know what foreign keys and cross-table joins are, right? And you
really need to know the kind of operations which will simply lock
individual rows rather than an entire table. For messaging, there’s a
little research you can do there. We’re all about AMQP in OpenStack, but
there’s been a few other messaging protocols in the past. My personal
favorite is CORBA. What’s the difference between a broker, router and
peer-to-peer based architecture? What’s this “fanout” and “topic” things
we talk about in messaging? Incidentally, you know that we’re not
actually using the standard AMQP protocol in OpenStack, right?

You needn’t have touched a line of code at this point. But, if you’re
going to contribute to OpenStack, you need to code, right? Almost
certainly in **Python**, but we like ourselves a little Bash too. With
Python, it’s important to understand not just the syntax from the most
basic to the more advanced topics like iterators, decorators, context
managers and metaclasses. You also need to have a good knowledge of the
huge number of python libraries out there, inside and outside the core
Python distribution. We need true Pythonistas. Oh, and we’re in the
process of porting to Python 3, so make sure you understand the
differences between Python 2 and 3.

But wait, wait. That’s no good. You can’t just dive straight into
Python. You need to start with C. Allocate and free your own memory,
damnit. You can’t go through life without learning about pointers. Now
learn how to use threads and the various synchronization primitives out
there, and why it’s all just terrible. Now learn about asynchronous I/O
techniques; what an event loop is, how you use select() and non-blocking
sockets to write a single-threaded server which processes requests from
multiple clients. Oh, Richard Stevens. My hero. Don’t be afraid to read
a few RFCs.

Speaking of authors, we forgot algorithms. Yes, those. Just carefully
study all three volumes of Knuth.

Now, before returning to Python, perhaps you should implement a REST API
in Java using JAX-RS and a web UI using Ruby on Rails. Hang out with the
cool kids and port your UI to Sinatra, before realizing that’s not cool
anymore and switching to Node.js.

You might be ready to contribute some code to OpenStack at this point.
But, I hate to think of anyone writing software without having a full
appreciation of the **user experience design** we’re driving towards. We
don’t want the inmates running the asylum, do we? Which “personas” are
we designing for? “As a web developer, I want to launch a virtual
machine to test my code in.”

Wait, we forgot **tools**. You can’t get anything done without knowing
your tools. You’re going to do all of your work on Linux, whether that
be in VMs or by running Linux on your main machine. If you’re a serious
person, you need to learn emacs. You’re going to become very close
friends with grep and sed, so learn yourself regular expressions. Lazy
and greedy regexs, both. You know how to do a HTTP POST with curl,
right?

Ah, git! Oh, the glorious **git**! You can never learn too much about
git. It’s the gift that keeps on giving. If you think I’m joking, spend
some time getting to know interactive rebasing. Reordering, editing,
squashing and splitting commits! Re-writable history! Where have you
been all my life? No git detail is too obscure to ignore. Learn how a
tilde is different from a caret in revision parameters. How you can
delete branches by leaving out the first part of a refspec in a
git-push. Force override, exciting! Is your mind blown yet? No? Find out
how git’s reflog is a history of history!

(Give me a second to calm down, here)

Now, you’ve got to realize something. Based on everything you’ve learned
so far, you could probably write OpenStack on your own. But that’s not
what’s going on here. You’re **collaborating**. You’re following a
process. How we collaborate and why we follow certain processes is a
more complex, involved and undocumented topic than anything you’ve
learned so far.

To really understand how we get stuff done in OpenStack, you need to be
steeped in open source culture. Understand what we mean when we say
things like “rough consensus and running code” or “do-acry”.

Perhaps start by following the linux-kernel mailing list for a few
months, watching how controversial discussions are worked through and
the subtleties that determine who holds the balance of power and
influence. Don’t worry if you’re shocked and appalled by how unfriendly
it all seems, you’re not the first. If that’s your one take-away from
the kernel, that was time well spent. Now seek out friendlier
communities and understand how they get stuff done. Compare them to
OpenStack and ask yourself questions like “how does our reliance on
voting to make decisions compare to other communities?” or “why does
there seem to be less flamewars in OpenStack than elsewhere?”.

The history of open source is important, will inform how you engage with
OpenStack and that, in turn, will influence how OpenStack evolves. Learn
about the “free software” versus “open source” camps, and how those
**philosophies** relate to the choice of copyleft licenses like the GPL
versus permissive licenses like Apache, MIT or BSD. Are you in this for
the freedom of users of your code, or are you in it to build
collaborative software development communities? That contributor
agreement you were asked to sign before you contributed to OpenStack -
how do you feel about that?

Think about the different **governance models** that open-source
communities adopt. Learn about benevolent dictators, project management
committees, “commit bit”, consensus based decision making and the pros
and cons of our representative democracy model.

Learn about the **release processes** various projects use. Time based
versus feature based. Rapid release cycles with merge windows. Planning
periods, feature freezes, release candidates, stable branches. How do
different distros do this when there are so many maintainers and
packages involved? We use Python a lot, how do they coordinate their
release cycles?

That’s all very well, but it’s important not to be blind to the **world
outside** open source. Understand how extreme programming and agile
software development evolved. Read the Agile Manifesto. Understand how
this all relates to Continuous Integration, Continuous Delivery and
DevOps. We’re operating in a much different context, but is code review
our variant of XP’s pair programming? Is our gated master superior to
traditional post-commit CI?

You can now consider educated to a basic level. But is that enough to be
an effective contributor? Do you now have everything you need to make an
impact? No, far from it. The hardest part is learning to be a **good
human**. You need to have superb communication skills, in English of
course, mostly written communication skills for mailing list, gerrit and
IRC discussions. We do meet twice a year in design summits, so you need
to be able to present and defend your ideas in person too. You need to
work on that Irish mumble of yours.

More than that, though, you need to understand people. You need to know
when to be empathetic, when to be pragmatic and when you be dogmatic.
When is someone’s -1 on your patch likely to be an intractable veto and
when is it simply a take-it-or-leave-it suggestion? What fights are
worth fighting? How can you build up kudos points by assisting your
fellow contributors and when is the right time to call in some favours
and spend those kudos points?

Ok, we’re ready to go! How do we **put all of this into practice**?

Probably the best way to start contributing to the project is by doing
**code reviews**. You should probably be spending at least a couple of
hours on code review every day. Not just because the number of code
reviewers on a project has the greatest influence on its velocity, but
also because its the best way to start building trust with your fellow
contributors. If you can show yourself as thoughtful, committed and
diligent through your code reviews, then other code reviewers will be
much more inclined to prioritize your patches and less carefully
scrutinize your work.

A good code reviewer manages to simultaneously focus on the little
details while also considering the big picture. Try not to just leave +1
on patches, but instead a little commentary that shows the kind of
things you’ve taken into consideration. Why should anyone trust that
your +1 was the result of 2 hours of careful analysis, research and
testing rather than just 2 minutes of coding style checking?

Also, think about who you are building up trust with. As a new code
reviewer it’s probably more fruitful to provide helpful input on some
meaty patches from some of the lead developers on the project. Then
again, patch triage can be hugely helpful too - catch obvious problems
in patches before the core reviewers ever get to the patch. Don’t forget
to mentor new contributors as a code reviewer, though. Code review is
the face of the project to these contributors and its your opportunity
to show how you can lead by example.

Now, you obviously want to **contribute code**. Find some gnarly bug to
fix, perhaps some race condition only rarely seen during automated
tests. With all the code reviewing you’ve been doing, you’ve acquired
excellent taste in coding and your work will no doubt live up to those
standards. Don’t forget to write a detailed, helpful commit message and
include a unit test which would catch any regression of the issue. If
this is a more substantial change, you must split your change into
smaller chunks where each patch represents a logical step in your
progression towards the final result.

If you’re making a substantial addition like a new feature or a
re-architecture, you need to document your design in some detail in a
blueprint. Make sure someone reading the spec can quickly understand the
problem you’re trying to solve, why it’s important and the general idea
behind your solution. Then make sure there’s enough background
information included that a reviewers work is made easy. Include the use
cases, any relevant history, related discussions or bugs, alternative
approaches considered and rejected and any security, upgrade,
performance or deployer impact. Describe how your work will be tested
and what documentation changes will be required.

While we’re on the subject of blueprints, don’t forget that these too
need reviewers. Most projects now review the specs associated with
blueprints using gerrit and so this is a way for you to demonstrate your
design skills and catch things which no-one else has yet considered.

Back to code, though. Yes, it’s important to contribute to the various
integrated service projects like Nova, Neutron, Swift and whatnot.
However, there are a bunch of other areas where code contributions are
always needed. For a start, the client projects are always forgotten.
Then there’s the cross-project technical debt that the Oslo program is
hard at work cleaning up. We’re also gradually porting all of OpenStack
to Python 3, and this is going to be a multi year effort requiring the
help of many.

We also place a huge emphasis on automated testing in OpenStack, and the
awesome CI system we have doesn’t come from nowhere. You should always
be ready to jump in a contribute to the infrastructure itself, tools
like devstack-gate, zuul, nodepool or elastic-recheck. And, last but not
least, our functional test suite, Tempest, is always desperately in need
of more contributions to increase our test coverage.

**Security** is critical in a public-facing service like OpenStack, and
there are several ways you should contribute in this area. Firstly,
there is a small vulnerability management team which collaborates with
each project’s -coresec team to handle privately reported security bugs,
ensuring a fix is prepared for each supported branch before a
coordinated, responsible disclosure of the issue first to vendors and
then the wider world. Important work is this. There’s also a security
group which is trying to bring together the efforts of interested
parties to prepare official notices on security issues that aren’t
actual vulnerabilities, develop a threat analysis process for OpenStack
and maintain the OpenStack Security Guide. They need your help! Most
importantly, though, you need to be security conscious as you write and
review code. There’s a good chance you’ll find and report an existing
vulnerability during the course of your work if you keep your eyes open!

And then there’s **docs**, always the poor forgotten child of any open
source project. Yet OpenStack has some relatively awesome docs and a
great team developing them. They can never hope to cope with the
workload themselves, though, so they need you to pitch in and help
perfect those docs in your area of expertise.

I mentioned **bugs**. We must not forget the bugs! Bugs are one way
users can provide valuable contributions to the project, and we must
ensure these contributions are valued so that users will continue to
file bugs. With over 700 configuration options in Nova alone, the
project can’t possibly test all possible combinations by itself so we
rely on our users to test their own use cases and report any issues as
bugs. You should help out here by setting aside some time every day to
triage new bugs, making sure enough information has been provided and
the bug has been appropriately tagged, categorized and prioritized.

Along those same lines, **users** often struggle with issues with aren’t
obviously or necessarily bugs. You should also pay attention to forums
like ask.openstack.org or the openstack-operators mailing list. Any
outreach you can do to help users be successful with OpenStack will pay
massive dividends in the long run, even just in terms of your
understanding which issues are most important to real users. This
outreach should extend to your attending OpenStack meetups, giving
presentations on your work and listening to what users have to say.

Speaking of mailing lists, we have a hugely active **openstack-dev
mailing list**, with over 2500 emails in April alone. This is the center
of all activity happening in OpenStack at any time. You really must
track what’s happening there and engage where you can help move things
forward positively. It’s a struggle to keep up, but it really isn’t an
option.

However, one of the side effects of openstack-dev being overloaded is
that many important conversations now happen **IRC**. You can’t expect
to be around for all of those, so make sure to remain connected and log
all channels so you can catch up later.

Because conversations can be spread around multiple places, it can be
helpful to link all of these conversations with little breadcrumbs. A
mailing list thread might reference a gerrit review, which might
reference a log of an IRC conversation, which might reference a blog
post, which might reference a bug, which might reference a previous
commit message which referenced a previous mailing list thread.

Don’t be fooled into thinking IRC is all about the serious stuff,
though. It’s also a place where you can get to know your fellow
contributors on a personal level and build up yet more of that all
important trust. You will make friends working on OpenStack and some of
those **friendships** will last longer than your involvement in
OpenStack itself. That’s a hugely positive sign in any community. Beware
of forming cliques, however. We need this community to be open to the
most diverse set of contributors, and not all of those will buy into
US-centric young white male geek humour, for example.

Speaking of cliques, it’s popular to accuse OpenStack developers on
being so self-absorbed that the needs of real operators and users are
ignored. That OpenStack developers aren’t held responsible for the real
world consequences of the decisions they make. “You write code
differently when you carry a pager”. Lorin Hochstein proposed an “Adopt
a Dev” program where operators could invite individual developers to
shadow them for a few days and share their experience in the terms of a
summary, bug reports and blueprints. Basically, you should take any
opportunity you can to get your hands dirty and help **operate a
production OpenStack service**.

Related to the needs of operators are the deployment, configuration and
**operational tools** out there which desperately need contributions
with people more familiar with the dirty details of how the software
works. Many developers use devstack to deploy their development clouds,
but there’s huge benefit in occasionally deploying something more
production-like and contributing to whatever tool you used. TripleO is a
great deployment effort to contribute to because it’s attempting to
create a space where everyone interested in deployment can collaborate,
but also because it closely tracks the development branch of OpenStack.

Once you have succeeded at making an impact as an individual
contributor, you should look to extend your **leadership** efforts
beyond simply leading by example. Naturally, you’ll tend towards
volunteering for the responsibility of the PTL position on whichever
program you contribute most to. To demonstrate your willingness and
trustworthiness for the position, perhaps you’ll suggest the PTL
delegate some of their responsibilities to you.

Your leadership interests should extend beyond a single project too. In
some ways, the kind of cross-project issues considered by the
**Technical Committee** are as important as the per-project
responsibilities of PTLs. Do you have strong opinions on how, why and
when should add new programs or Integrated projects. If not, why not?

The governance of OpenStack and the shared responsibility for the future
direction of OpenStack extends beyond the TC and PTL’s governance of the
project itself, to the role of the **Foundation Board of Directors** in
protecting, empowering and promoting the project as well as ensuring
there’s a healthy commercial and non-commercial ecosystem around the
project. Do you care how the TC and board divide their responsibilities?
Or how much explicit corporate influence is appropriate in the technical
decision making of the project? Or how the board makes legal decisions
which directly impact the project? Or how individual members elect their
representatives on the board? You should.

Wait, wait, I’m forgetting a bunch of stuff. You should care deeply
about bringing contributors on board and participate in the awesome OPW
and GSoC programs. It’s important to keep track of how the project is
perceived, so you should read any articles published about the project
and follow even our worst detractors on twitter. Watch carefully how our
major competitors like AWS and GCE are evolving. Make sure to keep on
relevant new developments like NFV or Docker. Keep an eye on new
projects on Stackforge to track how they develop.

Huh, wait. You’re probably **employed** to work full time on the
project, right? Well, you really need to learn how to wear upstream and
downstream “hats”. You need to understand how you can help your employer
be successful with their objectives around the project. You need to be
able to reconcile any apparent conflicts between your employers’ needs
and the best interests of the project. This is not a zero sum game. Meet
with your employer’s customers and partners, help deliver what OpenStack
product or service your employer is providing, mentor colleagues on how
to successfully engage with the project and be the bridge over the
upstream and downstream gap.

Above all, through all of this, be nice to everyone you encounter and
wear a smile.

**BZZZT … BURNOUT ALERT**

I’m obviously being facetious, right? There’s no way anyone can possibly
live up to those expectations and live to tell the tale?

It’s pretty obvious when you put it all together like this that these
are unreasonable expectations. The hero of this tale does not exist.
Many of us have tried to be this person, but it’s just not possible.
Read into this, if you like, a very personal tale of burnout caused by
unreasonable self-imposed expectations.

But really, what I want to get across today is that you don’t need to be
this hero in order to contribute. Far from being too many active monthly
contributors, five hundred is just the tip of the iceberg. Why shouldn’t
every attendee of every OpenStack meetup be able to contribute in some
small way?

When mentoring new Red Hat engineers, my basic advice is always “find
your niche”. Find something that takes your interest and that you can
see an obvious path towards making a significant impact, and go deep!
Ignore pretty much everything else and do your thing. Maybe after a
while you’ll have got the ball rolling of its own accord and that there
are other areas you can now make an equally big impact on. Or perhaps
you’ll stick with this niche and continue to make an impact doing it
over the longer term.

One of my favorite examples of a less likely niche is bug triage. Back
in the summer of 2001 when I started seriously contributing the GNOME
project and became a maintainer of its CORBA ORB, ORBit, another new
contributor to the project called [Luis Villa posted this
email](https://mail.gnome.org/archives/gnome-bugsquad/2001-June/msg00004.html):

> Hey, everybody. By way of introduction: I'm the new bugmaster at
> Ximian. As some of you may have noticed, I'm slowly moving towards
> cleaning out evo and RC bugs from bugzilla.gnome and into
> bugzilla.ximian.

Luis went on to breath new life into GNOME’s “bugsquad”, helped put in
place a highly effective bug triage process and taught the GNOME
community how to truly value and celebrate the contributions of both bug
reporters and bug triagers. If you want to make fame and fortune in the
open source world, how many people would pick bug triage as the place to
start? Well, Luis did and made a huge impact, before moving on to
engineering management and then giving it all up to go to law school. He
is now Assistant General Counsel for the Wikimedia Foundation.

There’s a real “find your niche” lesson in that story, but also a lesson
that we as a community need to learn to truly value and celebrate all of
the myriad of different ways that contributors can help the project.
Rather than judge others based on how they’re not contributing, rather
than feel exasperated when so few others share your passion for a
particular niche no matter how important it seems to you personally, we
as a community need to acquire a greater level of empathy for our fellow
contributors.

We also need to experiment with ways of running the project so that
different roles and niches are appropriately recognized. Does the focus
we put on PTLs detract from the valuable project management
contributions others make? Are official programs the only way of
recognizing the importance of particular areas? If programs are the only
way, do we need to be more open to creating programs wherever a group of
people have coalesced around some particular effort? Do we need to
explicitly raise the profiles of those contributors doing hard
behind-the-scenes work in areas that we don’t typically recognize? Are
we building a culture that places too much emphasis on recognition and
instead roll back some of the ways we recognize people now?

Lot’s of questions, few answers. But hopefully this can get the
conversation started.
