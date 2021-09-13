"""
"""
import sys
import os
import json
import requests

from flask import Flask, request

# Ignore warnning from certificates
requests.packages.urllib3.disable_warnings()

app = Flask(__name__)

@app.route("/", methods=["POST"])
def getHook():
    """
        Simply listen for POST request from a webhook.
        Responsinble for processing and acting upon a reaquest by calling appropriate functions.
    """
    # Read URL request that comes in as a JSON file.

    print("Here")
    # request_data = request.get_json()
    # interface = request_data["interface"]

    # print(request_data)

    # print(json.dumps(interface, indent=4, sort_keys=True))

    # validateRestconf()
    # For Inteface ID you need to do this weird % sings, TODO: try find a way to make this simpler ....
    setInterfaceStatus("GigabitEthernet", "1%2F0%2F6", "shut")

    print("Change Interface Status")

    return "POST - Interface Status Change OK"


@app.route("/", methods=["GET"])
def usingGetMethod():
    """
        Only checks if RESTCONF is working on the device.
        TODO: Make it more useful for getting info from DNAC ...
    """
    # Read URL request that comes in as a JSON file.
    request_info = request.get_json()
    ppJSON(request_info)

    validateRestconf()

    return "Using GET Method"


@app.after_request
def add_header(response):
    '''
    Caching control
    '''
    response.cache_control.max_age = 300
    return response


def makeApiCall(method, resource, payload):
    """
        General funtion that executes the RESTCONF call based on the method, resource uri and payload.
    """

    url = "https://10.0.0.20:443/restconf/{r}".format(r=resource)
    # print("\n ... Debug: {} ---\n".format(url))

    # Specify headers for the RESTCONF
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # Simply does the API call
    response = requests.request(method, url, auth=("netadmin", "C1sco12345"), data=payload, headers=headers, verify=False)

    try:
        return (response.json())
    except:
        print(response)
        return ""


def ppJSON(parsed):
    """ Pretty Print JSON so it's visible better """
    print(json.dumps(parsed, indent=4, sort_keys=True))


def setInterfaceStatus(name, id, status):
    """
        Sets the interface status to shut or no shut.

        TODO: Adjust so it is generic and can take any interface name and number.
    """

    print("Changing interface status...")

    if status == "shut":
        data = {
            "Cisco-IOS-XE-native:GigabitEthernet": {
                "name": "1/0/6",
                "shutdown": [""]
            }
        }
    elif status == "no shut":
        data = {
            "Cisco-IOS-XE-native:{n}".format(n=name): {
                "name": id
            }
        }
    else:
        print("Use 'shut' or 'no shut' as the status")
        return

    payload = json.dumps(data)

    # resource = "data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1%2F0%2F5"
    # response = makeApiCall("GET", resource, payload="")
    # print(ppJSON(response))

    resource = "data/Cisco-IOS-XE-native:native/interface/{n}={i}".format(n=name, i=id)
    # For Cisco native, we need to use PUT, as "shutdown" is only displayed if port is admin down
    response = makeApiCall("PUT", resource, payload)
    print(ppJSON(response))


def validateRestconf():
    """ Validate that we can reach RESTCONF and display available resources """

    response = makeApiCall("GET", resource="", payload="")
    print(ppJSON(response))

    # Display available yang models for this device
    resource = "data/netconf-state/capabilities"
    response = makeApiCall("GET", resource, payload="")
    print(ppJSON(response))


# create a main() method2
def main():
    app.run(host="127.0.0.1", port= (os.environ.get("PORT", 8008)), debug=False)
    

if __name__ == '__main__':
    sys.exit(main())
