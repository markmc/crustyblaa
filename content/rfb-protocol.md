Title: RFB Protocol
Date: 2004-02-06 18:12
Author: markmc
Category: General
Slug: rfb-protocol
Status: published

So, I had a discussion with the RFB protocol maintainers at  
[RealVNC](http://www.realvnc.com) about getting the  
new RFB security types - which I added in Vino for doing the  
encryption thing - registered in the protocol. As far as I can  
make out at this point:

-   There are more security types registered than appear in  
   the protocol specification.
-   Security types 1-16 are reserved for "standard" security  
   types.
-   A security type becomes "standard" when it is added to the  
   "reference implementation" ... which just happens to be  
   the same product RealVNC is trying to make money from.

I can't make up my mind whether I care about this or whether  
I should just leave sleeping dogs lie. My main worry is what  
happens if we decide there are other additions we want to make  
to the protocol. Oh well, cross that bridge when we come to it.  
The RealVNC guys are friendly, so I don't expect there would  
actually be problems.

In the end, we agreed that I had to use different numbers to  
identify the new security types and I had to modify the way  
the new security type actually worked. End result - I've just  
pushed a new version of Vino with incompatible changes in the  
protocol.
