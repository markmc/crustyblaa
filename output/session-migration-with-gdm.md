Title: Session Migration With GDM
Date: 2005-04-26 17:59
Author: markmc
Category: General
Slug: session-migration-with-gdm
Status: published

Last year [Caolan](http://blogs.linux.ie/caolan/index.php)  
and I demoed hotdesking with GDM and VNC.
[Owen](http://fishsoup.net/blog) later pointed out that VNC  
probably wasn't the way to go once the [rendering  
improvements](http://www.gnome.org/~seth/blog/xshots) they're working
come on line.

So, last week I picked up a patch I'd hacked up before Christmas,  
finished it off and committed it to GDM. The idea is to do the same  
thing as the VNC patch, but this time using a X proxy (like Xnest)  
server on the terminal server instead of a VNC server.

Specifically, though, the features added to GDM are:

-   You can now configure GDM to run XDMCP sessions on a local X  
   proxy server. This may be useful on its own for performance
    reasons;  
   in theory, at least, an X proxy server should be able to limit the  
   number of roundtrips it makes to the remote X server since if all
    you  
   want to do is query server state, then that state is local. I've no  
   idea yet how well Xnest and others do on this in practice, though.
-   If the proxy server supports disconnecting from its parent  
   display and re-connecting later, you can configure GDM such that
    you  
   can disconnect from your session and reconnect later simply by
    logging  
   back in. The only proxy server's that I know of which support this
    is  
   the [DMX](http://dmx.sf.net) X server and [NoMachine
    NX's](http://www.nomachine.com) nxagent. Its  
   certainly possible to do this with any proxy though; I had it half  
   done for Xnest before realizing DMX had good enough support to get
    the  
   GDM patch done.

I've played around a little today with NoMachine's proxy. You can try  
it out with GDM HEAD up by:

1.  Install NoMachine's server package
2.  Set `xdmcp/EnableProxy=true` in gdm.conf
3.  Download these scripts
    ([run-nxagent.sh](http://www.gnome.org/~markmc/code/run-nxagent.sh)  
   and
    [reconnect-nxagent.sh](http://www.gnome.org/~markmc/code/reconnect-nxagent.sh))  
   and stick them in `/tmp`
4.  Set `xdmcp/ProxyXServer` to  
   `ProxyXServer=/tmp/run-nxagent.sh -audit 0 -name NX -geometry 768x576`
    and `xdmcp/ProxyReconnect` to  
   `/tmp/reconnect-nxagent.sh`
5.  Re-start GDM
6.  From another machine run `X -query $server` and login  
   through the login screen
7.  Run `/tmp/reconnect-nxagent.sh --to :20` on the server to  
   disconnect your remote X server from the session
8.  Run `X -query $server` again on the server, login and you  
   should be immediately re-directed to your original session

