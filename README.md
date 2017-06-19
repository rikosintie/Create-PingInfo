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
Device ID: Test-IDFM8-M8-1
  IP address: 192.168.10.90
Device ID: Test-IDFU3-U3-1
  IP address: 192.168.10.150
Device ID: Test-IDFM5-M5-1
  IP address: 192.168.10.100
Device ID: Test-IDFT2-T2-1
  IP address: 192.168.10.160
Device ID: Test-IDFM4-M4-1
  IP address: 192.168.10.70
Device ID: Test-IDFL_DataRmL-1
  IP address: 192.168.10.60
```  
Script output:
```
mhubbard@1S1K-SYS76:~/Dropbox/Python/Scripts$ python3 pinginfo.py
 192.168.10.90 Test-IDFM8-M8-1
 192.168.10.150 Test-IDFU3-U3-1
 192.168.10.100 Test-IDFM5-M5-1
 192.168.10.160 Test-IDFT2-T2-1
 192.168.10.70 Test-IDFM4-M4-1
 192.168.10.60 Test-IDFL_DataRmL-1
 ```

Either save the output to a file for future use or click File, Ping Options and paste it in. 
