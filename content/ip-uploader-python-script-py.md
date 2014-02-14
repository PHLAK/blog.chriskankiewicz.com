Title: IP Uploader – Python Script (.py)
Date: 2008-09-30 15:23
Author: Chris Kankiewicz
Category: Code
Tags: Code, Cox, Dynamic IP, Python, Script, VNC
Slug: ip-uploader-python-script-py

**NOTE:** This script can now be found here:
[https://gist.github.com/826108](https://gist.github.com/826108)

This is my first python script I ever wrote. This script connects to
[whatismyip.com](http://whatismyip.com), fetches the external IP address of the
network you are on, puts it into a text file and uploads it via FTP to any
server you want.

At home I have Cox, therefore I have a dynamic IP. Even though this IP only
changes about once every month, I got sick of needing to connect to my home
computer via VNC and not being able because my IP had changed. Therefore I
created the following script and set up a scheduled task on my home computer to
run this script every hour.

After running this script, you can then use PHP (or any similar language) to
include this file into any page you desire.

    #! /usr/bin/env python
    import httplib
    import sys
    import os
    import ftplib

    file="ip.txt"

    conn = httplib.HTTPConnection("www.whatismyip.com")
    conn.request("GET","/automation/n09230945.asp")
    response = conn.getresponse()
    data = response.read()

    filename = str(os.path.abspath(os.path.dirname(sys.argv[0])) + "\\"+file) #Create file
    FILE = open(filename,"w") #Open file ready for writing
    FILE.writelines(data) #Write 'data' to file
    FILE.close() #Close file

    #Replace [server], [user], and [pass] with your information.
    s = ftplib.FTP('[server]','[user]','[pass]') #Connect
    f = open(file,'rb') #File to send
    s.storbinary('STOR '+file, f) #Send the file
    f.close() #Close file and FTP
    s.quit() #Quit FTP

    sys.exit(0)

Shouts to Automated Penguin and Nak!
