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
    # if query paramters are needed add them here
    url = "/users"
    # pass any data that needs to be in the body of the request
    # should be a dict will be converted to json for you
    data = {}
    # specify RESTful action get,patch,put,post,delete
    action = "get"
    # send the request the send_reequest() function is imported from ./lib/req.py
    # It takes 3 arguments action(the RESTFUL API verb), the url(everything after 'https://api.zoom.us/v2/'), and data(a dict that acts as the body of the request)
    response = send_request(action, url, data)
    # prettyPrint response
    printJSON(response)


listUsers()
