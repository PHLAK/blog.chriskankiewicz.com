Title: Turn your old PC into a hardware firewall with IPCop
Date: 2008-10-02 22:18
Author: Chris Kankiewicz
Category: Hardware, Software
Tags: CDBurnerXP, Firewall, Hardware, IPCop, Linux, PC, Software, Systm
Slug: turn-your-old-pc-into-a-hardware-firewall-with-ipcop

So you’ve got a 10-year old PC sitting around the house. You’re sick of your
cats always getting into the wires and knocking the darn thing over. You don’t
want to throw it away, but you just don’t know what to do with it. Well my
friend, why don’t you turn that thing into a new hardware firewall?!

How would you go about doing that you might ask, well I’ve got the solution for
you: **IPCop**!

## What is IPCop?

IPCop is a secure Linux distribution managed through a web-interface. It turns
an old PC into a firewall and VPN gateway. Features an Intrusion Detection
System. Check it out at [http://www.ipcop.org](http://www.ipcop.org/).


## What are the hardware requirements for IPCop?

I ran IPCop on an old system I had lying around. Specs:

  * Pentium 2
  * 320MB PC100/133 RAM
  * 20GB HDD (Overkill, but the smallest I had)
  * 2 NICs
  * ATI Rage 8MB Video Card *
  * CD ROM *
  * Cardboard and packaging tape (to keep as much cat/dog hair out as
    possible... and for STYLE!)

\* Only needed for install

The actual requirements are pretty low. You probably only need a 2-5GB hard
drive, smaller if don’t plan on keeping any logs. Also, if you’re not planning
on running the intrusion detection system, you could get away with 64MB of RAM
easily.

![Hardware Firewall Running IPCop](http://farm4.static.flickr.com/3191/2897432811\_f379a00d59.jpg)

## Where do I get it?

Go to [http://www.ipcop.org](http://www.ipcop.org/) and choose “Download” from
the menu on the left. This will forward you to a SourceForge page. Find the
latest version and download the .ISO file. You will then have to use some
[CD burning software](http://cdburnerxp.se/en/download) to burn the .ISO as a
bootable CD.

## How do I install IPCop?

IPCop couldn’t have been easier to install. You just pop the CD you burned in
the last step into your CD ROM drive and boot the computer. Make sure your
computer is set to boot from the CD drive first, otherwise this wont work. Once
the install CD boots, just follow the on-screen instructions. Most of the
options are pretty straigt forward, if you’re at all confused about any of it,
refer to the documentation found here:
[http://www.ipcop.org/index.php?module=pnWikka&tag=IPCopDocumentation](http://www.ipcop.org/index.php?module=pnWikka&tag=IPCopDocumentation)

Also, this episode of Systm was a great resource:
[http://revision3.com/systm/firewall/](http://revision3.com/systm/firewall/),
I highly recommend checking this out before you start your project.

## Got anything else?

Web interface screenshots @
[http://www.flickr.com/photos/kankie/sets/72157607445592055/detail/](http://www.flickr.com/photos/kankie/sets/72157607445592055/detail/)
