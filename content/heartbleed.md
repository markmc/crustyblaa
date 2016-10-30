Title: Heartbleed
Date: 2014-04-10 10:04
Author: markmc
Category: fedora, General, openstack
Slug: heartbleed
Status: published

Watching [\#heartbleed](http://heartbleed.com/) (aka
[CVE-2014-0160](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0160))
fly by in my twitter stream this week, I keep wishing we could all just
pause time for a couple of weeks and properly reflect on all the angles
here.

Some of the things I'd love to have more time to dig into:

-   Obviously, [the bug itself and its
    fix](http://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=96db902)
-   Why countermeasures in the kernel, libc or the compiler didn't
    prevent this, or how static analysis tools didn't catch it. (Update:
    see
    [here](http://www.tedunangst.com/flak/post/heartbleed-vs-mallocconf)
    and [here](http://article.gmane.org/gmane.os.openbsd.misc/211963))
-   The protocol design - some wonder why a seemingly application-level
    feature is included in such a critical security protocol and why the
    feature is available before authentication has completed.
    Interesting to note that one of the stated purposes of the feature
    is [PMTU discovery for
    DTLS](http://tools.ietf.org/html/draft-ietf-tls-dtls-heartbeat-04)
    yet it's enabled for plain TLS too
-   That it's not only servers which are vulnerable - [clients equally
    vulnerable](http://security.stackexchange.com/questions/55119/does-the-heartbleed-vulnerability-affect-clients-as-severely)
-   The fact that attacks can't be detected because there is no logging
    of this failure condition
-   The health of the OpenSSL project, [talk of its developers being
    irresponsible](http://article.gmane.org/gmane.os.openbsd.misc/211963)
    when it comes to their development practice
-   [How the bug was
    introduced](http://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=4817504),
    how much code review or testing was involved. (Update: [comments
    from the original author of the
    code](http://www.smh.com.au/it-pro/security-it/man-who-introduced-serious-heartbleed-security-flaw-denies-he-inserted-it-deliberately-20140410-zqta1.html))
-   The realization that few in our industry are actively investing in
    this project which so many place so much trust in
-   The question of whether OpenSSL is the library everyone should be
    relying on, whether it should be e.g. NSS or GnuTLS
-   How something like OpenSSL can be a critical part of a web service's
    architecture [even where e.g. the service is implemented with
    technologies like
    .NET](http://www.troyhunt.com/2014/04/everything-you-need-to-know-about.html)
-   The question of whether we're putting all our eggs in one basket if
    an SSL vulnerability can have such far reaching implications
-   Just how much was exposed by the vulnerability - e.g. private keys,
    usernames and passwords, other sensitive data - and how much data
    could have been compromised by a determined, well-resourced attacker
    in possession of this knowledge before it was patched
-   The [efficacy of certificate revocation
    measures](http://www.quora.com/OCSP-Online-Certificate-Status-Protocol/Is-it-better-to-enable-OCSP-and-leak-personal-information-or-disable-OCSP-and-risk-trusting-a-revoked-certificate/answer/Robert-Love-1?srid=cwn&share=1)
    in protecting users from potentially compromised certificates
-   How [Perfect Forward Security is an important mitigation
    measure](https://www.eff.org/deeplinks/2014/04/why-web-needs-perfect-forward-secrecy)
    for vulnerabilities like this
-   The [claim by one site that they could detect attacks in their
    logs](http://www.seacat.mobi/blog/heartbleed), that there was
    someone exploiting the vulnerability two weeks before it was
    disclosed publicly. (Thierry Carrez points out the update to this
    post which says "other tools \[..\] can produce the same pattern in
    the SeaCat server log")
-   How [our perception of a vulnerability like this has
    changed](http://oneverythings.blogspot.ie/2014/04/i-heartbleed-nsa.html)
    now that we know just how aggressive intelligence agencies (the NSA
    and others) are in their approach to population surveillance
    and monitoring. [This FOSDEM talk is rather
    prescient](http://ftp.belnet.be/FOSDEM/2014/Janson/Sunday/NSA_operation_ORCHESTRA_Annual_Status_Report.webm)
    in describing OpenSSL as the "crown jewels" for the NSA. (Update:
    [claims that the NSA knew of the bug soon after its introduction and
    exploited
    it](http://www.bloomberg.com/news/2014-04-11/nsa-said-to-have-used-heartbleed-bug-exposing-consumers.html))
-   The approach that was taken to disclosing the vulnerability, how
    responsible a disclosure process it was and the pros/cons of
    delaying disclosure further. [Apparently CloudFlare was disclosed
    before the public disclosure, whereas vendors like Red Hat
    weren't](http://www.eweek.com/security/heartbeat-ssl-flaw-puts-linux-distros-at-risk.html).
    (Update: [more details on the disclosure timeline from Kurt
    Seifried](http://www.openwall.com/lists/oss-security/2014/04/08/10))
    (Another update: [OpenSSL's official view of the
    timeline](https://plus.google.com/+MarkJCox/posts/TmCbp3BhJma)) (Yet
    another update: [interview with Codenomicon's David
    Chartier](http://www.vocativ.com/tech/hacking/behind-scenes-crazy-72-hours-leading-heartbleed-discovery/))
-   How effective entities like Linux distros were in helping getting
    the vulnerability quickly patched in the wild (see e.g. that [Stripe
    went and built their own patched
    package](https://stripe.com/blog/heartbleed) rather than wait for an
    Ubuntu package)
-   How much more difficult patching this was due to applications
    bundling OpenSSL and how much worse it could have been if the
    practice of bundling was more widespread
-   The impact that the [impressive
    marketing](http://www.kalzumeus.com/2014/04/09/what-heartbleed-can-teach-the-oss-community-about-marketing/) -
    i.e. a cool name vs simply a CVE number, a logo, clear technical
    writing which speaks to the business impact, etc. - had on the speed
    with which the patch was deployed

