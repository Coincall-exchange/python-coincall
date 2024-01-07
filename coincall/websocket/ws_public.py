from twisted.internet import reactor

from .ws_connect_manager import WsConnectManager


class WsPublic(WsConnectManager):
    def __init__(self, url):
        super().__init__(url, isPrivate=False)

    def subscribe(self, params: list, callback):
        self.subscribeSocket(params, callback)

    def unsubscribe(self, params: list, callback):
        self.unsubscribeSocket(params, callback)

    def stop(self):
        try:
            self.close()
        finally:
            reactor.stop()
