Title: The RHEL rebuilds debate - let's talk about values
Date: 2023-07-17 20:00
Author: markmc
Tags: Red Hat
Slug: rhel-rebuilds-debate-lets-talk-values
Status: published

The status quo around RHEL source code availability has
[changed](https://www.redhat.com/en/blog/red-hats-commitment-open-source-response-gitcentosorg-changes),
as has Red Hat’s stance on RHEL rebuilds. For example, we now say:

> Ultimately, we do not find value in a RHEL rebuild and we are not
> under any obligation to make things easier for rebuilders; this is
> our call to make.
> ...
> Simply rebuilding code, without adding value or changing it in any
> way, represents a real threat to open source companies everywhere.

If the status quo has changed, doesn’t that mean that our values have
changed? I believe the opposite is true - this is Red Hat fully
confronting its values, taking uncomfortable steps to make our values
more clear, and moving beyond an uneasy ambiguity that I think has
existed for too long. And that’s not a convenient, reverse-engineered
conclusion to justify the change after-the-fact. I can actually
pinpoint the discussion in 2011 where our values on this became clear
to me. Let me explain.

I joined Red Hat 20 years ago via the GNOME project. Any personal
values I had around software freedom were not particularly strongly
held, and GNOME itself had a sometimes fractious relationship with the
FSF. But I was drawn in and excited by the potential of developing
software in the open, with a community of like-minded contributors
with diverse motivations for contributing. This was a time of
open-source vs free software debates, and I found myself observing,
fascinated, and leaning towards the open-source perspective. To pick
one random example of the sort of
[argument](https://www.oreilly.com/tim/opensource/) that appealed to
me (while absolutely rejected by other friends in the community):

> Richard thinks there is a moral imperative underlying the free
> redistribution of software, and now, by extension, other
> information. Richard feels that since there isn't any physical cost
> associated with copying software, limiting free redistribution is a
> form of extortion. I on the other hand feel that it's immoral to try
> to compel someone else to give you something they've created without
> compensating them in some way. That is, when software is freed, it
> is a gift, not the result of an obligation...

When I joined Red Hat, I again found myself observing the perspectives
of my colleagues and the decisions we were making. I guess I was
trying to identify Red Hat's values on this knotty subject. It's a
funny thing trying to pin down a group’s values - you're unlikely to
find a consensus view, and neither are you simply looking for the view
of a set of senior leaders.

Over time, we developed a mission statement - *“To be the catalyst in
communities of customers, contributors, and partners creating better
technology the open source way”* - and a set of behavioral values -
*freedom, courage, commitment, and accountability*. I found the
omission of anything about software freedom is telling. My sense has
always been that we are reluctant to open a potentially divisive
debate on this, perhaps indicating a nervousness that there is an
underlying and unspoken division between community-oriented technical
leaders and business-oriented executive leaders.

I happened to be in the Westford office when Oracle announced its RHEL
rebuild - Unbreakable Linux - in 2006. Sentiments such as [“With this
move, Oracle simply rips off Red Hat's mind-share, while promising a
cheaper price”](https://lwn.net/Articles/206290/) were widely
shared. There was a sense of existential threat, and a need to rally
and respond that RHEL was “Unfakeable Linux”. I 100% bought into this,
but I also wondered… isn't this software freedom in action? If our
customers aren’t paying for the bits, what's the problem? And yet we
did have a problem with this move. It stung. It was unfair. It wasn't
in the spirit of this industry movement we thought we were all a part
of. And so, it seemed pretty clear to me - this sort of software
freedom was not one of our values, and if we would have no qualms
about limiting this particular freedom.

Some five years later in 2011, I was involved in deciding which
license we would use for an exciting new open-source project we were
launching based on a codebase from an acquisition. Given a blank slate
in terms of license choice, we spent some time discussing the merits
of copyleft vs permissive licenses. In that discussion, we seemed to
have no interest in preventing any downstream user from incorporating
the codebase into a proprietary product - that was fine by us. But we
did agonize over the best strategy for building a community, a
community where we might hope one day to not be the largest
contributor. We chose the Apache License (v2), and the discussion made
something clear to me - we saw no “moral imperative” around software
freedom, but we were absolutely committed to building in the open, and
forming or joining healthy communities - [“the open source
way”](https://opensource.com/open-source-way) was an core, unshakeable
value.

And so I'm glad we're openly confronting our values on this now, even
if this move disappoints any of our friends in the open-source world
who have different - but hugely overlapping - values. My personal view
is that we are staying true to our values even as we limit the
redistribution of our products - while respecting the applicable
upstream licenses.

Especially when it is in response to a move - by those software
vendors or larger enterprise users who do have the resources to pay
for RHEL or to create their own derivative of a community distro - to
benefit or profit from the value of RHEL without paying Red Hat.

However, Red Hat remains exceptionally committed to the open-source
development model, following the principle of "upstream first",
developing our products in the open, building communities, and
embracing the diversity of users downstream of any of these
open-source projects. CentOS Stream - the recently created upstream of
RHEL, a project and community that we now use to develop RHEL - shows
an additional level of commitment to open-source community building
that I would not have predicted 10 years ago when RHEL development
(then downstream of Fedora) was entirely behind Red Hat’s firewall.

I can understand the negative reaction to this change. However, a lot
of the commentary is pretty muddled, and I would be happy to see a
deeper discussion of open-source values. I think that Red Hatters
should be proud of our values, and embrace the debate that we have now
triggered.
