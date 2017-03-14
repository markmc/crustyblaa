Title: March 8, 2017 OpenStack Foundation Strategic Planning Workshop
Date: 2017-03-14 07:00
Author: markmc
Tags: OpenStack, OpenStack Foundation Board Meeting
Slug: march-8-2017-openstack-foundation-strategic-planning-workshop
Status: published

The OpenStack Foundation Board of Directors [met in-person for two
days](https://wiki.openstack.org/wiki/Governance/Foundation/8Mar2017BoardMeeting)
in Boston last week.

The first day was a joint workshop with the Technical Committee, User
Committee, and Foundation staff. The workshop was planned in response
to the "OpenStack Futures" discussion at our three previous board
conference calls in
[November](https://crustyblaa.com/november-17-openstack-foundation-board-meeting.html),
[December](https://crustyblaa.com/december-6-openstack-foundation-board-meeting.html),
and January.

## Introductions

We began the workshop with very brief personal introductions, followed
by Alan, Thierry, and Edgar giving an overview of the roles and
responsibilities of the Board of Directors, the [Technical
Committee](https://docs.google.com/presentation/d/17U3Lf83nKrhfqT0HLr3gq5xqQmwUFcW28OcfUrS1n3E),
and the [User
Committee](https://docs.google.com/presentation/d/1dsRa35TaqeiSrB-n76pj2jONBnWW_-L1UryEbT1vqNE).

## State of the Union

Next, [Mark Collier presented his view of the state of
OpenSack](http://lists.openstack.org/pipermail/foundation/attachments/20170313/73838d4b/attachment-0003.pdf),
with a particular emphasis on [the four areas planned for discussion
during the
day](https://etherpad.openstack.org/p/ocata-strategic-review-board). Mark
began by talking about the exciting opportunity we had by having such
breadth and depth of expertise in the room, and appealed to everyone
to put aside their particular roles and work together as a single
leadership team to talk about the work.

### Evolving The Architecture

Mark spent some time trying to demystify the Big Tent change,
describing how the previous Stackforge/Incubation/Integrated stages
have been replaced by almost any project being welcome to use
OpenStack infrastructure with the TC responsible for reviewing
applications to join the set of official OpenStack projects known as
"The Big Tent".

Mark then described one of the key changes happening in OpenStack
right now as the containerization of the control plane, with projects
like Kolla, openstack-helm, and TripleO all tackling this area. He
also talked about the work happening around running containers on
OpenStack itself with projects like Kuryr, Fuxi, Magnum, and Zun, but
he also wondered aloud whether we're addressing all the right
integration points. He also described some of the ongoing debates
about the scope of OpenStack and our technology choices, with topics
like the use of golang, the Gluon project, whether we welcome
competition within the Big Tent, and community-wide goals.

Finally, Mark gave us a preview of the work happening around version 2
of the [OpenStack Project
Navigator](https://www.openstack.org/software/project-navigator/) and
talked about how this will play a key role in helping people
understand what OpenStack provides and how it can be used.

### Unanswered Requirements

Mark talked briefly about the [working groups under the User
Committee](https://wiki.openstack.org/wiki/Governance/Foundation/UserCommittee)
and the transition from Design Summit to [Project Team
Gathering](https://www.openstack.org/ptg/) and
[Forum](https://wiki.openstack.org/wiki/Forum) formats. These concepts
are all important in understanding how OpenStack thinks about our
requirements gathering, strategic long-term planning, and
implementation planning.

Mark also gave a preview of some detractor quotes from our user
survey, and emphasized a common theme - the perceived and actual
complexity of OpenStack, both in terms of understanding and operating
the software.

### Adjacent Communities

Mark classified the various sets of adjacent communities that we are
particularly interested in developing strong relationships
with. Container technologies like Kubernetes, Docker, and Mesos. PaaS
technologies like CloudFoundry and OpenShift. NFV projects like OPNFV
and Cloudify. Provisioning technologies like Terraform, Puppet, and
Saltstack. And specific ecosystem relationships, with companies like
CoreOS.

Mark described the change in the Foundation's event strategy,
targeting events like KubeCon, DockerCon, CoreOS Fest, etc. as key
events where we should be positioning the OpenStack brand and
developing relationships.

He also described particular focus areas of individual staff members
which are relevant to the topic - Chris Hoge working with upstream
Kubernetes and running OpenStack SIG meetings, David Flanders working
on a report around the gaps when running platforms on OpenStack (like
Cloud Foundry, OpenShift, Kubernetes, and Terraform), and how Ildiko
Vancsa and Kathy Cacciatore are both working closely with OPNFV.

Finally, Mark talked about the Open Source Days event at the OpenStack
Summit in Boston, as well as some very early stage discussions for an
OpenDev event which would be a small, focused event around improving
the integration between applications frameworks and open
infrastructure.

### Community Health

The final area of discussion was the subject of community health, and
Mark first put out some statistics that he felt painted a very
reassuring picture of the community's health. In 2016, we had 3,500
unique contributors, 1,850 of which were retained from 2015. In Ocata,
we had fewer developers than Newton, most likely because it was a
shorter cycle.

Mark contrasted challenges with projects like Trove and Designate
losing contributors, while projects like Kuryr, Kolla, and Zun seeing
the greatest number of new contributors.

Similarly, Mark talked about HPE laying off upstream developers, Cisco
killing off intercloud, a small slowdown in Summit sponsorships, while
we have also added 7 more Gold members, and many first-time corportate
members and Summit sponsors.

## Strategic Planning Exercise

The rest of the day was given over to a multi-stage strategic planning
exercise prepared by Allison and Alan. The idea was to discuss these
focus areas, [gather everyone's ideas for
improvement](https://photos.google.com/share/AF1QipM10xRXuSCufsV8g8O60nnWgAW0n3yDteHqM1BPSgUfxNNZ6fZulsJ8BnYtcY5pNA?key=UEk5SXlaYlRSdllyYXZDVTlvN2EwR1NidjhjUGl3),
summarize and categorize these ideas, vote on ideas in each focus
area, and finally agree on how to proceed with concrete goals for the
next 6-9 months.

### Discussion

The initial discussion covered a lot of ground. Allison introduced
each focus area by describing the input we gathered via the etherpads
and input she gathered through 1:1 interviews with a variety of
people.

One topic of discussion related to how OpenStack can simplify how we
describe OpenStack, particularly to reduce confusion introduced with
the Big Tent change. Various ideas around categorization, tagging,
vertical definitions, a concept of constellations, maturity ratings,
and much more, were discussed.

We talked about the promise for the future that OpenStack
provides. That there will be evolution over time, that we deliver the
cloud solutions of today and will deliver the solutions of
tomorrow. That the challenge of smooth upgrades is part of our
challenge in delivering "future proof infrastructure".

We talked about the challenges of scalability, manageability, and
complexity. The theme of containerized deployments, the need for
vertically focused views of OpenStack, for example for Telco users. We
discussed the need for OpenStack to be able to evolve over time, with
refactoring or rewriting components being only one of the possible
approaches we may see over time.

We talked at great length about how OpenStack could work more closely
with adjacent communities. How the relationship with these communities
should bring value to both communities. We particularly emphasized the
need for a closer relationship with the CNCF and the Kubernetes
community.

### Gathering Ideas

Over lunch, everyone wrote their concrete, actionable ideas for
improvement on sticky notes and put them on [flipcharts for each of the
areas of
discussion](https://photos.google.com/share/AF1QipM10xRXuSCufsV8g8O60nnWgAW0n3yDteHqM1BPSgUfxNNZ6fZulsJ8BnYtcY5pNA?key=UEk5SXlaYlRSdllyYXZDVTlvN2EwR1NidjhjUGl3). Later,
Jonathan volunteered to group the ideas into themes, and summarized
these themes for the group, facilitating further discussion before
voting on which theme in each area we should particularly focus on.

On the subject of communicating about "what is OpenStack", the main
themese were marketing activities, various categorization ideas, and
idea Allison talk about earlier referred to as "constellations". We
later voted to focus on the categorization area and formed a group of
interested parties:

> Communicate about OpenStack: Categorize (objective data) and map
> (subjective approach) OpenStack projects as base versus optional
> (within a specific use case), integrated versus independent release,
> emerging versus mature, stability, adoption metrics, what works
> together, services versus consumption (operational tools/client
> libraries), and other criteria
>
> Names: Thierry Carrez [lead], Alan Clark, Allison Randal, Jon
> Proulx, Melvin Hillsman, Lauren Sell, Tim Bell, Mark Baker, Kenji
> Kaneshige

For unanswered requirements, we discussed how to prioritize, ideas
around a solution focus, scalability challenges, and a list of
specific features that people felt were important. A counter-point was
made that rather than focusing on any of these ideas, perhaps the
focus should be on working with adjacent communities. Later, we
discussed the need to grow the connection between the Product Working
Group, the TC, and individual projects. The outcome and group for this
was:

> Requirements: Bring different groups (UC/technical/etc) together at
> Forum to collaborate/communicate aroud user stories, gap analysis,
> what fits in the current state of tech, prioritize what would have
> the greatest impact in reducing pain for users.
>
> Names: Melvin Hillsman [lead], Yih Leong Sun, Jon Proulx, Rob Esker,
> Emilien Macchi, Doug Hellmann, Tim Bell, Shamail Tahir

On the topic of adjacent communities, we observed that by far the most
dominant area of discussion was the need to create better connection
with the Kubernetes community. The themes were community engagement,
technical engagement, OpenStack consuming technology from the
Kubernetes and containers world, and making OpenStack technology more
consumable by Kubernetes. In the end, there was strong consensus to
focus on the consumability of OpenStack technologies:

> Adjacent Technologies: Make our technology more consumable
> (independently) by other communities/projects.
>
> Names: Chris Price [lead], Alan Clark, Dims, Rob Esker, Mark
> Collier, Steven Dake, Mark McLoughlin, Shamail Tahir

For changes to the technology, we discussed simplifications, making
containers first class citizens, recording tribal knowlede, culling
failed efforts, converging deployment tools, and welcoming emerging or
competing projects. The theme we voted to focus on was:

> Changes to the Technology: Workstream to simplify existing projects,
> reduce dependency options, reduce config options.
>
> Names: Mike Perez [lead], --> TC project

Finally, on the subject of community health, we talked about
onboarding contributors, reworking our processes, community tools,
growing leaders, corporate involvement in the project, and recognizing
work with adjacent communities. We voted to focus on the leadership
theme:

> Community Health: Grow next generation of
> leadership/experts/cross-project devs within the community
>
> Names: Steven Dake [lead], Chris Price, Jeremy Stanley, Dims,
> AlanClark, Joseph Wang

### Next Steps

For each of these focus areas, the lead person in the group committed
to organizing a kick-off meeting by March 22nd. The real work will
begin there!








