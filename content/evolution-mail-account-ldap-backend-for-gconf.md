Title: Evolution Mail Account LDAP Backend For GConf
Date: 2005-04-14 14:30
Author: markmc
Tags: GNOME
Slug: evolution-mail-account-ldap-backend-for-gconf
Status: published

(Jaysus, thats a very long name for a few hundred lines of  
code)

I've just finished hacking on what was a really interesting little  
project. Basically, its a GConf backend which uses information in  
the user's LDAP entries to generate the mail account configuration for  
Evolution. The idea is that if you've a large number of users, all you  
have to do is stick each user's email address, incoming mail server and  
outgoing mail server in her LDAP entry and Evolution should just  
magically work.

I'm really happy with how well this thing turned out. I mean, it  
actually works, it didn't take much code, there wasn't anything  
lurking in GConf or Evo waiting to stab me in the back ... and, most  
of all, it should actually be very useful.

The code is in
[evolution-gconf-ldap-backend](http://cvs.gnome.org/viewcvs/evolution-gconf-ldap-backend/)  
in GNOME CVS and more details are in the
[README](http://cvs.gnome.org/viewcvs/*checkout*/gconf/backends/README.evoldap).

What's more, Dave Malcolm has also written some [cool  
scripts](http://lists.ximian.com/archives/public/evolution-hackers/2005-April/005427.html)
to solve the same problem, but without LDAP.
