Title: Checksums, Scatter-Gather I/O and Segmentation Offload
Date: 2008-05-28 09:09
Author: markmc
Tags: KVM
Slug: checksums-scatter-gather-io-and-segmentation-offload
Status: published

When dealing with virtualization and networking in the kernel, a number
of fairly difficult concepts come up regularly. Last week, while
tracking down some bugs with [KVM](http://kvm.qumranet.com/) and
[virtio](http://lwn.net/Articles/239238/) in this area, decided to write
up some notes on this stuff.

Thanks to [Herbert Xu](http://gondor.apana.org.au/~herbert/) for
checking over these.

Also, a good resource I came across while looking into this stuff is
[Dave Miller's How SKBs
Work](http://vger.kernel.org/~davem/skb_data.html). If you don't know
your headroom from your tailroom, that's not a bad place to start.

### Checksumming

TCP (and other protocols) have a checksum in its header which is a sum
of the TCP header, payload and the "pseudo header" consisting of the
source and destination addresses, the protocol number and the length of
the TCP header and payload.

A TCP checksum is the inverted ones-complement sum of the pseudo header
and TCP header and payload, with the checksum field set to zero during
the computation.

Some hardware can do this checksum, so the networking stack will pass
the packet to the driver without the checksum computed, and the hardware
will insert the checksum before transmitting.

Now, with (para-)virtualization, we have a reliable transmission medium
between a guest and its host and any other guests, so a PV network
driver can claim to do hardware checksumming, but just pass the packet
to the host without the checksum. If it ever gets forwarded through a
physical device to a physical network, the checksum will be computed at
that point.

What we actually do with virtualization is compute a partial checksum of
everything except the TCP header and payload, invert that (getting the
ones-complement sum again) and store that in the checksum field. We then
instruct the other side that in order to compute the complete checksum,
it merely needs to sum the contents of the TCP header and payload
(without zeroing the checksum field) and invert the result.

This is accomplished in a generic way using the csum\_start and
csum\_offset fields - csum\_start denotes the point at which to start
summing and csum\_offset gives the location at which the result should
be stored.

### Scatter-Gather I/O

If you've ever used readv()/writev(), you know the basic idea here.
Rather than passing around one large buffer with a bunch of data, you
pass a number of smaller buffers which make up a larger logical buffer.
For example, you might have an array of buffer descriptors like:

        struct iovec {

            size_t iov_len;     /* Number of bytes to transfer */

            void  *iov_base;    /* Starting address */

        };

In the case of network drivers, (non-linear) data can be scattered
across page size fragments:

        struct skb_frag_struct {

            struct page *page;

            __u32 page_offset;

            __u32 size;

        };

sk\_buff (well, skb\_shared\_info) is designed to be able to hold a 64k
frame in page size\[1\] fragments (skb\_shinfo::nr\_frags and
skb\_shinfo::frags). The NETIF\_F\_SG feature flag lets the core
networking stack know that the driver supports scatter-gather across
this paged data.

Note, the skb\_shared\_info frag\_list member is not used for
maintaining paged data, but rather it is used for fragmentation
purposes. The NETIF\_F\_FRAGLIST feature flag relates to this.

Another aspect of SG a flag, NETIF\_F\_HIGHDMA, which specifies whether
the driver can handle fragment buffers that were allocated out of high
memory.

You can see all these flags in action in dev\_queue\_xmit() where if any
of these conditions are not met, skb\_linearize() is called which
coalesces any fragments into the skb buffer.

<small>\[1\] - These are also known as non-linear skbs, or paged skbs.
This what "pskb" stands for in some APIs.</small>

### Segmentation Offload

TCP Segmentation Offload (TSO). UDP Fragmentation Offload (UFO). Generic
Segmentation Offload (GSO). Yeah, that stuff.

TSO is the ability of some network devices to take a frame and break it
down to smaller (i.e. MTU) sized frames before transmitting. This is
done by breaking the TCP payload into segments and using the same IP
header with each of the segments.

GSO is a generalisation of this in the kernel. The idea is that you
delay segmenting a packet until the latest possible moment. In the case
where a device doesn't support TSO, this would be just before passing
the skb to the driver. If the device does support TSO, the unsegmented
skb would be passed to the driver.

See dev\_hard\_start\_xmit() for where dev\_gso\_segment() is used to
segment a frame before passing to the driver in the case where the
device does not support GSO.

With paravirtualization, the guest driver has the ability to transfer
much larger frames to the host, so the need for segmentation can be
avoided completely. The reason this is so important is that GSO enables
a much larger \*effective\* MTU between guests themselves and to their
host. The ability to transmit such large frames significantly increases
throughput.

An skb's skb\_shinfo contains information on how the frame should be
segmented.

gso\_size is the size of the segments which the payload should be broken
down into. With TCP, this would usually be the Maximum Segment Size
(MSS), which is the MTU minus the size of the TCP/IP header.

gso\_segs is the number of segments that should result from
segmentation. gso\_type indicates e.g. whether the payload is UDP or
TCP.

drivers/net/loopback.c:emulate\_large\_send\_offload() provides a nice
simple example of the actions a TSO device is expected to perform - i.e.
breaking the TCP payload into segments and transmitting each of them as
individual frames after updating the IP and TCP headers with the length
of the packet, sequence number, flags etc.
