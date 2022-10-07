# PYTHON ZOOM REST API SCRIPT TEMPLATE

## Installation
Clone this project
```
the link goes here
```
Install dependencies
```
pip install -r requirements.txt
```

## Usage
This project should act as a template to create scripts to interact with the Zoom REST API
Authentication is Handled through a Zoom [Server to Server OAuth application](https://marketplace.zoom.us/docs/guides/build/server-to-server-oauth-app/)
Be Sure to Add the necessary scopes to your marketplace app

You will need to create a ```.env``` file  in the root of the project with the following
```
ACCOUNTID="yourAccountID"
CLIENTID="yourClientID"
CLIENTSECRET="yourClientSecret"
```
### Example GET Request
```
def listUsers():
    # set the URL for the api request
    #if query paramters are needed add them here
    url = "/users"
    # pass any data that needs to be in the body of the request
    #should be a dict will be converted to json for you
    data = {}
    # specify RESTful action get,patch,put,post,delete
    action = "get"
    # send the request
    response = send_request(action, url, data)
    # prettyPrint response
    printJSON(response)
```
## Logging
A logfile is generate for you in ``` ./logs/log.log```
This logfile will containg all of the information you need to debug your Zoom REST API requests