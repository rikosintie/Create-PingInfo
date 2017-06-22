# Create-PingInfo
Takes the output from `show cdp ne det | i Dev|IP a` from a core switch and returns a sorted list of IP Address and hostnames of the CDP neighbors.

This is useful when you show up at a customer site you aren't familiar with and need to log into several edge switches. Instead of having to look through the raw output of the switch you get a consolidated list with just an IP address and hostname.

The output is formatted to work with Nirsoft.net's PingInfoView.

PingInfoView is a free tool for Windows from [Nirsoft PingInfoView](http://www.nirsoft.net/utils/multiple_ping_tool.html) that
allows you to ping multiple hosts at one time. It is a really great tool.

I use it during core switch cutovers to make sure that all servers/switches/devices are up after the cutover. To manually create the list of switches at a large site is time consuming but this script will do it in a second.

**Usage**:

Note: Occasionlly I have seen a switch return one IP address instead of two for a switch. Rerunning the show command usually corrects the issue.

The script takes the output from a `show cdp neighbor detail | i Dev|IP a` and turns it into the input needed
by PingInfoView.

On Windows `py pinginfo.py`

On Linux `python3 pinginfo.py`

Exmaple of `show cdp neighbor detail | i Dev|IP a` on a newer IOS
In this case enter 2 when prompted by the script
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
Older IOS versions will display this. In this case enter 1 when prompted by the script.
```
Device ID: test-MDF1
  IP address: 10.52.1.10
Device ID: test-IDF1
  IP address: 10.52.1.20
Device ID: test_4-Post
  IP address: 10.52.1.30
```

Script output from an older IOS version:
```
mhubbard@1S1K-SYS76:~/Dropbox/Python/Scripts$ python3 pinginfo.py

Enter the number of IP addresses per switch 1 or 2: 1

10.52.1.10 test-MDF1
10.52.1.20 test-IDF1
10.52.1.30 test_4-Post
 ```

for use with PingInfoView, either save the output to a file for future use or click File, Ping Options and paste it in. 
