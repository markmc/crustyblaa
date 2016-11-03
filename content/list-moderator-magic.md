Title: List moderator magic
Date: 2004-03-31 11:14
Author: markmc
Tags: GNOME
Slug: list-moderator-magic
Status: published

I spent some time floundering about a while ago trying to figure out a  
Javascript hack to allow you to mark all mails in a mailman moderation  
queue to be discarded. I certainly wasn't going to manually click  
"Discard" for each of the 400 mails in the gconf-list queue.

[DV](http://www.advogato.org/person/DV) saved me with some  
[jamesh](http://www.advogato.org/person/jamesh) magic.

Mailing list admins, bookmark this link -  
[Discard all
mails]((function()%7Bvar%20elements=document.forms%5B0%5D.elements;for(var%20i=0;ielements.length;i++)%7Bvar%20el=elements%5Bi%5D;if(el.type=='radio'&&el.value=='3')%7Bel.checked=true;%7D%7D%7D)())

(No, don't click on the link. Right-click, "Bookmark link...")
