from twisted.internet import reactor

from . import ws_utils
from .ws_connect_manager import WsConnectManager


class WsPrivate(WsConnectManager):
    def __init__(self, apiKey: str, passphrase: str, url: str, useServerTime: False):
        if (
            ~ws_utils.isNotBlankStr(apiKey)
            or ~ws_utils.isNotBlankStr(passphrase)
            or ~ws_utils.isNotBlankStr(url)
        ):
            return
        super().__init__(url, isPrivate=True)
        self.apiKey = apiKey
        self.passphrase = passphrase
        self.useServerTime = useServerTime

    def subscribe(self, params: list, callback):
        self.subscribeSocket(params, callback)

    def unsubscribe(self, params: list, callback):
        self.unsubscribeSocket(params, callback)

    def stop(self):
        try:
            self.close()
        finally:
            reactor.stop()
