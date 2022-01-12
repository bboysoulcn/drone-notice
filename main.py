import time
import requests
import hmac
import hashlib
import base64
import urllib.parse
import json
import sys
import os







def send_msg(msg, title, ding_secret, dingding_base_url):
    ding_secret = ding_secret
    dingding_base_url = dingding_base_url
    timestamp = str(round(time.time() * 1000))
    secret = ding_secret
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc,
                         digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    body = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": msg
        },
        "at": {
            "isAtAll": "true"
        }
    }
    dingding_url = dingding_base_url + "&timestamp=" + timestamp + "&sign=" + sign
    requests.post(dingding_url, json.dumps(body), headers=headers)


if __name__ == "__main__":
    dingding_base_url = os.getenv("PLUGIN_DDBASEURL")
    ding_secret = os.getenv("PLUGIN_DDSECRET")
    if os.getenv("DRONE_BUILD_STATUS") =="success":
        try:
            send_msg("build is success", "drone build", ding_secret, dingding_base_url)
        except Exception as e:
            print(e)
    else:
        try:
            send_msg("build is failed", "drone build", ding_secret, dingding_base_url)
        except Exception as e:
            print(e)
