import logging
import requests
import json
import base64
from dotenv import load_dotenv
import os
import jwt
from datetime import datetime
import sqlite3


# auth data for getting server to server OAuth Token requires appropriate scopes
load_dotenv()
CLIENT_ID = os.environ.get('CLIENTID')
CLIENT_SECRET = os.environ.get('CLIENTSECRET')
ACCOUNTID = os.environ.get('ACCOUNTID')

# Connect to the DB


def connectDB():
    con = sqlite3.connect("token.db")
    c = con.cursor()
    c.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='tokens' ''')
    if c.fetchone()[0] == 1:
        logging.info("Table exists")
    else:
        logging.info("Table does NOT exist Creating Table")
        c.execute("CREATE TABLE tokens(uuid INTEGER UNIQUE, token TEXT)")

# Function to fetch a new token from Zoom REST API


def get_token():
    con = sqlite3.connect("token.db")
    c = con.cursor()
    # generate basic auth
    logging.info("Fetching NEW Token")
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
    # Write token to DB
    try:
        c.execute(
            "INSERT OR REPLACE INTO tokens(uuid,token) VALUES (?,?)", (1, token,))
        con.commit()
    except sqlite3.Error:
        logging.warning(sqlite3.Error)
    #print("Token from Zoom API: %s" % token)
    return token

# Function to check if a token is expired


def isExpired(t):
    logging.info("Validating Token")
    decoded = jwt.decode(t, CLIENT_SECRET,
                         options={"verify_signature": False})
    expiry = decoded["exp"]
    if expiry < datetime.now().timestamp():
        logging.info("Token Expired = True")
        return True
    else:
        logging.info("Token Expired = False ")
        return False

# Function to manage token usage


def token():
    connectDB()
    con = sqlite3.connect("token.db")
    c = con.cursor()
    try:
        # Get TOken from DB
        data = c.execute("SELECT token FROM tokens Where uuid = 1").fetchone()
        #print("Token from DB: %s" % data[0])
        token = data[0]
    except Exception as ex:
        logging.info("Token not exist in DB")
        token = get_token()
    # check if token is expired
    if isExpired(token) == True:
        # if token expired get new token
        return get_token()
    else:
        # if token not expired use token
        return token
