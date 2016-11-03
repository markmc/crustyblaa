Title: The Future of Incubation and Core
Date: 2012-11-17 17:53
Author: markmc
Tags: OpenStack
Slug: the-future-of-incubation-and-core
Status: published

The [OpenStack Technical
Committee](http://www.openstack.org/foundation/technical-committee/) and
the [OpenStack Foundation Board of
Directors](http://www.openstack.org/foundation/board-of-directors/) have
pretty separate sets of responsibilities and can get on with their work
independently. One exception to that is the inclusion of new projects in
OpenStack.

In the coming weeks, members of the two bodies will decide how to
clarify confusion around the term "core project" and what exactly
happens projects who graduate through OpenStack's Incubation process.

A [thread on the openstack-dev mailing
list](http://lists.openstack.org/pipermail/openstack-dev/2012-November/thread.html#2387)
is ongoing and is a great example of how a mailing list discussion can
actually help to drive a rough consensus while still giving everyone an
opportunity to express their views.

The TC is attempting to agree on a rough direction that represents the
views of the TC before meeting with the Foundation Board. There are
currently three distinct views. Firstly,
[this](http://lists.openstack.org/pipermail/openstack-dev/2012-November/002771.html):

> The concepts of "what is core" and "what is in OpenStack" have been
> conflated until now. The TC cares far more about the process for new
> projects to be included in the coordinated release than it cares about
> which projects are required to be used by providers in order to access
> the trademark.
>
> We would like to take an inclusive but measured approach to accepting
> new OpenStack projects. We should evaluate any given proposed project
> on a well defined set of criteria like whether it embraces our values
> and processes, is useful to OpenStack users, well integrated with
> other projects and represents a sensible broadening of the scope of
> OpenStack.
>
> We see Incubation as a trial period where promising projects have the
> opportunity to demonstrate their suitability for inclusion in our
> coordinated releases.
>
> We see the term "Core OpenStack Project" in section 4.1.b of the
> bylaws as being solely related to trademark guidelines. The Foundation
> should simply maintain a list of projects required for trademark
> usage. We would be happy for that list to be called "Core Projects" or
> for a new name to be chosen to describe that list.

Secondly, [Anne Gentle's
variation](http://lists.openstack.org/pipermail/openstack-dev/2012-November/002956.html)
which I'd summarize as allowing two groups of projects be accepted into
OpenStack - "nuclear" projects which are the current group of "core"
service projects and "core" projects which are everything else, for
example Horizon, Ceilometer or Heat.

Thirdly, [John Dickinson's
variation](http://lists.openstack.org/pipermail/openstack-dev/2012-November/002954.html)
which I'd summarize as only accepting projects into OpenStack which
"solve IaaS problems" or support those projects in some way.

The way I'm thinking of these three approaches is how we want the
project to treat proposals for new projects: "inclusive", "inclusive but
two-tier" or "exclusive".
