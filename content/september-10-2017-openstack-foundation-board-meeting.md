Title: September 10th OpenStack Foundation Board Meeting
Date: 2017-09-14 11:00
Author: markmc
Tags: OpenStack, OpenStack Foundation Board Meeting
Slug: september-10-2017-openstack-foundation-board-meeting
Status: published

The [OpenStack Foundation met in Denver on September 10th for a Joint
Leadership
Meeting](https://wiki.openstack.org/wiki/Governance/Foundation/10Sep2017BoardMeeting)
involving the foundation Board of Directors, the Technical Committee,
and the User Committee.

The usual disclaimer applies - this my informal recollection of the
meeting. It’s not an official record.

## Foundation Events Update

We began with an update from Lauren, Jonathan, and Mark on the events
that have happened so far this year, the Project Teams Gathering (PTG)
in Denver this week, and the coming OpenStack Summit in Sydney.

Lauren outlined some details of the recent Pike release, emphasizing
the positive media coverage of the release, with the ["composable
infrastructure
services"](https://www.openstack.org/news/view/340/openstack-pike-delivers-composable-infrastructure-services-and-improved-lifecycle-management)
messaging resonating.

Jonathan talked about the many OpenStack Days events that happened
over the summer, including Melbourne, Tel Aviv, Budapest, Korea,
Taiwan, Japan, and China. Jonathan has attended all of these, covering
13 countries since the OpenStack Summit in Boston and he spoke about
the many new users and new use cases that he learned about over the
course of these events. [More OpenStack Days are
coming this
year](https://www.openstack.org/community/events/openstackdays)
including Benelux, UK, Italy, Turkey, Nordic, Canada, France, and
Germany.

Mark spoke about the [OpenDev event](http://www.opendevconf.com) held
the previous week in San Francisco. The goal was to bring in people
who are experts in different domains, and the important and emerging
use case of "Edge Computing" was chosen for this first event. The
keynote from [Dr Satya of Carnegie Mellon
University](https://www.cs.cmu.edu/~satya/) was mentioned as one
particularly inspiring contribution.

An particularly interesting conclusion from [one of the
sessions](https://etherpad.openstack.org/p/Deployment_Considerations__Hardware_options)
was a simple definition of what Edge Computing actually is:

> Edge is the furthest boundary that separates application-agnostic
> scheduled computing workloads within the same operator's domain of
> control, from applications or devices that can't schedule workloads,
> and are outside the same operator's control.

(Thanks to Dan Sneddon for pointing this out!)

Another interesting development is [the collection of edge use
cases](https://etherpad.openstack.org/p/opendev-sf-use-cases) which
will be published to [Edge Computing mini-site on
openstack.org](https://www.openstack.org/edge).

The [PTG](https://www.openstack.org/ptg/) was touched on next - more
than 400 contributors in attendance from 35 project teams, with the
first two days focused on the strategic goals of simplification,
adjacent technologies, onboarding new contributors, etc.

Jonathan also talked about the coming [OpenStack Summit in
Sydney](https://www.openstack.org/summit/sydney-2017/). We are aiming
for 2500+ attendees, and the amazing work by the program committee to
work the 1100 speaking submissions into an awesome three day schedule
has been completed. There will be [Hackathon focused on Cloud
Applications](http://hackathon.openstack.org.au/) the weekend before
the event.

Finally, we looked forward to the OpenStack Summits in [Vancouver in
May](https://www.openstack.org/summit/vancouver-2018/), and [Berlin the
following November](https://www.openstack.org/summit/berlin-2018/).

## The Strategic Focus Areas

Back in March, at the [Strategic Planning Workshop in
Boston](https://crustyblaa.com/march-8-2017-openstack-foundation-strategic-planning-workshop.html),
we developed a set of 5 strategic focus areas and formed working
groups around each of these. For each of those focus areas, the
working group presented their findings and progress, followed by some
discussion.

### Better communicate about OpenStack

Thierry Carrez and Lauren Sell lead the discussion of this topic with
[a set of
slides](https://docs.google.com/presentation/d/1qQ1oCjhEE3bjtjkPydGhyeR6vFyuyFeOhbwc-WueddI).

We began by discussing progresson developing a map of OpenStack
deliverables. The idea is for the map to make it easy for users of the
software to make sense of what OpenStack has to offer, and one key
part of this mapping effort is to categorize deliverables into
buckets:

- openstack-user: Things an end user installs to consume the IaaS
  stack
- openstack-iaas: Primary compute, storage & networking services
- openstack-operations: Things an operator uses to manage an openstack
  cloud once installed
- openstack-lifecyclemanagement: Things that help deploy/upgrade
  OpenStack or standalone components
- openstack-adjacentenablers: Things that other infrastructure stacks
  can use to leverage individual OpenStack components

Some of the outstanding questions include how to represent projects
which are coming down the line, where various types of plugins should
live, and whether Glance is tied to Compute or should be represented
as a Shared Service.

After the meeting, [Lauren sent out a
request](http://lists.openstack.org/pipermail/foundation-board/2017-September/000376.html)
for everyone to [contribute their
feedback](https://etherpad.openstack.org/p/map-feedback) on the draft
of the map. Please do join in!

Next, we discussed at some length how OpenStack has been affected by
"Big Tent" concept where we welcome collaboration, experimentation,
and innovation on "infrastructure things" beyond the core OpenStack
technology. We've know that users have found it difficult to make
sense of the breadth of project teams, and we have created further
confusion around "what is OpenStack".

Our discussion on this revolved around the idea of separating the
technologies directly related to the deliverables map above (which we
could call "OpenStack IaaS and friends"), the ["software forge"
infrastructure project](https://docs.openstack.org/infra/), and the
free-for-all project hosting area previously known as
Stackforge. There was broad consensus that we should give each of
those its own identity, which is particularly exciting when you think
of the potential for "Infra" to have an identity that isn't so closely
tied with OpenStack. We also discussed the potential to extend this
model to other projects in the future, but also our desire to not
become a "Foundation of Foundations" or a collection of entirely
unrelated projects.

### Requirements: Close the feedback loop

Melvin Hillsman and Thierry Carrez talked us through the [unanswered
requirements strategic focus
area](https://docs.google.com/presentation/d/1vjGm5OzjVvtbhf_WUyKN3nvYGpB_hDTJEzMAwvgLd1I).

The focus of this discussion was on the creation of [OpenStack Special
Interest Groups
(SIGs)](https://wiki.openstack.org/wiki/OpenStack_SIGs) as a mechanism
to have cross-community collaboration on a given topic, without the
work being under the umbrella of any one governance body.

The SIGs created so far are:

- a Meta SIG to discuss how to improve SIG processes
- an API SIG, which is an evolution of the [API Working
  Group](https://wiki.openstack.org/wiki/API_Working_Group) already
  formed, and
- a still-forming Ansible SIG, with the goal of facilitating
  collaboration between Ansible and OpenStack projects.

### Community Health

On this topic, Steve Dake talked us through some efforts to help grow
the next generation of leaders in the OpenStack community, supporting
people who wish to become a core contributor or PTL. Steve
particularly highlighted efforts along these lines within the Kolla
project.

### Increase complementary with adjacent technologies

Steve Dake again took the lead on [presenting this
topic](https://docs.google.com/presentation/d/1iF09E1LTil55sLzncWIyS9WvRK-L_4Gp975mWQ53sis),
focusing on success stories of collaboration between OpenStack and
other communities - Ansible and Helm, in particular.

For Ansible, it was observed that OpenStack has built upon Ansible's
highly reusable technology in many ways, and OpenStack members have
contributed significantly to the Ansible modules for OpenStack based
on Shade. The conclusion was that the success was down to (a)
building releationships between the communities, (b) leadership
endorsement, and (c) the simplified collaboration process adopted by
Ansible.

For Helm, the collaboration has been focused in areas where Helm is
being used to deploy OpenStack services on Kubernetes.

Finally, Dims gave a read-out on collaboration on OpenStack within the
Kubernetes community, mostly with work in the [OpenStack
SIG](https://github.com/kubernetes/community/blob/master/sig-openstack/README.md)
focused on [the OpenStack cloud
provider](https://github.com/kubernetes/kubernetes/blob/master/pkg/cloudprovider/providers/openstack/openstack.go).

### Technology changes: Simplify OpenStack

For our final strategic focus area, [Mike Perez gave an
update](http://www.scaryland.net/complicated.pdf) on progress. He
described projects which have recently been retired, the OpenStack
manuals project migration, and the status of a number of projects who
are seeing low levels of contribution activity.

## Clarifying and communicating where help is needed

Next up, Thierry walked us through the TC's mechanism for exposing
areas where help is needed in the community. We talked through this
["top 5 help wanted
list"](https://governance.openstack.org/tc/reference/top-5-help-wanted.html)
and had a good discussion on the two items currently on the list -
Documentation and Glance.

## Interoperability Working Group

As our final topic, Egle Sigler gave an update from [Interoperability
Working
Group](https://docs.google.com/document/d/1CZxF-DL9CaxX9ab3Rd_IAqDzV-R_M8TCm1RwmQ_Emd4/).

The first item of business was to [approve the 2017.09
guideline](https://review.openstack.org/502328). Both the compute and
object components gained some new capabilities in this update.

[As discussed in the previous
meeting](https://crustyblaa.com/june-20-openstack-foundation-board-meeting.html),
the working group proposed the creation of "add-on" programs which
would focus on interoperability between different implementations of a
given service, without having to add that service as a requirement in
the core OpenStack Powered programs. As a starting point, it was
proposed to create advisory add-ons for [DNS
(Designate)](https://review.openstack.org/492635) and [Orchestration
(Heat)](https://review.openstack.org/#/c/490648/). After some
discussions on the implications of these additions, they were formally
approved by the board.

## Next Meeting

The board's next meeting is a 2 hour conference call on [Tuesday,
October
10](https://wiki.openstack.org/wiki/Governance/Foundation/10Oct2017BoardMeeting). Our
next in-person meeting will be in [Sydney on Sunday, November
5](https://wiki.openstack.org/wiki/Governance/Foundation/5Nov2017BoardMeeting).


