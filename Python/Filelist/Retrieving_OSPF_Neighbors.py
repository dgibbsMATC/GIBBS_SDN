#Author: Kaden Ganser, Logan Sutton, and David Gibbs
#Decription: Getting OSPF neighbor information and printing out with formatting

# import modules
import requests
import json
import urllib3

#disable login warning
urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# function to authenticate and connect to designated switches and execute a "show ip ospf neighbors" command taken from API
def getOSPFNeighbor(mgmtIPAddress):
    switchuser='cisco'
    switchpassword='cisco'

    url='https://' + mgmtIPAddress + '/ins'
    myheaders={'content-type':'application/json-rpc'}
    payload=[
        {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
        "cmd": "sh ip ospf nei",
        "version": 1
        },
        "id": 1
        },
        
        {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
        "cmd": "show version",
        "version": 1
        },
        "id": 2
        }
            ]
    
# def getVersion(mgmtIPAddress):
#     switchuser='cisco'
#     switchpassword='cisco'

#     url='https://' + mgmtIPAddress + '/ins'
#     myheaders={'content-type':'application/json-rpc'}
#     payload=[
#   {
#     "jsonrpc": "2.0",
#     "method": "cli",
#     "params": {
#       "cmd": "show version",
#       "version": 1
#     },
#     "id": 1
#   }
# ]


# json returned and assigned to variable
    response = requests.post(url,data=json.dumps(payload), verify=False, headers=myheaders,auth=(switchuser,switchpassword)).json()


# function to format and print table headers
def printOSPFNeighbor(neighbors):
    print("RouterID\t" + "Neighbor IP\t" + "Int\t", end = ' ')
    print()
    print('-' *45)
    table = neighbors['result']['body']['TABLE_ctx']['ROW_ctx']['TABLE_nbr']['ROW_nbr']
    print(f"{table[0]['rid']:15}", f"{table[0]['addr']:15}", f"{table[0]['intf']}")
    print(f"{table[1]['rid']:15}", f"{table[1]['addr']:15}", f"{table[1]['intf']}")

#Main

devices = [
    
    {   
        "Host": "dist-sw01",
        "Type": "Switch",
        "mgmtIP": "10.10.20.177"
    }, 
            
    {
        "Host": "dist-sw02",
        "Type": "Switch",
        "mgmtIP": "10.10.20.178"
    }

]






