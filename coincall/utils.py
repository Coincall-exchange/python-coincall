import hashlib
import hmac
import base64
import time


def sign(message, secretKey, debug=True):
    if debug == True:
        print('pre_hash: ', message)
    signature = hmac.new(secretKey.encode('utf-8'),
                         message.encode('utf-8'), hashlib.sha256).hexdigest()
    return signature.upper()


def pre_hash(timestamp, method, request_path, apiKey, diff, body={}, debug=True):
    if debug == True:
        print('body: ', body)
    hash = ''
    sorted_params_list = []
    for key in sorted(body.keys()):
        sorted_params_list.append(key+'='+str(body[key]))
    hash = str.upper(method) + request_path + (("?" + "&".join(sorted_params_list) + "&")
                                               if sorted_params_list else "?") + "uuid=" + apiKey + "&ts=" + str(timestamp) + "&x-req-ts-diff=" + str(diff)
    return hash


def get_header(api_key, sign, timestamp, diff, debug=True):
    header = dict()
    header['Content-Type'] = 'application/json'
    header['X-CC-APIKEY'] = api_key
    header['sign'] = sign
    header['ts'] = str(timestamp)
    header['X-REQ-TS-DIFF'] = diff
    if debug == True:
        print('header: ', header)
    return header


def get_header_no_sign(debug=True):
    header = dict()
    header['Content-Type'] = 'application/json'
    if debug == True:
        print('header: ', header)
    return header


def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        if (value != ''):
            url = url + str(key) + '=' + str(value) + '&'
    url = url[0:-1]
    # print('url:',url)
    return url


def get_timestamp():
    return int(time.time() * 1000)


def signature(timestamp, method, request_path, body, secret_key):
    if str(body) == '{}' or str(body) == 'None':
        body = ''
    message = str(timestamp) + str.upper(method) + request_path + str(body)

    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(
        message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()

    return base64.b64encode(d)
