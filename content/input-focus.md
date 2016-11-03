Title: Input Focus
Date: 2005-06-14 12:16
Author: markmc
Tags: GNOME
Slug: input-focus
Status: published

The details of behind input focus and X/GTK+ have always confused the  
hell out of me. Its all fine and dandy when you only have to think  
about GTK+ focus, but whenever I had to think about the interaction  
between GTK+, the window manager and what's actually happening at the  
Xlib/Xserver level, by brain used to go to mush. I'd barely figure  
out the bits neccessary to fix whatever bug I was up against and  
promptly forget it all again five minutes later.

Well, this morning I have to get focus handling working with Xnest  
embedded in a GTK+ window. So, I figure I'm really going to have to  
understand it this time. Here's some of the details:

-   In order for any X window to receive events of a certain type,  
   you must call `XSelectInput()` on that window with the  
   appropriate event mask.
-   When a key event is generated, the Xserver tries to find a  
   client and window to deliver the event to. It starts with the  
   window which contains the pointer and recurses up through its  
   ancestors until it finds a window with that event selected.
-   X has the notion of "the keyboard focus window". This is set  
   using `XSetInputFocus()`. When a key event is generated,  
   the event is propopagated as normal if the focus window contains  
   the pointer, but propogation stops at the focus window. If the  
   focus window doesn't contain the pointer, the event is  
   delivered directly to the focus window.
-   What's important here is this has nothing to do with GTK+  
   keyboard focus. Its more about which toplevel window is  
   currently focused by the window manager, rather than which  
   widget is focused within the application. The [XEmbed  
   spec](http://www.freedesktop.org/Standards/xembed-spec) more or less
    redefines this as the window's "activation  
   state" - i.e. if a toplevel or its descendants is the current  
   keyboard focus window then the toplevel is said to be active.
-   None of this really reflects the way modern desktops and  
   toolkits work. What happens in reality is that applications  
   never focus themselves (i.e. `XSetInputFocus()`) unless  
   the window manager tells it to using the WM\_TAKE\_FOCUS ICCCM  
   ClientMessage.
-   On receipt of this message GTK+ makes a 1 pixel square window,  
   located just outside the visible area of the toplevel  
   window, be the keyboard focus window. That causes all  
   KeyPresses to always go straight to this window (the window  
   doesn't have any descendants which can contain the pointer).
-   When this window receives an X KeyPress event, GTK+ then  
   generates a GTK key press event (with the toplevel as the  
   target window) and puts that on the GTK event queue.
-   At this point the event is entirely in the hands of GTK+. X  
   has wiped its hands of the whole affair.
-   Each toplevel GtkWindow knows which widget within the window  
   is currently focused. All the toplevel now needs to do is  
   send that event onto the currently focused widget.

One last little interesting detail is how the window manager  
implements click-to-focus:

-   The WM establishes a pasive grab on each unfocused toplevel  
   window using `XGrabButton()`
-   A passive grab is where events are delivered as normal until a  
   specific key or button combination is pressed and an active grab  
   is established causing the event (and following events) to be  
   delived to the grabbing client.
-   The WM passes `GrabModeSync` to `XGrabButton()`  
   which causes all event delivery to freeze when the specific  
   key/button combination is pressed.
-   So, when a user clicks on an unfocused window, all subsequent  
   events are queued in the Xserver, the WM gets the ButtonPress,  
   focuses the toplevel of the window which was clicked in and  
   releases the event queue again using `XAllowEvents()`

In case its not obvious, I'm only really writing this down so there's  
less chance of me forgetting it all again :-)
