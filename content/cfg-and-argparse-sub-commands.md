Title: cfg and argparse sub-commands
Date: 2012-11-26 16:03
Author: markmc
Tags: OpenStack
Slug: cfg-and-argparse-sub-commands
Status: published

[Laurence Miao](https://launchpad.net/~laurence-miao) did some great
work recently to [port cfg from optparse to
argparse](https://blueprints.launchpad.net/oslo/+spec/cfg-argparse).

The only significant API impact was that we could no longer have
`CONF()` return unparsed command line arguments.

We chose to offer two alternatives - firstly, support for positional
arguments:

> &gt;&gt;&gt; CONF.register\_cli\_opt(MultiStrOpt('bar',
> positional=True))  
> True &gt;&gt;&gt; CONF(\['a', 'b'\])  
> &gt;&gt;&gt; CONF.bar  
> \['a', 'b'\]

and, secondly, integration with [argparse's
sub-commands](http://docs.python.org/dev/library/argparse.html#sub-commands):

> &gt;&gt;&gt; def add\_parsers(subparsers):  
> ... list\_action = subparsers.add\_parser('list')  
> ... list\_action.add\_argument('id')  
> ...  
> &gt;&gt;&gt; CONF.register\_cli\_opt(SubCommandOpt('action',
> handler=add\_parsers))  
> True  
> &gt;&gt;&gt; CONF(\['list', '10'\])  
> &gt;&gt;&gt; CONF.action.name, CONF.action.id  
> ('list', '10')

After porting the CLIs in [Nova](https://review.openstack.org/16881)
(nova-manage), [Glance](https://review.openstack.org/16900)
(glance-control and glance-manage) and
[Keystone](https://review.openstack.org/16899) (keystone-manage) over to
this sub-parsers stuff, it looks like it's going to work out quite
nicely.
