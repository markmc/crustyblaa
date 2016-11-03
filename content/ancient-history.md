Title: Ancient History
Date: 2012-07-27 11:54
Author: markmc
Tags: Git, OpenStack
Slug: ancient-history
Status: published

In OpenStack, we have a particular problem where much of the early
development on the project was done using bzr and launchpad. All this
history is in git, but it can be difficult to find the bzr merge
proposal in launchpad which caused a given commit to be merged.

Here's an example of how I did it yesterday.

We're interested in [commit
8aea573](https://github.com/openstack/nova/commit/8aea573):

    commit 8aea573bd2e44e152fb4ef1627640bab1818dede
    Author: Trey Morris ...
    Date:   Tue Dec 28 23:55:58 2010 -0600

        initial lock functionality commit

To trace back to the merge commit which merged this into master, I did:

    $> git log --graph --topo-order --ancestry-path --merges 8aea573bd2e44e152fb4ef1627640bab1818dede..HEAD
    * commit ae5dbe2b5d4871d3e26e859c03feab705c9c59ea
      Merge: 9eca4d5 76e3923
      Author: Trey Morris ...
      Date:   Fri Jan 7 00:49:30 2011 +0000
      
          This branch implements lock functionality. The lock is stored in the compute worker database. Decorators have been added to the opens
      
    * commit f9c33f4ba09e02f8668bdd655b7acba15984838c
      Merge: ba245da 9eca4d5
      Author: Trey Morris ...
      Date:   Thu Jan 6 16:35:48 2011 -0600
      
          merged trunk
      
    * commit f09d1ce4d38f3a8ef72566e95cde38f1dc1b8bed
      Merge: 9b9b5fe 9a84a2b
      Author: Trey Morris ...
      Date:   Wed Dec 29 15:13:24 2010 -0600
      
          fixed merge conflict with trunk

Double check that by looking at exactly what was merged in:

    $> git diff 9eca4d5..ae5dbe2
    diff --git a/nova/api/openstack/servers.py b/nova/api/openstack/servers.py
    index ce64ac7..f8d5e76 100644
    --- a/nova/api/openstack/servers.py
    +++ b/nova/api/openstack/servers.py
    @@ -170,6 +170,50 @@ class Controller(wsgi.Controller):
                 return faults.Fault(exc.HTTPUnprocessableEntity())
             return exc.HTTPAccepted()
     
    +    def lock(self, req, id):
    ...

That's the one!

Now how to find the merge proposal? Simply googling for "This branch
implements lock functionality" quickly lead me to the [correct merge
prop](https://code.launchpad.net/~tr3buchet/nova/lock/+merge/44874), but
better ideas welcome :)
