"""
"""
import sys
from dna_api_helper import makeApiCall, ppJSON, TOKEN

DEFAULT_HEADER = {
    'x-auth-token': TOKEN,
    'content-type': "application/json",
    'accept': "application/json"
}


def getSiteHealth():
    '''
        Get Health of the Site. Used just to test the connectivity and that APIs work.
    '''

    resource = "dna/intent/api/v1/site-health"

    response = makeApiCall('GET', resource, headers=DEFAULT_HEADER, payload="")
    print(ppJSON(response))


def getDeviceInfo(deviceId=""):
    '''
        Returns device info for a given device ID.
        If no id is provided then it returns a lits of all devices in the network.

        TODO: Add these features in this function:
            - https://developer.cisco.com/docs/dna-center/#!cisco-dna-2-2-2-api-api-devices-get-device-detail
            - 
    '''
    resource = "dna/intent/api/v1/network-device/{d}".format(d=deviceId)

    response = makeApiCall('GET', resource, headers=DEFAULT_HEADER, payload="")
    print(ppJSON(response))


def getDeviceBriefInfo(deviceId):
    '''
        Returns device info for a given device ID.
        If no id is provided then it returns a lits of all devices in the network.
    '''
    resource = "dna/intent/api/v1/network-device{d}/brief".format(d=deviceId)

    response = makeApiCall('GET', resource, headers=DEFAULT_HEADER, payload="")
    print(ppJSON(response))


def getDeviceConfig(deviceId):
    '''
        Returns device config  for a given device ID.
    '''
    resource = "dna/intent/api/v1/network-device{d}/config".format(d=deviceId)

    response = makeApiCall('GET', resource, headers=DEFAULT_HEADER, payload="")
    print(ppJSON(response))





# create a main() method2
def main():
    """ 
        
    """
    # getSiteHealth()
    deviceId = 'a62c9f20-424c-4811-87ce-3a04178ba59f'
    getDeviceInfo(deviceId)
    # getDeviceConfig(deviceId)
    
    

if __name__ == '__main__':
    sys.exit(main())
