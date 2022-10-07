# IMPORT
from lib.log import *
from lib.req import *
from lib.printJSON import *

# SETUP LOGGING
create_log()

# Code Goes Here


# Example request
def listUsers():
    # set the URL for the api request
    url = "/users"
    # pass any data that needs to be in the body of the request
    data = {}
    # specify RESTful action get,patch,put,post,delete
    action = "get"
    # send the request
    response = send_request(action, url, data)
    # prettyPrint response
    printJSON(response)


listUsers()
