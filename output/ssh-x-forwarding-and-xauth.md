Title: SSH, X Forwarding and Xauth
Date: 2005-02-25 09:11
Author: markmc
Category: General
Slug: ssh-x-forwarding-and-xauth
Status: published

Discovered something interesting yesterday while trying to figure out  
why [Sabayon](http://www.gnome.org/projects/sabayon) wasn't  
working for jdennis over SSH:

-   With `ssh -Y`, the SSH server creates a proxy X server to  
   your local display which is just like any other SSH tunnel. Then  
   it points `$DISPLAY` at the tunnel,  
   e.g. `DISPLAY=:10`
-   In order for you to have permission to access the local display,  
   though, it also needs to add an xauth cookie your \~/.Xauthority on  
   the remote host.
-   The interesting part is that it doesn't do what you might assume  
   and just forward your xauth cookie for the local display to the  
   remote host. Instead it creates another cookie, sends that to the  
   remote host and its that cookie which gets merged to your  
   \~/.Xauthority. When you try and connect from the remote host to
    the  
   local display over the tunnel, the SSH client compares the cookie  
   in the first protocol message and if it matches the one it  
   generated for the tunnel, it swaps that cookie with the original  
   cookie and allows the connection to complete.

At first that might just seem like misguided paranoid delusional  
crackrock, but it does actually make sense. With this cool trick, if  
you SSH to a compromised machine (i.e. a machine where an attacker can  
access you \~/.Xauthority), then your display is only vulnerable while  
you remain logged in. Once you log out again, the compromised cookie  
is useless.
