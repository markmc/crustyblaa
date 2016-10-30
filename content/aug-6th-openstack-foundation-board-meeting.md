Title: Aug 6th OpenStack Foundation Board Meeting
Date: 2013-08-08 10:25
Author: markmc
Category: openstack, openstack-foundation-board-meeting
Slug: aug-6th-openstack-foundation-board-meeting
Status: published

On Aug 6th, the OpenStack Foundation Board held a two hour conference
call meeting which was open to anyone to join. [The agenda was published
in
advance](https://wiki.openstack.org/wiki/Governance/Foundation/6Aug2013BoardMeeting).

As usual, this my informal recollection of the meeting. It's not an
official record, etc. Jonathan published an [official
summary](http://lists.openstack.org/pipermail/foundation/2013-August/001454.html)
on the foundation mailing list.

### Preliminaries

Alan Clark chaired the meeting and spent the first few minutes reviewing
the agenda and holding the roll call. We had more than 50% of the board
members, and so had sufficient quorum.

We then reviewed the [minutes of the previous
meeting](https://wiki.openstack.org/wiki/Governance/Foundation/27June2013BoardMinutes)
and approved them by vote. Todd, Troy, Nick, Devin and Jim all abstained
because they weren't present at that meeting.

### Patent Cooperation

Next up was a follow-on from the patent cooperation discussion at our
[previous
meeting](http://blogs.gnome.org/markmc/2013/06/29/june-27th-openstack-foundation-board-meeting/).

The Legal Affairs Committee had previously [proposed three
options](https://wiki.openstack.org/w/images/2/24/OSLAC_Update_for_Board_062713.pdf)
that we make no change, that we implement a Google-style patent pledge
or that we introduce an OIN-style cross licensing agreement.

Keith Bergelt, CEO of the Open Invention Network, attended the meeting
and gave a
[presentation](https://wiki.openstack.org/w/images/1/10/20130806OIN_Presentation_To_The_Open_Stack_Board.pdf)
describing the OIN and how it could play a key role in OpenStack's
strategy to create an environment of patent non-aggression around
OpenStack. Keith has been actively working with the Legal Affairs
Committee to develop a fourth proposal for the board which would make
the best possible use of the OIN.

Keith described how the OIN was formed 8 years ago by IBM, NEC, Novell,
Philips, Red Hat and Sony to ensure "freedom of action, freedom to
operate" around Linux. It has some 560 member companies who sign up to a
broad cross-licensing agreement whereby any patents they hold which read
on Linux is licensed to all other member companies.

The patents which are covered by the OIN agreement are those which read
on the software packages listed in the [OIN's Linux System
Definition](http://www.openinventionnetwork.com/pat_linuxdef.php). Over
time, this definition has grown to include the likes of Android, WebOS
and, more recently, OpenStack. The OIN views OpenStack has one of the
most import projects after Linux and feels that including OpenStack in
its defintiion is an obvious step.

That OpenStack is included in the OIN system definition means that there
are already 560 licensees committed to non-aggression around OpenStack.
Keith feels that this goes a long way to achieving the OpenStack
Foundation's goals in this area and that we should seek to make the most
effective use of the existence of this agreement rather than reinvent
the wheel.

Keith proposes a more formalized relationship with the Foundation, that
members would be encouraged to join the OIN, that we'd do joint press
releases and that there would be an ongoing direct relationship with the
TC to ensure the system definition is regularly updated to include all
OpenStack projects.

### Legal Affairs Committee

Van Lindberg was up next to provde an update from the [Legal Affairs
Committee](https://wiki.openstack.org/wiki/Governance/Foundation/LegalAffairsCommittee)
but this turned out to be a continuation of the previous discussion on
patent cooperation.

Van summed up this fourth proposal succinctly - that OpenStack members
get behind the OIN. He went on to describe how a difficulty with this
approach is that some members of OpenStack will never be members of the
OIN because the OIN fundamentally see those companies as a threat to
Linux. He didn't name these companies.

So, the question becomes how we can ensure the ability of those
OpenStack members who aren't members of the OIN to join a patent
cooperation initiative specifically around OpenStack.

Van first described how OpenStack LLC (the Rackspace owned entity which
held OpenStack's before the Foundation was formed) actually joined the
OIN some time ago because of concerns about the ["CPTN
transaction"](http://www.virtualizationpractice.com/doj-blocks-emcvmware-from-acquiring-virtualization-patents-from-novell-10368/).
The OpenStack Foundation could quite easily take over this agreement
and, by virtue of the fact that the OpenStack Foundation is in some
sense the entity licensing the OpenStack software to everyone, the
benefits of the OIN cross-license would flow to all OpenStack users.

For OIN non-members, the Foundation could create a separate, limited
license agreement whereby the OpenStack related patents held by such
licensors would be licensed to the Foundation and the benefits of that
agreement would also flow to all OpenStack users.

Van went on to talk a little about patent trolls [(a subject close to
his heart)](http://www.rackspace.com/blog/tag/patent-trolls/), how this
is a serious issue for OpenStack and how, even now, there is a troll
going after Rackspace and HP over a number issues including some related
to OpenStack. Van feels that the OIN does not actually protect against
the threat of trolls very well, because (somewhat obviously) such trolls
would not be members of the OIN.

Van raised again (this has been discussed before) the idea of a patent
indemnity program whereby OpenStack members (or even just the
Foundation) would contribute to a fund which could be used for the legal
defence (not any settlements themselves) of any OpenStack members
threatened by patent trolls for the use of OpenStack. Van feels that
patent trolls often go after some weaker companies, obtain a small
settlement because that company feels it's cheaper to settle than to
defend and that settlement sets a problematic precedent that the troll
can then build upon. An indemnity program would encourage members to
fight patent trolls and avoid precedents being established which would
set the entire community up for trouble.

Eileen made the point that the OIN was created because the GPL lacks a
patent license. We're not in the same position, since OpenStack is
licensed under the Apache License which includes a broad patent license.
She raised concerns about the idea of an indemnity program, how it's
scope could turn out to be very large and expensive and disagreed that
trolls always go after the smaller players.

The conclusion was ... no decisions today, more dialogue needed.

### OpenStack Training

Next up, Jonathan revisited the topic of how the Foundation can
encourage and regularize the market forming around OpenStack training.

This topic was also covered in the June meeting and Jonathan felt there
was good support for some of the proposals but board members had
concerns and questions about other aspects. Since then, Jonathan has
been talking to several board members including Brian Stevens and Boris
Renski and feels he can provide some clarifications and updates. The
Foundation would like to move forward with two proposals - a training
licensing program and a baseline certification test.

The training licensing program would replace the use by training
providers of the Built For OpenStack mark. This will allow the
Foundation to have a closer relationship with training providers and
help raise awareness about the availability of OpenStack training. There
is broad support for this proposal  
and the Foundation have a draft agreement ready to circulate to training
providers.

The baseline certification test proposal was the proposal that has
required more discussion but it is better understood now. The idea is
that the Foundation would define a common baseline set of training which
all licensed OpenStack providers must include and certify against, but
that the Foundation also fully expects providers to expand upon this
content greatly and compete on the unique aspects of their training.

The vast majority of what would be included in this baseline training is
already covered by all training courses out there. The Foundation would
not seek to force content and topics on training providers but would
instead seek to add new content when it sees that training providers are
already covering these new topics. It is expected that the Foundation
staff and others it engages will take 6-9 months to prepare this
program.

Jonathan feels a baseline OpenStack certification would ensure that
there is OpenStack training which globally available, not
cost-prohibitive for students in regions all around the world and
provides a target for people who want to become knowledge around
OpenStack.

The board moved to support the Foundation staff in its efforts to create
a baseline certification testing program for OpenStack. The motion was
passed unanimously.

### User Committee Update

Tim Bell took the floor next to raise an issue the [User
Committee](http://www.openstack.org/foundation/user-committee/) has been
discussing in recent times.

The committee currently consists of Tim, Ryan Lane and JC Martin. While
the committee is doing a great job, they feel that their limited numbers
(and their limited time) is constraining their ability to achieve some
of their goals.

The obvious solution is to add more members to the committee, but
there's a catch. Committee members sign an NDA and have access to some
sensitive data about OpenStack deployments which are obtained through
surveys with the understanding that the information is confidential.
Adding significantly more members could compromise the confidence that
survey responders would have in the confidentiality of their responses.

Tim has been talking with Tom Fifield about what role Tom could take (as
a Foundation staff member) on the committee in order to help out,
without Tom having to sign the NDA and gain access to the confidential
survey results. The idea is that Tom can take on some of the
responsibility to act as a go-between who ensures that issues which are
identified by the committee are raised as appropriate with the developer
community.

In a similar vein, the committee is exploring the idea of a structure
whereby only the "core" committee members need to sign the NDA and there
would be sub-groups of the committee who can get involved without
gaining direct access to the survey results.

### What is Core

Rob Hirschfeld gave a quick update on the "what is core" discussions he
is  
leading. The discussion was initially limited to the board, more
recently  
[broadened to include the
TC](http://lists.openstack.org/pipermail/openstack-tc/2013-July/thread.html#308)
and Rob now plans to broaden it to include the  
wider community.

Rob mentioned a
[flowchart](http://lists.openstack.org/pipermail/foundation/2013-August/001453.html)
he has prepared to describe some of the proposed process. He also
discussed how the initial position on requiring "plugins" has evolved
into talk of designating some parts of projects as "required
implementations" and allowing other parts to have "alternate
implementations".

### Other Updates

Todd and Rob met with the Foundation's legal team to discuss what
changes to the Individual Directors election process would be allowed
under Delaware law. He will present some thoughts on this at the next
board meeting.

Simon has been working with Mark Collier and Heidi Bretz to ensure that
companies who have expressed an interest in applying to be a Gold Member
are aware of the board's revised expectations around new members. Simon
and the membership committee still plan on re-drafting the wiki page
describing the [criteria for new
members](https://wiki.openstack.org/wiki/Governance/Foundation/PotentialMemberCriteria).

Alan mentioned that the Compensation Committee completed a mid-year
review of Jonathan's goals for the year and concluded things are very
much on track. Full details were posted to the foundation-board mailing
list.

The next board meeting is scheduled for October 3rd at 9am PST. There
will also be an all day board meeting in Hong Kong on November 4th.
