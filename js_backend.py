"""
"""
import sys

from flask import Flask, request
# from requests_toolbelt.multipart.encoder import MultipartEncoder

app = Flask(__name__)


@app.route("/", methods=["POST"])
def getHook():
    '''
    Simply listen for POST request from a webhook.
    Responsinble for processing and acting upon a reaquest by calling appropriate functions.
    '''
    # Read URL request that comes in as a JSON file.
    # It will contain information about room ID and type of hook it is (i.e. message or action)
    # Room ID will allow you to query the excact message since webhook does not include message just the notification.
    hook_info = request.json

    print(hook_info)

    # print(json.dumps(hook_info, indent=4, sort_keys=True))

    return "Using POST Method"


@app.route("/", methods=["GET"])
def usingGetMethod():
    '''
    '''
    # Read URL request that comes in as a JSON file.
    # It will contain information about room ID and type of hook it is (i.e. message or action)
    # Room ID will allow you to query the excact message since webhook does not include message just the notification.
    hook_info = request.json

    print(hook_info)

    # print(json.dumps(hook_info, indent=4, sort_keys=True))

    return "Using GET Method"


@app.after_request
def add_header(response):
    '''
    Caching control
    '''
    response.cache_control.max_age = 300
    return response


# create a main() method2
def main():
    # Hosted on localhost port 5004 - Remember to run "ngrok http 5004"
    app.run(host="0.0.0.0", port=8008, debug=False)
    

if __name__ == '__main__':
    sys.exit(main())
