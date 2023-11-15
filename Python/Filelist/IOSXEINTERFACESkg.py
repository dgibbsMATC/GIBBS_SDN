#Author: Kaden G
#Description: IOS XE RESCONF Interfaces

import requests
import json

def getIntRest(ipAddr):
    nameIP = []

    url = "https://" + ipAddr + ":443/restconf/data/ietf-interfaces:interfaces"

    username = 'developer'
    password = 'C1sco12345'
    payload={}
    headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm'
    }

    response = requests.request("GET", url, auth = (username,password), verify = False, headers=headers, data=payload).json()

    for device in response["ietf-interfaces:interfaces"]["interface"]:
        for value in device["ietf-ip:ipv4"].values():
            ipValues = value[0]
            nameIP.append({"Name": device["name"], "Ip": ipValues["ip"]})

    return nameIP

def getIntRestMAC(ipAddr):
    nameMAC = []

    url = "https://" + ipAddr + ":443/restconf/data/interfaces-state"

    username = 'developer'
    password = 'C1sco12345'
    payload={}
    headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm'
    }

    response = requests.request("GET", url, auth = (username,password), verify = False, headers=headers, data=payload).json()

    for device in response["ietf-interfaces:interfaces-state"]["interface"]:
        nameMAC.append({"Name": device["name"], "MAC": device["phys-address"]})
   
    return nameMAC

def combineIntLists(intStateList, intList):
    combinedList = []

    for item in intList:
        for item2 in intStateList:
            if item["Name"] == item2["Name"]:
                combinedList.append({"Name": item["Name"], "Ip": item["Ip"], "MAC": item2["MAC"]})
                
    return combinedList  

def printList(combinedIntList):
    print("Int" + " "*18 + "IP" + " "*14 + "MAC")
    print("-"*55)
    for device in combinedIntList:
        print(f"{device['Name']:20} {device['Ip']:15} {device['MAC']}")


ipAddr = "10.10.20.48"

intList = getIntRest(ipAddr)

intStateList = getIntRestMAC(ipAddr)

combinedIntList = combineIntLists(intStateList, intList)

printList(combinedIntList)

# for device in intDict["ietf-interfaces:interfaces"]["interface"]:
#         for value in device["ietf-ip:ipv4"].values():
#             if not value:
#                 print()
#             else:
#                 ipValues = interface["ietf-ip:ipv4"]["address"][0]
#                 print(f"{interface['name']:20} {ipValues['ip']:15} {ipValues['netmask']}")