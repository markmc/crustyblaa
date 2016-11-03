Title: LDAP Notifications
Date: 2006-01-24 04:18
Author: markmc
Tags: Fedora
Slug: ldap-notifications
Status: published

Figuring out what the story is with LDAP notifications isn't terribly
easy. There are a number of different protocol extensions out there:

-   Netscape's [Persistent
    Search](http://www.watersprings.org/pub/id/draft-smith-psearch-ldap-01.txt)
    or *PSEARCH*. [Fedora Directory
    Server](http://directory.fedora.redhat.com) supports this. Extends
    the standard searchRequest such that it doesn't complete
    immediately, and returns any changes to the matched by the search.
-   [Triggered Search
    Control](http://www.watersprings.org/pub/id/draft-ietf-ldapext-trigger-01.txt)
    or *TSEARCH*. Not sure what implements this. Similar to psearch.
-   [Microsoft LDAP Control for Directory
    Synchronization](http://www.watersprings.org/pub/id/draft-armijo-ldap-dirsync-01.txt)
    or *DIRSYNC*. Implemented by Active Directory, but requires the
    client to poll for changes.
-   [LDAP Content Synchronization
    Operation](http://www.watersprings.org/pub/id/draft-zeilenga-ldup-sync-04.txt)
    or *SYNC*. Implemented by OpenLDAP and allows both polling and
    persistent modes.
-   [LDAP Client Update Protocol
    (RFC 3928)](http://www.ietf.org/rfc/rfc3928.txt) or *LCUP*. Similar
    to SYNC. Not sure who actually implements this.

The strangest thing about all this is that LCUP is the only one of these
that progressed from Internet Draft to RFC, yet neither OpenLDAP nor
Fedora Directory Server implement it. SYNC seems to have been proposed
by the OpenLDAP crew because when they went to implement LCUP they found
that it ["requires server implementations to maintain complete history
information in order to provide eventually convergent incremental
refreshes"](http://www.imc.org/ietf-ldup/mail-archive/msg01754.html),
which presumably wasn't something that OpenLDAP already did. Yet the
working group went ahead and progressed LCUP to RFC and not SYNC.

Anyway, moral of the story is that if you want notifications, then you
want PSEARCH if you're using Fedora Directory Server and SYNC if you're
using OpenLDAP.

If you're using OpenLDAP's client library, rather than the [Mozilla LDAP
C SDK](http://www.mozilla.org/directory/csdk.html), then it's a little
tricky since you have to manually create the psearch control and parse
the entryChange controls. Here's [some example
code](http://www.gnome.org/~markmc/code/test-ldap-psearch-notifications.c).
