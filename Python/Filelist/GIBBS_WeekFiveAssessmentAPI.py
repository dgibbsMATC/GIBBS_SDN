# David Gibbs 9/26/23
# This script takes the dictionary output from a device on a Cisco Sandbox virtual network
# and formats and prints the specified output
# - Previous assignments and notes
# - https://www.w3schools.com/python/


# function to filter, format, and print output after the header info
def outputFunction(rowDict):
    for output in rowDict:
        print(output['intf-name'], output['proto-state'], output['link-state'], output['prefix'], sep='\t\t')



# main *********************************************************************

# take json output from assignment device and assigns it to a variable
switchOutput = {'jsonrpc': '2.0', 'result': {'body': {'TABLE_intf': {'ROW_intf': [{'vrf-name-out': 'default', 'intf-name': 'Vlan101', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 71, 'prefix': '172.16.101.2', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan102', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 72, 'prefix': '172.16.102.2', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan103', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 73, 'prefix': '172.16.103.2', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan104', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 74, 'prefix': '172.16.104.2', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan105', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 75, 'prefix': '172.16.105.2', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Eth1/3', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 7, 'prefix': '172.16.252.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Eth1/4', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 8, 'prefix': '172.16.252.5', 'ip-disabled': 'FALSE'}]}}}, 'id': 
1}

# variable assigned to ROW_intf nested list of dictionaries
rowDict = switchOutput['result']['body']['TABLE_intf']['ROW_intf']

# print and space column names as headers over a dash line
print('Name\t\t' + 'Protocol\t' + 'Link State\t' + 'Address')
print("-" * 60)
# funtion call to print output
outputFunction(rowDict)