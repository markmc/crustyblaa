Title: Python Exception Chaining
Date: 2013-07-11 09:28
Author: markmc
Category: openstack, python
Slug: python-exception-chaining
Status: published

OpenStack has an awful lot of developers writing Python code and many of
us wouldn't consider ourselves true "pythonistas". This means we wind up
having a bunch of interesting discussions about e.g. [EABL vs
LBYL](http://lists.openstack.org/pipermail/openstack-dev/2013-July/thread.html#11635).

A particular bugbear of mine is exception handling. I'm convinced that
very, very few developers think hard about their error handling strategy
and that the problem is even more serious with exception based
languages.

So, I really like getting into error handling discussions. This morning,
we have a great one - [how to do exception chaining in Python, and
whether that's even something you want to
do](http://lists.openstack.org/pipermail/openstack-dev/2013-July/011702.html).
