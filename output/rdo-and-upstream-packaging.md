Title: RDO and Upstream Packaging
Date: 2015-06-12 12:27
Author: markmc
Category: fedora, openstack
Slug: rdo-and-upstream-packaging
Status: published

Derek mentioned "upstream packaging" on [this week's packaging
meeting](http://meetbot.fedoraproject.org/rdo/2015-06-10/rdo.2015-06-10-15.00.html)
and asked RDO packagers to participate in the upstream discussions. I
thought some more context might be useful.

First, a little history ...

When I first started contributing to OpenStack, it
[briefly](https://review.openstack.org/708) looked like I would need to
make some Ubuntu packaging updates in order to get a Nova patch landed.
At the Essex design summit a few weeks later, I raged at Monty Taylor
how ridiculous it would be to require a Fedora packager to fix Ubuntu
packaging in order to contribute a patch. I was making the point that
upstream projects should leave packaging to the downstream packaging
maintainers. Upstream CI quickly moved away from using packages after
that summit, and I've heard Monty cite that conversation several times
as why upstream should not get into packaging.

Meanwhile, Dan Prince was running the Smokestack CI system at the time,
which effectively was being treated as OpenStack's first "third party
CI". Interestingly, Smokestack was using packages to do its deployment,
and for a long time Dan was successfully keeping packaging up to date
such that Smokestack could build packages for patches proposed in
gerrit.

And then there's been the persistent interest in "chasing trunk".
Operators who want to practice Continuous Deployment of OpenStack from
trunk. How does packaging fit in that world? Well, the DevOps mantra of
doing development and CI in environments that model your production
environment applies. You should be using packaging as early on in your
pipeline as possible.

My conclusion from all of that is:

1.  A key part in building a Continuous Delivery pipeline for OpenStack
    is to practice continuous package maintenance. You can glibly say
    this is "applying a DevOps mindset to package maintenance".
2.  How awesome would it be if OpenStack had "upstream infrastructure
    for downstream package maintainers". In other words, if downstream
    package maintainer teams could do their work close to the upstream
    project, using upstream infrastructure, without disrupting
    upstream development.

I think the work that Derek, Alan, Dan, John, and everyone else has been
doing on Delorean is really helping RDO maintainers figure out how to
practice (1). I first started maintaining Fedora packages for Fedora
Core 2, so IMO what RDO is doing here is really dramatic. It's a very
different way of thinking about package maintenance.

As for (2), this where we get back on topic ...

At a [Design Summit session in
Vancouver](https://etherpad.openstack.org/p/YVR-ops-packaging), the idea
of maintaining packaging using upstream infra really took hold. Thomas
Goirand (aka zigo) [proposed the creation of a "distribution packaging"
team](https://review.openstack.org/185187) and this triggered a [healthy
debate on
openstack-dev](http://lists.openstack.org/pipermail/openstack-dev/2015-June/thread.html#65545).
Derek has since pushed [a WIP patch showing how RDO packaging could be
imported](https://review.openstack.org/189497).

There's a clear desire on the part of the Debian and Ubuntu package
maintainers to collaborate on shared packaging, and it sounds like this
goal of further collaboration is one of the primary motivators for
moving their packaging upstream. This makes a lot of sense, given the
shared heritage of Debian and Ubuntu.

The RDO team is enthusiastic about adopting this sort of upstream
workflow, but the Debian/Ubuntu collaboration has added an entirely new
aspect to the conversation. Despite the fact that RDO and SUSE platforms
have little in the way of shared heritage, shouldn't the RDO and SUSE
packaging teams also collaborate, since they both use the RPM format?
And perhaps deb and rpm maintainers should also collaborate to ensure
consistency?

To my mind, the goal here should be to encourage downstream packaging
teams to work closer to the upstream project, and have downstream
packaging teams collaborate more with upstream developers. This is about
upstream infrastructure for downstream teams, rather than a way to force
collaboration between downstream teams, simply because forced
collaboration rarely works.

For me, what's hugely exciting about all of this is the future prospect
of the package maintainers for different platforms adopting a
"continuous packaging" workflow and working closely with project
developers, to the extent that packaging changes could even be
coordinated with code changes. With its amazing infrastructure,
OpenStack has broken new ground for how open-source projects can
operate. This could be yet another breakthrough, this time demonstrating
how a project's infrastructure can be used to enable an entirely new
level of collaboration between package maintainers and project
developers.

 

 

 
