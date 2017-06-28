'''
read a file 'pinginfo.txt' containing the output of sh cdp ne det | i Dev|IP a
It should look like this:

Device ID: test-MDF1
  IP address: 10.52.1.10
Device ID: test-MDF1
  IP address: 10.52.1.10
Device ID: test_IDF2_Conf
  IP address: 10.52.1.30

or this:

Device ID: SBHS-IDFL-LDAT-SW01
  IP address: 10.131.3.116
  IP address: 10.131.3.116
Device ID: S-131-IDFU3-U3-1
  IP address: 10.131.1.150
  IP address: 10.131.1.150
Device ID: S-131-IDFT2-T2-1
  IP address: 10.131.1.160
  IP address: 10.131.1.160
Device ID: S-131-IDFZ3-Z3-1
  IP address: 10.131.1.170
  IP address: 10.131.1.170
Print out the code needed to create the pinginfo file in the format: 
ip address hostname
'''
def remove_duplicates(x):
    a = []
    for i in x:
        if i not in a:
            a.append(i)
    return a

#create a space between the command line and the output
print()
#create a blank list to accept each line in the file
listname = []
f = open('pinginfo.txt', 'r')
for line in f:
    listname.append(line)
f.close
#remove blank line at end of list
while True:
  try:
    listname.remove('\n')
  except ValueError:
    break
items = len(listname)
'''
Determine if the output has 1 or 2 IP address statements.
If the third item in the list doesn't have IP in it then there is one IP address line.
'''
if listname[2].find('IP') == -1:
	numberofIPs = 2
else:
	numberofIPs = 3

#Build the end condition for the while loop.
items = len(listname)-1
#initalize the loop counter
counter = 0
sItems = []
while counter < items:
    #read in the first hostname line
    hostname = listname[counter]
    #remove the Device ID: from the hostname line.
    colon = hostname.find(':')
    colon = colon + 1
    hostname = hostname[colon:]
    #remove the newline from the hostname
    hostname = hostname.strip('\n')
    #The interface is on the next line
    IPaddress = listname[counter + 1]
    #Find the colon in IP Address line
    colon = IPaddress.find(':')
    colon = colon + 1
    #strip the colon out
    IPaddress = IPaddress[colon:]
    #delete the colon
    IPaddress = IPaddress.replace(':','')
    IPaddress = IPaddress.strip('\n')

#A Nexus doesn't put a space between the Device ID and hostname.
#If no space exists add one.
    if hostname.find(' ') == -1:
        hostname = ' ' + hostname
#create the output
    temp = IPaddress + hostname
 #   print(temp)
    sItems.append(temp)
#increment the counter to jump to the next hostname line
    counter = counter + numberofIPs
#
#sort by IP address
sItems.sort()
#remove duplicates
sItems = remove_duplicates(sItems)
#print results
for s in sItems:
    print(s)
print()