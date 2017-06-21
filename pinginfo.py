'''
read a file 'pinginfo.txt' containing the output of sh cdp ne det | i Dev|IP a
It should look like this:
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
#create a space between the command line and the output
print()
#create a blank list to accept each line in the file
listname = []
f = open('pinginfo.txt', 'r')
for line in f:
    listname.append(line)
f.close
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
    #Find the comma in IP Address line
    colon = IPaddress.find(':')
    colon = colon + 1
    #strip the comma out
    IPaddress = IPaddress[colon:]
    #delete the colon
    IPaddress = IPaddress.replace(':','')
    IPaddress = IPaddress.strip('\n')
    #print the information needed to create the interface description
    temp = IPaddress + ' ' + hostname
#    print(temp)
    sItems.append(temp)
#increment the counter by three to jump to the next hostname line
    counter = counter + 3
print()
sItems.sort()
for s in sItems:
    print(s)
