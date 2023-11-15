#Author: Kaden G, Logan S, with David G cheerleading
#Description: IOSXE Interfaces 2

import requests
import json
import urllib3

urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# identify and authenticate to device
def get_int_rest(ip_addr):
    url = "https://" + ip_addr + ":443/restconf/data/ietf-interfaces:interfaces"

    username = 'developer'
    password = 'C1sco12345'
    payload={}
    headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm'
    }

    response = requests.request("GET", url, auth = (username,password), verify = False, headers=headers, data=payload).json()

    return response

# Function to get list of interfaces and their management IP addresses
def print_dev_ints(int_list):
    for device in int_list["ietf-interfaces:interfaces"]["interface"]:
        name = device["name"]
        for list in device["ietf-ip:ipv4"].values():
            for address in list:
                ip = address["ip"]
                print(f"{name:20} {ip} ")

# Function to validate IPs
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

# Function to update given range of interfaces with new IP address
def update_dev_int(ip_addr,int_name,newIP):
    url = "https://" + ip_addr + ":443/restconf/data/ietf-interfaces:interfaces/interface="+ int_name
    username = 'developer'
    password = 'C1sco12345'
    payload={"ietf-interfaces:interface": {
                        "name": int_name,
                        "description": "Configured by RESTCONF",
                        "type": "iana-if-type:softwareLoopback",
                        "enabled": "true",
                                        "ietf-ip:ipv4": {
                                                                "address": [{
                                                                    "ip": newIP,
                                                                    "netmask": "255.255.255.252"
                                                                    
                                                                            }   ]
                                                            }
                                            }
            }

    headers = {
    'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm',
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
    }

    response = requests.request("PUT", url, auth=(username,password),headers=headers, verify = False, data=json.dumps(payload)
    )

#Main
ip_addr = "10.10.20.48"

#Get list of interfaces and IPs
int_list = get_int_rest(ip_addr)


#Print list and IPs
print_dev_ints(int_list)

#Gets int to change and verify
valid_int = True

while valid_int == True:
    int_name = input("Which interface do you want to modify? ")

    if int_name in str(int_list):
        valid_int = False
    else:
        print("Invalid interface name")

#Gets new IP and verifies
valid_IP = False

while valid_IP == False:
    newIP = input("Enter a new IP for " + int_name + ": ")
    valid_IP = checkIP(newIP)
    if valid_IP == False:
        print("Bad IP, please re-enter a valid IP")

update_dev_int(ip_addr,int_name,newIP)

#Reprint Updated Interface
int_list = get_int_rest(ip_addr)

print_dev_ints(int_list)
