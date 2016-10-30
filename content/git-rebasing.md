Title: Git Rebasing
Date: 2011-02-23 14:01
Author: markmc
Category: General
Slug: git-rebasing
Status: published

For me, 'git rebase -i' is perhaps git's killer feature. I'm a big fan
of small, self-contained commits both for ease of patch review and for
the sake of useful commit history later. I used to do this on CVS using
quilt but git takes a huge amount of the pain out of it.

Ever since I discovered the feature a few years ago, I've also been
vaguely aware of kernel developers advice to people on rebase ... often
simplified to [OMG no. Never
rebase.](http://twitter.com/dwmw2/status/14387074346000384).

When pushed to elaborate, I guess most would say:

> Once you share a commit with someone, never rebase it. They may base
> their work on your commit and by rebasing it, you're screwing
> everything up.

One memorable comment from Linus on the subject was ["Have the f\*cking
back-bone to be able to stand behind what you
did!"](http://lkml.org/lkml/2008/2/12/653).

In context, this all makes sense. If a kernel developer sends a pull
request and it gets merged into one tree, then rebases and that gets
merged into another tree and both get merged into Linus's tree ... then
yes, you have a bit of a disaster on your hands.

However, I think the rules above are too simplistic for most git
newbies. Such newbies are unlikely to see their trees pulled into the
whirling vortex of kernel trees so there's no need to terrify them about
using rebase.

My advice is:

1.  If you're learning git, take the time to understand the rebase
    command and, especially, the interactive option.
2.  If you're working on a series of patches, it's perfectly fine for
    you to share that series with others even if it's not finished. That
    means later rebasing a commit you've shared with others.
3.  If you're worried people might base their work on a commit you plan
    to rebase later, then you warn people by putting e.g. "v1",
    "rebases" or "rebasing" in the repository or branch name.
4.  If someone does base their work on a commit you have rebased, then
    point them at the [Recovering From Upstream Rebase part
    of git-rebase(1)](http://www.kernel.org/pub/software/scm/git/docs/git-rebase.html#_recovering_from_upstream_rebase).
    It's really not the end of the world, especially in the
    simpler cases.

