#Author: Kaden Ganser
#Description: YANG

import requests
import json

def getInts(deviceIP):
    url = "https://" + deviceIP + ":443/restconf/data/ietf-interfaces:interfaces"

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

def printInt(intDict):
    for device in intDict["ietf-interfaces:interfaces"]["interface"]:
        name = device["name"]
        for list in device["ietf-ip:ipv4"].values():
            for address in list:
                ip = address["ip"]
                netmask = address["netmask"]
                print(f"{name:20} {ip:15} {netmask}")

deviceIP = "10.10.20.48"
intDict = getInts(deviceIP)
printInt(intDict)
