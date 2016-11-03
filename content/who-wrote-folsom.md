Title: Who Wrote Folsom
Date: 2012-09-28 07:19
Author: markmc
Tags: OpenStack
Slug: who-wrote-folsom
Status: published

As [I did for
Essex](https://lists.launchpad.net/openstack/msg09650.html), I've used
[Jonathan Corbet's gitdm](http://lwn.net/Articles/290957/) to do some
analysis of the commits to the core projects during Folsom.

Here's the top 20 committers across Nova, Glance, Swift, Keystone,
Horizon, Quantum and Cinder:

` Processed 3110 csets from 291 developers 132 employers found A total of 350046 lines added, 275491 removed (delta 74555)`

Developers with the most changesets  
Russell Bryant 160 (5.1%)  
Brian Waldon 160 (5.1%)  
Dan Prince 154 (5.0%)  
Gabriel Hurley 124 (4.0%)  
Mark McLoughlin 118 (3.8%)  
Johannes Erdfelt 113 (3.6%)  
Vishvananda Ishaya 92 (3.0%)  
Joe Gordon 85 (2.7%)  
Michael Still 71 (2.3%)  
Eoghan Glynn 70 (2.3%)  
Rick Harris 59 (1.9%)  
Gary Kotton 58 (1.9%)  
Dolph Mathews 55 (1.8%)  
Yun Mao 50 (1.6%)  
John Griffith 45 (1.4%)  
Daniel P. Berrange 45 (1.4%)  
Dan Wendlandt 43 (1.4%)  
gholt 40 (1.3%)  
Rongze Zhu 39 (1.3%)  
Alex Meade 39 (1.3%)  
Covers 52.090032% of changesets  
</code>

Congrats and thanks to everyone involved in this release!

There are [more raw stats
here](https://github.com/markmc/openstack-gitdm/tree/results/folsom)
showing stats for each project individually and also statistics for
gerrit reviewers and launchpad bug fixers.

Of course, this is nowhere near as polished as [Bitergia's awesome
report](http://bitergia.com/public/reports/openstack/2012_09_folsom/)
with pretty graphs and detailed analysis.
