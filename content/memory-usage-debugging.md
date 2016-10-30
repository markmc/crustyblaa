Title: Memory Usage Debugging
Date: 2005-05-10 12:43
Author: markmc
Category: General
Slug: memory-usage-debugging
Status: published

There's been a lot of talk about reducing memory usage in GNOME, so  
some people may be interested in the [little  
adventure](http://mail.gnome.org/archives/desktop-devel-list/2005-May/msg00052.html)
I had this morning tracking down a mysterious 10M that  
appeared in gnome-panel's memory map in FC4.

Update: I better clarify that to avoid misunderstandings ... this is  
10M of unused virtual memory, not physical memory. The kernel would  
only have ever allocated a handful of physical pages in this space.  
This does not mean that GNOME now uses 10M less of your RAM.
