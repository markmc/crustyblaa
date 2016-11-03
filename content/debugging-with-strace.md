Title: Debugging With Strace
Date: 2005-05-25 11:44
Author: markmc
Tags: GNOME
Slug: debugging-with-strace
Status: published

I just check in a [short
doc](http://cvs.gnome.org/viewcvs/*checkout*/vino/docs/debugging.txt?rev=1.1)
explaining some tricks to use when debugging Vino.

I got a bit side tracked explaining how you can figure out what messages
are being sent back and forth to the X server, just by looking at the
`read()`s and `write()`s in the strace. A snippet:

    [markmc@blaa ~]$ grep -rn X_QueryExtension /usr/include/X11/Xproto.h
    2091:#define X_QueryExtension               98

      That's 0x62 in hex. So, we're looking for a write to the X
    connection (file descriptor 3) with 0x62 as the first byte. What do ya
    know:

    1117012824.950683 writev(3, [{"\x62\x01\x04\x00\x06\x00\x01\x00", 8}, {"DAMAGE", 6}, {"\x00\x00", 2}], 3) = 16
    1117012824.950939 read(3, "\x01\x00\x52\x00\x00\x00\x00\x00\x01\x9d\x75\xba\x00\x00"..., 32) = 32

      It's pretty clear that its QueryExtension for DAMAGE. Now, lets
    figure out the event base from the reply. The format for the reply is:

    typedef struct {
        BYTE type;  /* X_Reply */
        BYTE pad1;
        CARD16 sequenceNumber B16;
        CARD32 length B32; /* 0 */
        BOOL  present;
        CARD8 major_opcode;
        CARD8 first_event;
        ...
    } xQueryExtensionReply;

       first_event is 11 bytes in. Looking at the read, that's 0x75. The
    value of XDamageNotify is zero, so we can be 100% sure that all those
    events after our NoExpose events are XDamageNotify events.

</p>
Some people might find it interesting. Others will think I'm weird and
tell me to use something like xscope.
