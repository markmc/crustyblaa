Title: REST API For RHEV-M
Date: 2010-06-21 21:44
Author: markmc
Tags: Red Hat, KVM
Slug: rest-api-for-rhev-m
Status: published

Today, [Eoghan Glynn](http://eoghang.blogspot.com/) and I [announced the
first milestone
release](https://fedorahosted.org/pipermail/rhevm-api/2010-June/000256.html)
of a [REST API for Red Hat Enterprise Virtualization
Manager](https://fedorahosted.org/rhevm-api/).

The only current API for RHEV-M is a Windows Powershell plugin which
provides a perfectly fine scripting interface for RHEV-M on Windows, but
isn't so easy to call remotely or to integrate with another application.
By adding a REST API, we're adding an integration interface which we
hope everyone will find convenient to use.

If you have a 2.2 installation of RHEV-M, it's a quick and painless
process to download our distribution, deploy the WAR to an Java EE
application server (e.g. JBoss EAP or AS) and play around with our
[Apache Felix
Karaf](http://felix.apache.org/site/apache-felix-gogo.html) based shell.
You can also read the [API reference
guide](http://markmc.fedorapeople.org/rhevm-api/en-US/html-single/index.html)
and jump on our [mailing
list](https://fedorahosted.org/mailman/listinfo/rhevm-api) to give us
feedback.

RHEV-M isn't yet an open-source project, so we've had to put a lot of
effort into making it possible to develop this REST API in the open.
We've concentrated our initial efforts on API design and building a
prototype implementation of the API on top of the Powershell interface
in 2.2. However, in time for the next release of RHEV-M, our plan is to
add a compatible implementation of the API directly to the RHEV-M
backend. At that time, the API will be a fully supported part of the
product.

If you care about integrating with RHEV-M, now is the time to get
involved with the API project. While the API is already quite well
defined, there is buckets of scope for design changes and adding new
features. And, most of all, we want your help!
