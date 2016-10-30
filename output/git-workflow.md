Title: Git Workflow
Date: 2008-05-07 07:55
Author: markmc
Category: git
Slug: git-workflow
Status: published

[Havoc's recent post on git](http://log.ometer.com/2008-04.html#29) was
interesting because it shows how frustrating git can be if you try and
treat it as "just another CVS". From that perspective, git just seems
like it's just some bizarre way for kernel hackers to torture those who
*just want to get work done*.

I turned that corner with git when I learned about "git-rebase -i" and
came to the startling realisation that *git's history is editable*.
Basically, this allows you to change your workflow such that you can
hack away at will, commit often and then rewrite the history of your
hacking session so that you have a coherent set of patches/commits at
the end of it with a useful changelog.

e.g. you can go from:

>     A1---B1---A2---A3---C1---B2---C2---C3

to:

>     A1---A2---A3---B1---B2---C1---C2---C3

or even:

>     A'---B'---C'

Using git rebasing, I found that I could use a similar workflow to using
[quilt](http://savannah.nongnu.org/projects/quilt) with CVS, or
mercurial with its [patch queue (mq)
extension](http://www.selenic.com/mercurial/wiki/index.cgi/MqExtension).
The revision history becomes less about tracking the progress of your
work, and more a maleable mechanism for preparing patches before
submitting upstream.

[Red Hat Magazine](http://www.redhatmagazine.com) has a [nice
article](http://www.redhatmagazine.com/2008/05/02/shipping-quality-code-with-git/)
explaining all this, and I even picked up some new tricks to try out:

-   `git-merge --squash` : merge a branch/tag into the current branch,
    but squash all the commits together as an uncommitted change to the
    working tree. When you go to commit the result, the changelog of all
    the merged commits is available in the commit message editor so you
    can munge them together into a useful changelog.
-   `git-cherry-pick --no-commit` : apply the changes from a given
    commit to your working tree, but do not commit it. Could be used to
    achieve something similar to a squashed merge, but where you
    selectively merge only some of the commits.
-   `git-add --patch/--interactive` : add some changes from the working
    tree to the index, but e.g. selectively add only some of the patch
    hunks from a given file. Allows you to make a bunch of changes to a
    file, but commit the changes as individual commits.

