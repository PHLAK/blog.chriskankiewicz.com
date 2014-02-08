Title: Increasing the Size of a Virtual Hard Drive in VirtualBox
Date: 2011-11-16 08:59
Author: Chris Kankiewicz
Category: Software
Tags: Virtual Machine, VirtualBox, VM, Windows 7, Development
Slug: increasing-the-size-of-a-virtual-hard-drive-in-virtualbox

I work in Linux primarily but run a Windows 7 virtual machine in VirtualBox so I
can use Photoshop and do some necessary testing. Today my VM ran out of space.
Silly me thought 20GB would be enough, but after installing service pack 1,
dozens of Windows updates and a few programs I had less than 1GB of space left.
After a little searching I found an easy way to increase the size of a virtual
disk.

First, shut down your VM then run the following command from your host PC:

    $ VBoxManage modifyhd /path/to/guest.vdi --resize <size_in_mb>

Once completed, boot into your VM and (for Windows) open up Control Panel ->
Administrative Tools -> Computer Management. In Computer Management navigate to
Storage -> Disk Management then, in the right pane, right click your disk and
select "Extend Volume" and follow the prompts to resize your disk. And that's
it! Your disk will now be resized.

This also works from a Windows host, you just have to locate and use
VBoxManage.exe

**Note:** This method only allows you to INCREASE the size of a virtual disk.
You cannot shrink one with this method.
