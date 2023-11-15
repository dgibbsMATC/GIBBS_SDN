import json

##sw01 = {'jsonrpc': '2.0', 'result': {'body': {'TABLE_intf':{'ROW_intf':
##        [{'vrf-name-out': 'default', 'intf-name': 'Vlan101', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up','iod': 71, 'prefix': '172.16.101.2', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default','intf-name': 'Vlan102', 'proto-state': 'up','link-state': 'up', 'admin-state': 'up', 'iod': 72, 'prefix': '172.16.102.2', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default', 'intf-name': 'Vlan103', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 73, 'prefix': '172.16.103.2', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default', 'intf-name': 'Vlan104', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 74, 'prefix': '172.16.104.2', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default', 'intf-name': 'Vlan105', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 75, 'prefix': '172.16.105.2', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default', 'intf-name': 'Eth1/3', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 7, 'prefix': '172.16.252.1', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default', 'intf-name': 'Eth1/4', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 8, 'prefix': '172.16.252.5', 'ip-disabled': 'FALSE'}]}}},
##        'id': 1}
##
##sw02 = {'jsonrpc': '2.0', 'result': {'body': {'TABLE_intf':{'ROW_intf':
##        [{'vrf-name-out': 'default', 'intf-name': 'Vlan101', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up','iod': 71, 'prefix': '172.16.101.3', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default','intf-name': 'Vlan102', 'proto-state': 'up','link-state': 'up', 'admin-state': 'up', 'iod': 72, 'prefix': '172.16.102.3', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default', 'intf-name': 'Vlan103', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 73, 'prefix': '172.16.103.3', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default', 'intf-name': 'Vlan104', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 74, 'prefix': '172.16.104.3', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default', 'intf-name': 'Vlan105', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 75, 'prefix': '172.16.105.3', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default', 'intf-name': 'Eth1/3', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 7, 'prefix': '172.16.252.2', 'ip-disabled': 'FALSE'},
##         {'vrf-name-out': 'default', 'intf-name': 'Eth1/4', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 8, 'prefix': '172.16.252.6', 'ip-disabled': 'FALSE'}]}}},
##        'id': 1}



sw01 = {'jsonrpc': '2.0', 'result': {'body': {'TABLE_intf':{'ROW_intf':
        [{'vrf-name-out': 'default', 'intf-name': 'Vlan101', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up','iod': 71, 'prefix': '172.16.101.2', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default','intf-name': 'Vlan102', 'proto-state': 'up','link-state': 'up', 'admin-state': 'up', 'iod': 72, 'prefix': '172.16.102.2', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default', 'intf-name': 'Vlan103', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 73, 'prefix': '172.16.103.2', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default', 'intf-name': 'Vlan104', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 74, 'prefix': '172.16.104.2', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default', 'intf-name': 'Vlan105', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 75, 'prefix': '172.16.105.2', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default', 'intf-name': 'Eth1/3', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 7, 'prefix': '172.16.252.1', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default', 'intf-name': 'Eth1/4', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 8, 'prefix': '172.16.252.5', 'ip-disabled': 'FALSE'}]}}},
        'id': 1}

sw02 = {'jsonrpc': '2.0', 'result': {'body': {'TABLE_intf':{'ROW_intf':
        [{'vrf-name-out': 'default', 'intf-name': 'Vlan101', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up','iod': 71, 'prefix': '172.16.101.3', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default','intf-name': 'Vlan102', 'proto-state': 'up','link-state': 'up', 'admin-state': 'up', 'iod': 72, 'prefix': '172.16.102.3', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default', 'intf-name': 'Vlan103', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 73, 'prefix': '172.16.103.3', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default', 'intf-name': 'Vlan104', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 74, 'prefix': '172.16.104.3', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default', 'intf-name': 'Vlan105', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 75, 'prefix': '172.16.105.3', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default', 'intf-name': 'Eth1/3', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 7, 'prefix': '172.16.252.2', 'ip-disabled': 'FALSE'},
         {'vrf-name-out': 'default', 'intf-name': 'Eth1/4', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 8, 'prefix': '172.16.252.6', 'ip-disabled': 'FALSE'}]}}},
        'id': 1}

#simulates getting a list of interfaces from the sandbox. Will accept 10.10.20.177 0r 10.10.20.178 as a url
#Returns a nested list of dictionaries identical to the one returned by a cli show ip interface brief

def shIntBri(url):
    if url == "10.10.20.177":
        ret_Int_List = sw01
    elif url == "10.10.20.178":
        ret_Int_List = sw02
    else:
        ret_Int_List = "None"
    return ret_Int_List

#simulates updating an interface on a NXOS switch in the sandbox
#accepts an url, interfaceName and ip address, all strings and returns nothing. It will update the sw01 or sw02 nested dictionary

def changeAddress(url,intName,ip):
    
    if url == "10.10.20.177":
        int_index = 0

#Change sw01 
        
        for interface in sw01["result"]["body"]["TABLE_intf"]["ROW_intf"]:
            if intName.capitalize() == interface["intf-name"]:
                sw01["result"]["body"]["TABLE_intf"]["ROW_intf"][int_index]["prefix"] = ip
            int_index +=1    
                
       
#Change sw02           
      
    elif url == "10.10.20.178":
        int_index = 0
        
        for interface in sw02["result"]["body"]["TABLE_intf"]["ROW_intf"]:
            if intName.capitalize() == interface["intf-name"]:
                sw02["result"]["body"]["TABLE_intf"]["ROW_intf"][int_index]["prefix"] = ip
            int_index +=1  
        
    else:
       print(url = " unreachable.")

###########################################################################################################################################


# function to format and print columns of information with headers
def printInterfaces(interfaces):

    print("Name" + " "*5 + "Proto" + " "*5 + "Link" + " "*5 + "Address")
    print("----" + " "*5 + "-----" + " "*5 + "----" + " "*5 + "-------")

    for dict in interfaces['result']['body']['TABLE_intf']["ROW_intf"]:
        print(f"{dict['intf-name']:8} {dict['proto-state']:10} {dict['link-state']:8} {dict['prefix']}")


# code to us if CML is live; takes given IP address of a device and updates the interfaces with new IP addresses
# def changeAddress(mgmt_IP, changeInt, newIP):

#     switchuser='cisco'
#     switchpassword='cisco'

#     url='https://' + mgmt_IP + '/ins'
#     myheaders={'content-type':'application/json-rpc'}
#     payload=[
#     {
#         "jsonrpc": "2.0",
#         "method": "cli",
#         "params": {
#         "cmd": "conf t",
#         "version": 1
#         },
#         "id": 1
#     },
#     {
#         "jsonrpc": "2.0",
#         "method": "cli",
#         "params": {
#         "cmd": "interface " + changeInt,
#         "version": 1
#         },
#         "id": 2
#     },
#     {
#         "jsonrpc": "2.0",
#         "method": "cli",
#         "params": {
#         "cmd": "ip add " + newIP + " 255.255.255.0",
#         "version": 1
#         },
#         "id": 3
#     }
#     ]

#     response = requests.post(url,data=json.dumps(payload), verify=False, headers=myheaders,auth=(switchuser,switchpassword)).json()
#     return response


#main  ************************************************************************************************************************************
    
# interfaces = get_Int("10.10.20.178")
# print(interfaces)
# update_Interface("10.10.20.178","vlan101","1.1.1.1")

# interfaces = get_Int("10.10.20.178")
# print(interfaces)

# dictionary listing of switches with management IPs
devices = {"SW1" : "10.10.20.177",
           "SW2" : "10.10.20.178"}

# loop through switches and get management IPs
for device in devices:
    mgmt_IP = (devices[device])

    # returns and prints interfaces from respective functions
    interfaces = shIntBri(mgmt_IP)
    printInterfaces(interfaces)
    print()

    # hardcode IP offset; loop through Vlan interfaces and add 5 to mgmt IP
    offsetIP = 5
    for device in interfaces['result']['body']['TABLE_intf']["ROW_intf"]:
            if "Vlan" in device['intf-name']:
                newInt = device['intf-name']                                 
                splitIP = device['prefix'].split(".")            
                newOctetValue = int(splitIP[3]) + offsetIP            
                splitIP[3] = str(newOctetValue)                       
                newIP = ".".join(splitIP)                
                # send updated IP addresses for specified interfaces to both switches
                changeAddress(mgmt_IP, newInt, newIP)

    # repeat above printout with updated IPs
    interfaces = shIntBri(mgmt_IP)
    printInterfaces(interfaces)

