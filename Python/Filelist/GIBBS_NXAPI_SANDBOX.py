# David Gibbs
# This script will retrieve json output of several Cisco CLI "show" commands as well as format and output
# specific values.
#
# script compiled from lesson illustrations and previous assignments

# import modules
import requests
import json
import urllib3
# disable warning
urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

"""
Modify these please
"""
#For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
#For basic authentication using username & pwd, set 'client_cert_auth' to False.
client_cert_auth=False
switchuser='cisco'
switchpassword='cisco'
client_cert='PATH_TO_CLIENT_CERT_FILE'
client_private_key='PATH_TO_CLIENT_PRIVATE_KEY_FILE'
ca_cert='PATH_TO_CA_CERT_THAT_SIGNED_NXAPI_SERVER_CERT'

url='https://10.10.20.177/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "sh version",
      "version": 1
    },
    "id": 1
  }
]
#connect and retrieve json from payload; added cancellation of verification
if client_cert_auth is False:
    response = requests.post(url,data=json.dumps(payload), verify=False, headers=myheaders,auth=(switchuser,switchpassword)).json()
else:
    url='https://10.10.20.177/ins'
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert,client_private_key),verify=ca_cert).json()

# assign nested information to a variable; print formated output from json file.
switchInfo = response["result"]["body"]
print(f"Hostname = " + switchInfo["host_name"], "\t" + "Memory = " + str(switchInfo["memory"]) + switchInfo["mem_type"])


