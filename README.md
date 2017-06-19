# Create-PingInfo
Create strings to be used with Nirsoft.net PingInfoView from a Cisco show cdp ne det output

PingInfoView is a free tool for Windows from [Nirsoft](http://www.nirsoft.net/utils/multiple_ping_tool.html) that
allows you to ping multiple hosts at one time. It is a really great tool.

I use it during core switch cutovers to make sure that all servers/switches/devices are up after the cutover. 

**Usage**:

The script takes the output from a "show cdp neighbor detail | i Dev|IP add" and turns it into the strings needed
by PingInfoView.

Exmaple of show cdp neighbor detail | i Dev|IP add. Save this in a file called pinginfo.txt.
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

Either save the output to a file for future use or click File, Ping Options and paste it in. 
