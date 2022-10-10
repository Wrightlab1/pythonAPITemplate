import logging
import requests
import json
import base64
from dotenv import load_dotenv
import os


# auth data for getting server to server OAuth Token requires appropriate scopes
load_dotenv()
CLIENT_ID = os.environ.get('CLIENTID')
CLIENT_SECRET = os.environ.get('CLIENTSECRET')
ACCOUNTID = os.environ.get('ACCOUNTID')


def token():
    # generate basic auth
    logging.info("Fetching Token")
    message = "%s:%s" % (CLIENT_ID, CLIENT_SECRET)
    auth = base64.b64encode(message.encode()).decode()
    headers = {'authorization': 'Basic %s' % auth,
               'content-type': 'application/json'}
    FINAL_URL = "https://zoom.us/oauth/token?grant_type=account_credentials&account_id=%s" % ACCOUNTID
    logging.debug("'{0}', '{1}'".format(FINAL_URL, headers))
    r = requests.post(FINAL_URL, headers=headers)
    if str(r.status_code).startswith('2'):
        logging.info("'Status: {0}', 'RESPONSE: {1}'".format(
            r.status_code, r.content))
    else:
        logging.warning("'Status: {0}', 'RESPONSE: {1}'".format(
            r.status_code, r.content))
    data = json.loads(r.content)
    token = data['access_token']
    return token
