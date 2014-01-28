Title: Windows 7 Activation Hack
Date: 2011-07-19 21:18
Category: Software
Tags: Activation, Hack, Microsoft, Regedit, Registry, Windows 7
Slug: windows-7-activation-hack
Author: Chris Kankiewicz
Summary: Bypass Windows 7 activation limitations (legitimate key required)

When installing Windows 7 it's very picky about which installation disc you use
(Full vs. Upgrade) and if improperly matched with your key can prevent you from
activating your copy of Windows usually returning an "Invalid Product Key" error
message.  You may also see the same or similar error when you do a full, clean
installation with an upgrade disc.  This can be very annoying, especially when
you have a legitimate key and disc but just didn't install it the way Microsoft
thinks you should.  In the event that you are having trouble activating your
Windows 7 installation with a legitimate key, try the following registry hack:

  1. First make sure there are no pending tasks requiring a reboot.This is
     indicated by an orange shield icon next to your shutdown button on the
     Start menu or in the notification tray.
  2. Open the Registry Editor (Start ->  search for "regedit" and hit Enter)
  3. Navigate to the following registry key:

        HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Setup\OOBE

  4. Double click on `MediaBootInstall` in the right pane and change
     "Value data" to `0`
  5. Open a command prompt with administrative rights (Start ->  search for
     "cmd" and hit Enter)
  6. Run the following command to reset Windows activation status:

        slmgr -rearm

  7. Reboot your computer.
  8. Run the Activate Windows utility (Start -> search for "Activate Windows"),
     enter your upgrade product key and activate Windows.

**NOTE:** This activation hack will only work if you have a legitimate key.
This method wont help if you have a pirated copy of Windows.
