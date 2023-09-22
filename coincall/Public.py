from .client import Client

class PublicAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', diff='3000', use_server_time=False, domain = 'https://api.coincall.com',debug = True):
        Client.__init__(self, api_key, api_secret_key, diff, use_server_time, domain, debug)

    def get_server_time(self):
        """
        |
        | **Check Server Time**
        | *Test connectivity to the Rest API and get the current server time.*

        :API endpoint: ``GET /time``
        :API doc: https://docs.coincall.com/#public-endpoints-check-server-time
        |
        """

        params = {}
        url_path = "/time"
        return self._request("GET", url_path, params)

    def get_config(self):
        """
        |
        | **Get Public Configurations**
        | *Trading-related configuration.*

        :API endpoint: ``GET /open/public/config/v1``
        :API doc: https://docs.coincall.com/#public-endpoints-get-public-configurations
        |
        """

        params = {}
        url_path = "/open/public/config/v1"
        return self._request("GET", url_path, params)

    def get_realtime_funding_rate(self, symbol=None):
        """
        |
        | **Get Funding Rate**
        | *Real-time funding rate*

        :API endpoint: ``GET /open/public/fundingRate/v1``
        :API doc: https://docs.coincall.com/#public-endpoints-get-funding-rate
        |
        """
        params = {}
        url_path = "open/public/fundingRate/v1"
        if symbol:
            params["symbol"] = symbol
        return self._request("GET", url_path, params)