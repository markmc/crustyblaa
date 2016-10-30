Title: Vino
Date: 2004-02-05 10:27
Author: markmc
Category: General
Slug: vino
Status: published

I've just imported *Vino* into CVS. Its "Remote Desktop" functionality  
for GNOME using VNC's [RFB](http://www.realvnc.com/docs/rfbproto.pdf)  
protocol which I wrote while at Sun.

Currently, the most notable bits over other VNC servers are:

-   Support for encrypting the RFB protocol stream using SSL
-   A dialog which prompts the user before allowing a remote user  
   to connect
-   Exports the local display, so you don't have to start up a  
   seperate VNC display
-   Properly integrated into GNOME

More details  
[  
here](http://www.gnome.org/~markmc/remote-desktop.txt).

The  
[  
TODO](http://cvs.gnome.org/bonsai/cvsblame.cgi?file=vino/docs/TODO) list
includes:

-   Use the new [  
   DAMAGE](http://freedesktop.org/Software/XDamage) extension instead
    of polling the screen
-   Write a GTK+ based client - the current client is a Java applet  
   but you can use any other vncviewer without encryption
-   Service discovery using DNS-SD and mDNS
-   Better authentication schemes

