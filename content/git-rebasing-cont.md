Title: Git Rebasing (cont.)
Date: 2011-02-26 15:25
Author: markmc
Tags: Git
Slug: git-rebasing-cont
Status: published

[As I said
already](http://blogs.gnome.org/markmc/2011/02/23/git-rebasing/), git's
interactive rebase tool is seriously useful for preparing a nice,
cleanly split up series of patches. And, despite some people's dire
warnings, there's no reason not to share an in-progress patch series
using git so long as you take care to warn others against relying on
your tree not rebasing.

Why would a patch series not be complete? One reason might be that a
patch introduces a regression. As they say, you often have to break some
eggs to make an omelette but, if you value the power of git's bisection
tool, you'll want each individual patch to be regression free.

Okay, say you're porting an application from one database framework to
another. You might do a bunch of hacking to demonstrate the concept and
then send that work out for comment. Only at this point will you go
about figuring out polishing the work off and, finally, cleaning the
changes up into a nice patch series.

This approach implies that the work will only stop rebasing quite late
in the day. Which leaves a problem - how can you possibly collaborate
with others if your tree is rebasing? How can you take patches to fix
regressions? How can others help you clean up the series?

Here's one suggestion, based on an approach Stephen Tweedie came up with
when we were working together on a series of patches:

1.  Say your branch is called fluffy-piglet. You've pushed it out and
    asked for comments. Don't rebase this branch again.
2.  Create another branch called fluffy-piglet-rebasing, basing it
    initially on fluffy-piglet.
3.  Tag both branches with e.g. a -v1 suffix, check that the trees in
    both tags are identical:

        $> git diff fluffy-piglet fluffy-piglet-rebasing
        $> git show -s --format='%t' fluffy-piglet fluffy-piglet-rebasing

4.  Push the rebasing branch and the v1 tags to your repo.
5.  If you wish to rebase and do some cleanup work on the patches, do so
    and tag and push the result to the fluffy-piglet-rebasing branch in
    your repo as in (3) and (4), but using a new suffix.
6.  If you receive some patches, pull them into your fluffy-piglet
    branch, tag the result and rebase the patches onto the rebasing
    branch e.g.

        $> git tag fluffy-piglet-v3
        $> git rebase --onto fluffy-piglet-rebasing-v2 fluffy-piglet-v2
        $> git tag fluffy-piglet-rebasing-v3

7.  If you wish to rebase unto latest upstream, you could first enable
    git's "reuse recorded resolution" feature:

        $> git config --global rerere.enabled true

    Then you rebase the rebasing branch:

        $> git checkout fluffy-piglet-rebasing
        $> git rebase upstream/master
        $> git tag fluffy-piglet-rebasing-v4

    And then, you merge upstream into the non-rebasing branch:

        $> git checkout fluffy-piglet
        $> git merge upstream/master
        $> git tag fluffy-piglet-v4

    As in (3), you should be able to verify that the two resulting trees
    are identical.

    <p>
    If any conflicts needed to be resolved during rebasing, there's a
    good chance that having rerere enabled will mean the conflict will
    be automatically resolved when merging.

8.  Finally, if anyone wants to help you with any of the series cleanup
    work, just 'pass the baton'. You basically say, 'No more rebasing
    from me after v4, go ahed' and the other person can work away on the
    rebasing branch until they are ready to pass control back again.

This certainly isn't a straightforward workflow, but it gives you:

-   The ability to work with others since folks have a non-rebasing
    branch to work against
-   The ability to clean up a series using rebase while still having
    confidence that nothing is being screwed up because you have the
    pair of tags with identical tree contents
-   The ability to allow others to help clean up the series too

The fact that this workflow is so awkward has its advantages too - it
encourages you to clean up the series early and stop rebasing it. This
is not a workflow you'd like to use for an extended period of time.
