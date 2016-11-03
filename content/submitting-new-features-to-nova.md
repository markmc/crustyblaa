Title: Submitting new features to Nova
Date: 2012-08-20 11:27
Author: markmc
Tags: OpenStack
Slug: submitting-new-features-to-nova
Status: published

I just wrote down a few pieces advice for someone submitting a large
feature patch to Nova, so I thought I'd re-post it here:

-   Think about what it is like to be a nova-core reviewer looking at a
    list of 40 to 60 reviews and having maybe 2 hours today to
    do reviews. Think about how to make it more likely that such a
    reviewer will choose your code to review.
-   Small patches are easier to consume. The smaller you make the patch,
    the more likely it is that it will get reviewed quickly.
-   Break your changes into a series of [small, self-contained
    changes](http://wiki.openstack.org/GitCommitMessages#Structural_split_of_changes).
-   The earlier in the release cycle you can begin submitting some of
    your changes the better. Don't wait until all of your changes are
    finished before submitting.
-   Do as much of your design discussion in the open, preferably on the
    [openstack-dev mailing
    list](http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-dev).
    If you have discussions on the phone or IRC, try and post a summary
    of those discussions to the  
   mailing list.
-   Holding a design summit session to discuss your changes in advance
    is a great idea, but don't assume that everybody who may have an
    opinion on your changes is present. Also, bear in mind that
    someone's quick opinion offered at a design summit session may be
    very different from their considered opinion after reviewing the
    code in detail.
-   Finally, try and participate in the project beyond just making the
    changes you need. Review other peoples' changes in gerrit and offer
    your opinions, participate in design discussions on the mailing
    lists, fix bugs you come across, triage bug reports, etc. etc. All
    of this will allow other developers to get to know you, trust your
    judgement and review your changes more quickly. You will also learn
    more by interacting with other developers.

