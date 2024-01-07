import base64
import hashlib
import hmac
import json
import time

import requests


def initLoginParams(useServerTime: bool, apiKey, passphrase):
    timestamp = getLocalTime()
    if useServerTime:
        timestamp = getServerTime()
    verb = "GET"
    uri = "/users/self/verify"
    message = verb + uri + "?uuid=" + apiKey + "&ts=" + str(timestamp)
    signature = hmac.new(
        passphrase.encode("utf-8"), message.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    sign = signature.upper()
    arg = {
        "apiKey": apiKey,
        "passphrase": passphrase,
        "timestamp": timestamp,
        "sign": sign,
    }
    payload = {"op": "login", "args": [arg]}
    return json.dumps(payload, ensure_ascii=False).encode("utf8")


def isNotBlankStr(param: str) -> bool:
    return param is not None and isinstance(param, str) and (~param.isspace())


def getParamKey(arg: dict) -> str:
    s = ""
    for k in arg:
        if k == "action":
            continue
        s = s + "@" + arg.get(k)
    return s


def initSubscribeSet(arg: dict) -> set:
    paramsSet = set()
    if arg is None:
        return paramsSet
    elif isinstance(arg, dict):
        paramsSet.add(getParamKey(arg))
        return paramsSet
    else:
        raise ValueError("arg must dict")


def checkSocketParams(args: list, channelArgs, channelParamMap):
    for arg in args:
        channel = arg["action"].strip()
        if ~isNotBlankStr(channel):
            raise ValueError("action must not none")
        argSet = channelParamMap.get(channel, set())
        argKey = getParamKey(arg)
        if argKey in argSet:
            continue
        else:
            validParams = initSubscribeSet(arg)
        if len(validParams) < 1:
            continue
        p = {}
        for k in arg:
            p[k.strip()] = arg.get(k).strip()
        channelParamMap[channel] = channelParamMap.get(channel, set()) | validParams
        if channel not in channelArgs:
            channelArgs[channel] = []
        channelArgs[channel].append(p)


def getServerTime():
    url = "https://api.coincall.com/time"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["data"]["serverTime"]
    else:
        return ""


def getLocalTime():
    return int(time.time())
