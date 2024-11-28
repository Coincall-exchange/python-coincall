from .client import Client

class RfqAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', diff='3000', use_server_time=False, domain = 'https://api.coincall.com',debug = True):
        Client.__init__(self, api_key, api_secret_key, diff, use_server_time, domain, debug)

    def get_board_list(self, currentPage=1, pageSize=10):
        """
        |
        | **Get block trade board list**
        | *Get block trade board list.*

        :API endpoint: ``GET /open/option/blockTrade/seek/list/v1``
        :API doc: https://docs.coincall.com/#rfq-board-list-signed
        :Parameter: request body
        |
        """

        params = {}
        if currentPage:
            params["currentPage"] = currentPage
        if pageSize:
            params["pageSize"] = pageSize
        url_path = "/open/option/blockTrade/seek/list/v1"
        return self._request("GET", url_path, params)
    
    def create_quote(self, requestId, price, symbol, type):
        """
        |
        | **Create block trade**
        | *Create block trade.*

        :API endpoint: ``GET /open/option/blockTrade/quote/create/v1``
        :API doc: https://docs.coincall.com/#rfq-create-quote-signed
        :Parameter: request body
        |
        """

        params = {
            'orderOpenApiDetailReqs': '[{"price":'+price+',"symbol":'+ symbol+',"type":'+ type+'}]',
            'requestId': requestId
        }

        url_path = "/open/option/blockTrade/quote/create/v1"
        return self._request("POST", url_path, params)
    
    def cancel_quote(self, quoteId):
        """
        |
        | **Cancel block trade**
        | *Cancel block trade.*

        :API endpoint: ``GET open/option/blockTrade/quote/cancel/v1/{quoteId}``
        :API doc: https://docs.coincall.com/#rfq-cancel-quote-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/option/blockTrade/quote/cancel/v1/{}".format(quoteId)
        return self._request("GET", url_path, params)