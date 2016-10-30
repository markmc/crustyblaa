Title: Friday is for Yak Shaving
Date: 2012-09-14 17:53
Author: markmc
Category: openstack
Slug: friday-is-for-yak-shaving
Status: published

My mate [Derek](http://goodsquishy.com/) was giving me grief about not
testing his OpenStack deployment in our lab at Red Hat. Friday seemed
like a good day to give it a shot for a few minutes.

First problem - I'm one of the weird people at Red Hat who eschews the
VPN in favour of SSH tunnels. At first, I figured I'd tunnel directly to
the various OpenStack API services but that didn't work because the
endpoint URLs returned by keystone obviously wouldn't point to my
tunnelled connections.

Ok, let's just use a HTTP proxy, that should be fine. But no, not on yak
shaving day. For some reason, I was getting 403 Forbidden errors.

To cut a long story short, it turns out:

-   httplib2 always uses HTTP CONNECT tunneling rather than just sending
    the requests directly to the proxy
-   squid by default and, indeed, our corporate proxy defaults to
    rejecting CONNECT for ports other than 443
-   The recently released httplib2 0.7.5 has a
    PROXY\_TYPE\_HTTP\_NO\_TUNNEL which only uses CONNECT tunnelling for
    port 443, but it doesn't use this type when you configure your proxy
    via http\_proxy in the environment

Not content with shaving the yak once, I shaved her thrice:

-   An upstream [patch to use
    HTTP\_NO\_TUNNEL](http://code.google.com/p/httplib2/issues/detail?id=228)
    when using http\_proxy env
-   A [request](https://bugzilla.redhat.com/857514) to get the patch
    into Fedora
-   A [patch to work around
    it](https://bugs.launchpad.net/python-novaclient/+bug/1051007) in
    python-novaclient

One other troubling conclusion is that if you're exposing the services
over HTTPS, you really should use port 443 for everything or clients
won't be able to connect over many proxies.
