#Author: Kaden G, Logan N, David G
#Description: NEXOS CLI

# function that takes user input IP address and updates it
def changeNumber(ip, offset, octet):
    splitIp = ip.split(".")
    octetValue = int(splitIp[octet-1]) + offset
    splitIp[octet-1] = str(octetValue)
    newIp = ".".join(splitIp)
    print(newIp)
    return(newIp)

#main *************************************************

# assign variable to user input IP address, the octet they want to change, and how much they want to change it by
ip = input("Enter an IP: ")
octet = input("Which octet do you want to change: ")
offset = input("Enter an offset to change the octet by: ")

# send input information to function changeNumber
changeNumber(ip, int(offset), int(octet))


