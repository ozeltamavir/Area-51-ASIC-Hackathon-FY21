"""
"""

# import the requests library
import requests
from requests.auth import HTTPBasicAuth
import sys
import json
import base64

import env_lab  # noqa

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# TO CHANGE ENVIRONMENT just CHANGE THE NAME HERE !!! ------------
HOST_ENV = env_lab.DNAC_DCLOUD

# use the IP address or hostname of your Cat9300
HOST = HOST_ENV['host']
PORT = HOST_ENV['port']

# use your user credentials to access the Cat9300
USER = HOST_ENV['username']
PASS = HOST_ENV['password']
TOKEN = HOST_ENV['token']

GET = "GET"
POST = "POST"
PATCH = "PATCH"
DELETE = "DELETE"
PUT = "PUT"

DEFAULT_HEADER = {
    'x-auth-token': TOKEN,
    'content-type': "application/json",
    'accept': "application/json"
}

# User Input
DNAC_PUBLIC = {
    "host": "sandboxdnac2.cisco.com",
    "port": 443,
    "username": "devnetuser",
    "password": "Cisco123!",
    "token": ""
}

DNAC_DCLOUD = {
    "host": "198.18.133.101",
    "port": 443,
    "username": "admin",
    "password": "C1sco12345",
    "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1ZmJmMGZiYWEwZTFjZTAwY2I5OTU3NGQiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVmYmYwZmI5YTBlMWNlMDBjYjk5NTc0YyJdLCJ0ZW5hbnRJZCI6IjVmYmYwZmI4YTBlMWNlMDBjYjk5NTc0YSIsImV4cCI6MTYyOTYxOTk1MywiaWF0IjoxNjI5NjE2MzUzLCJqdGkiOiIzZTgxOTIwNy0xMzFjLTRkNjMtYjkzMy1lYTgxNjViNTUyNzUiLCJ1c2VybmFtZSI6ImFkbWluIn0.X97_rApHt6jynhnc91bXkh6pKi_RzZ-lSb94OSj5v9SxYJUw1CsOdGuVAw2uLXYPD8NqPXHDSwbnAFTKvE58ycnahOu-8Vmktmuk3rXUYi5_cv3ubAyzQRNtbW2QQ6GZ-vCGvsD9ECoVNueiLuVQDAzJs9dI520p3VctNVslgJTqZzvq9_53bJN6L9PvwInaW-74SSA0I2RRKSUbWIKosPW4tmK_-4kekzvuFs-hwO7uwHy71mDfvVgCicjlP5MoEUFPzehWITeMHgz_I9v6HfNhh_a1-g2vdxtyRC55ZNHwOwPzXpY6UffM9Br1_5sWjvS4XKUGSNqeAy3zvfLN-w"
}

def base64Encode(message):
    """
        Encode the message as base64 and return.
    """
    message_bytes = message.encode("ascii")
    
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode("ascii")


def getToken():
    """
        String composed of ???Basic???, followed by a space, followed by the Base64 encoding of ???username:password???, NOT including the quotes. 
        For example ???Basic YWRtaW46TWFnbGV2MTIz???, where YWRtaW46TWFnbGV2MTIz is the Base 64 encoding.
    """

    # Auth is base64 encoding of username + password
    auth = base64Encode("{u}:{p}".format(u=USER, p=PASS))
    auth = "Basic {}".format(auth)
    # print(auth)
    
    headers = {
        "Content-Type" : "application/json",
        "Accept" : "application/json",
        "Authorization" : auth
    }

    # /dna/system/api/v1/auth/token
    url = "https://{h}:{p}/dna/system/api/v1/auth/token".format(h=HOST, p=PORT)
    response = requests.request("POST", url, headers=headers, verify=False)
    
    print(response)
    ppJSON(response.json())


def makeApiCall(method, resource, headers, payload):

    url = "https://{h}:{p}/{r}".format(h=HOST, p=PORT, r=resource)

    # print("\n ... Debug: {} ---\n".format(url))

    # RESTCONF media types for REST API headers
    # headers = {'x-auth-token': TOKEN}

    print(url)
    print(headers)

    # this statement performs a GET on the specified url
    response = requests.request(method, url, data=payload, headers=headers, verify=False)

    # print the json that is returned
    try:
        return (response.json())
    except:
        print(response)
        return ""


def ppJSON(parsed):
    """ Pretty Print JSON so it's visible better """
    print(json.dumps(parsed, indent=4, sort_keys=True))


# create a main() method2
def main():
    """ 
        Main returns token by default.
        Otherwise, it is only used as a helper function.
    """
    val = input("This function will generate new API Token. Are you sure you want to continue [y/n]: ")
    
    if val == 'y':
        print("HOST: {h}".format(h=HOST))
        print("---- TOKEN ----")
        getToken()
    else:
        print("exiting...")
    

if __name__ == '__main__':
    sys.exit(main())

