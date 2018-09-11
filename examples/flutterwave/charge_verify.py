import json
import requests
from encrypt import getKey, encryptData
import ast
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

post_url = "https://ravesandboxapi.flutterwave.com/flwv3-pug/getpaidx/api/charge"


def charge_card(url, data):
    payload = {}
    public_key = os.environ['FLW_PUB_KEY']
    encrypt_key = getKey()
    final = encryptData(encrypt_key, data)
    payload["PBFPubKey"] = public_key
    payload["client"] = final
    payload["alg"] = "3DES-24"
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=str(json.dumps(payload)), headers=headers)
    response = str(r.text)
    return response


def verify_card(event, context):
    print event
    event1 = event['body']
    event_data = ast.literal_eval(str(event1))
    card_data = json.dumps(event_data)
    returned = charge_card(post_url, card_data)
    headers = {'content-type': 'application/json'}
    payload = {}
    public_key = os.environ['FLW_PUB_KEY']
    otp = "12345"
    data = json.loads(returned)
    flw_ref = data["data"]["flwRef"]
    payload["PBFPubKey"] = public_key
    payload["transaction_reference"] = flw_ref
    payload["otp"] = otp
    url = "https://ravesandboxapi.flutterwave.com/flwv3-pug/getpaidx/api/validatecharge"
    r = requests.post(url, data=str(json.dumps(payload)), headers=headers)
    print r.text
    response = {
        "statusCode": r.status_code,
        "body": json.dumps(r.text)
    }
    return response


