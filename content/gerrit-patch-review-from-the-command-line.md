Title: Gerrit Patch Review From The Command Line
Date: 2011-09-25 14:28
Author: markmc
Tags: OpenStack, Git
Slug: gerrit-patch-review-from-the-command-line
Status: published

[OpenStack Nova](http://nova.openstack.org/) switched from bzr and
launchpad to github and [gerrit](http://code.google.com/p/gerrit/) on
Friday. While I'm delighted the project is using git now, I've always
found the gerrit UI to be a bit of a pain.

On IRC, [Monty Taylor](http://inaugust.com/~mordred) mentioned the
[gerrit command line
interface](https://review.openstack.org/Documentation/cmd-index.html)
which looked fairly interesting. Sure enough, you can actually review
and approve a patch using this without ever touching the web UI. Below
is an example of reviewing a [Glance](http://glance.openstack.org/)
patch, but the same thing would work for Nova.

First, you obviously need to clone the repo:

    $> git clone git://github.com/openstack/glance.git
    $> cd glance

To make life a little easier, you can add a host alias to your SSH
config:

    $> cat >> ~/.ssh/config <<EOF
    Host review
      Hostname review.openstack.org
      Port 29418
      User markmc
    EOF

Then add the gerrit server as a git remote:

    $> git remote add -f gerrit ssh://markmc@review/openstack/glance.git

Okay, now browse the patches needing review:

    $> ssh review gerrit query status:open project:openstack/glance | less

Once you've picked a patch, take it's Change-Id: and look at its patch
sets and reviews:

    $> ssh review gerrit query status:open project:openstack/glance   
            change:I27bb6b3951422ad32e5e0225765b1056c5b3ffc5   
            --current-patch-set --all-approvals | less

Then, using the 'ref' in the output, you can fetch the patches into your
repo and review them:

    $> git fetch gerrit refs/changes/36/636/2
    $> git checkout -b git-authors FETCH_HEAD

Once you're ready to submit your review, you can do:

    $> git checkout master
    $> git branch -D git-authors
    $> ssh review gerrit review --code-review +1 -m "'Looks good to me.'" cd9b3a0f2fb91d0d01606ef4bbd90cf8f29267da

That's all pretty neat, but I'm missing how to go about doing a detailed
review with comments inline with quoted sections of code. Perhaps if
'gerrit review' could take the review comments over stdin?
