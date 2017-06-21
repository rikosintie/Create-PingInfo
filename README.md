# Create-PingInfo
Takes the output from `show cdp ne det | i Dev|IP a` from a core switchand returns a sorted list of IP Address and hostnames of the CDP neighbors.

This is useful when you show up at a customer site you aren't familiar with and need to log into several edge switches. Instead of having to look through the raw output of the switch you get a consolidated list with just an IP address and hostname.

The output is formatted to work with Nirsoft.net's PingInfoView.

PingInfoView is a free tool for Windows from [Nirsoft PingInfoView](http://www.nirsoft.net/utils/multiple_ping_tool.html) that
allows you to ping multiple hosts at one time. It is a really great tool.

I use it during core switch cutovers to make sure that all servers/switches/devices are up after the cutover. To manually create the list of switches at a large site is time consuming but this script will do it in a second.

**Usage**:

Note: Occasionlly I have seen a switch return one IP address instead of two for a switch. Rerunning the show command usually corrects the issue.

The script takes the output from a "show cdp neighbor detail | i Dev|IP a" and turns it into the input needed
by PingInfoView.

On Windows 'py pinginfo.py'

On Linux `python3 pinginfo.py`

Exmaple of `show cdp neighbor detail | i Dev|IP add` 

Save this in a file called pinginfo.txt.
```
Device ID: Test-IDFM-M1-SW01
  IP address: 10.131.3.112
  IP address: 10.131.3.112
Device ID: Test-IDFSE-SE1-SW01
  IP address: 10.131.3.115
  IP address: 10.131.3.115
Device ID: Test-IDFZ-Z3-SW01
  IP address: 10.131.3.117
  IP address: 10.131.3.117
Device ID: Test-IDFV-V3-SW01
  IP address: 10.131.3.108
  IP address: 10.131.3.108
Device ID: Test-IDFU-U3-SW01
  IP address: 10.131.3.109
  IP address: 10.131.3.109
```  
Script output:
```
mhubbard@1S1K-SYS76:~/Dropbox/Python/Scripts$ python3 pinginfo.py
 192.168.10.112 Test-IDFM-M1-SW01
 192.168.10.115 Test-IDFSE-SE1-SW01
 192.168.10.117 Test-IDFZ-Z3-SW01
 192.168.10.108 Test-IDFV-V3-SW01
 192.168.10.109 Test-IDFU-U3-SW01
 ```

for use with PingInfoView either save the output to a file for future use or click File, Ping Options and paste it in. 
