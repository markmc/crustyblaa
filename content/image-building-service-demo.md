Title: Image Building Service Demo
Date: 2012-12-12 11:42
Author: markmc
Tags: OpenStack
Slug: image-building-service-demo
Status: published

Martyn Taylor and Steven Hardy have done an awesome job of [demoing an
Image Building Service for
OpenStack](http://lists.openstack.org/pipermail/openstack-dev/2012-December/003901.html):

http://www.youtube.com/watch?v=MdBM4HA3QUk

I think this has huge potential. Imagine an OpenStack API to which you
could send a request for a fresh image build of any OS, request specific
packages, software or other content to be included and have that image
be uploaded to Glance or Cinder once it's built. The image gets built in
the cloud on a Nova instance/VM and the cloud provider bills you for the
compute and I/O resources needed to complete the build.
