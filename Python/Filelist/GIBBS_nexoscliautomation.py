#Author: Kaden G, Logan N, David G
#Description: NEXOS CLI Automation

# import modules
import requests
import json
import urllib3

# disable device warning on login
urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# function pulled from API for "show ip int br" on the given management IP; returns the info in a json file.
def shIntBri(mgmt_IP):
    switchuser='cisco'
    switchpassword='cisco'

    url='https://' + mgmt_IP + '/ins'
    myheaders={'content-type':'application/json-rpc'}
    payload=[
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
        "cmd": "show ip interface brief",
        "version": 1
        },
        "id": 1
    }
    ]

    response = requests.post(url,data=json.dumps(payload), verify=False,headers=myheaders,auth=(switchuser,switchpassword)).json()
    return(response)


# function to format and display specific headers for info pulled from the returned dictionary
def printInterfaces(interfaces):

    print("Name" + " "*5 + "Proto" + " "*5 + "Link" + " "*5 + "Address")
    print("----" + " "*5 + "-----" + " "*5 + "----" + " "*5 + "-------")

    for dict in interfaces['result']['body']['TABLE_intf']["ROW_intf"]:
        print(f"{dict['intf-name']:8} {dict['proto-state']:10} {dict['link-state']:8} {dict['prefix']}")

# function to verify interface                 
def checkInt(interfaces, changeInt):
    validInt = False
    for device in interfaces['result']['body']['TABLE_intf']["ROW_intf"]:
        if changeInt == device['intf-name']:
            validInt = True

    return validInt

# function to check IP address format        
def checkIP(newIP):
    ipCheck = 0
    splitIp = newIP.split(".") 
    ipLen = len(splitIp) 
    if ipLen == 4: 
        for octet in splitIp:
            if int(octet) <= 255:
                if octet.isdigit():
                    ipCheck += 1      
    else:
        validIP = False

    if ipCheck == 4: 
            validIP = True
    elif ipCheck >=1 and ipCheck <=3: 
            validIP = False

    return validIP

# function to connect to device, enter configuration mode and update the requested interface to the requested IP address.
def changeAddress(mgmt_IP, changeInt, newIP):
    
    switchuser='cisco'
    switchpassword='cisco'

    url='https://' + mgmt_IP + '/ins'
    myheaders={'content-type':'application/json-rpc'}
    payload=[
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
        "cmd": "conf t",
        "version": 1
        },
        "id": 1
    },
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
        "cmd": "interface " + changeInt,
        "version": 1
        },
        "id": 2
    },
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
        "cmd": "ip add " + newIP + " 255.255.255.0",
        "version": 1
        },
        "id": 3
    }
    ]

    response = requests.post(url,data=json.dumps(payload), verify=False, headers=myheaders,auth=(switchuser,switchpassword)).json()
    return response


#main **************************************************************************************************

# variable assigned to device, call sent to shIntBri function to get command output in json/dictionary form.
mgmt_IP = "10.10.20.177"
interfaces = shIntBri(mgmt_IP)
printInterfaces(interfaces)

# logic flow and user input for an interface to update
validInt = False
while validInt == False:
    changeInt = input("What interface would you like to change? ")
    validInt = checkInt(interfaces, changeInt)
    if validInt == False:
        print("Enter a valid Interface")

# logic flow and loop to get input from user for an updated IP address; assign input to a variable and send to checkIP function for verification.
validIP = False
while validIP == False:
    newIP = input("Enter a new IP: ")
    validIP = checkIP(newIP)
    if validIP == False:
        print("Bad IP, please re-enter a valid IP")

# defines info to be sent to changeAddress function and sends it
changeAddress(mgmt_IP, changeInt, newIP)

# Send updated info to device again; format and print output as a table again
interfaces = shIntBri(mgmt_IP)
printInterfaces(interfaces)


