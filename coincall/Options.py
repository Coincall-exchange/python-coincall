from .client import Client

class OptionsAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', diff='3000', use_server_time=False, domain = 'https://api.coincall.com',debug = True):
        Client.__init__(self, api_key, api_secret_key, diff, use_server_time, domain, debug)

    def get_instruments(self, base):
        """
        |
        | **Get Instruments**
        | *Get all options instruments.*

        :API endpoint: ``GET /open/option/getInstruments/{}``
        :API doc: https://docs.coincall.com/#options-endpoint-get-option-instruments-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/option/getInstruments/{}".format(base)
        return self._request("GET", url_path, params)
    
    def get_options_by_endtime(self, index, endTime):
        """
        |
        | **Get Option Chain**
        | *Get option dnderlying information by index.*

        :API endpoint: ``GET /open/option/get/v1/{index}?{endTime}``
        :API doc: https://docs.coincall.com/#options-endpoint-get-option-chain-signed
        :Parameter: query string
        |
        """

        params = {
            "endTime": endTime
        }
        url_path = "/open/option/get/v1/{}".format(index)
        return self._request("GET", url_path, params)
    
    def get_option_by_name(self, symbol):
        """
        |
        | **Get Option Details**
        | *Get option details by option symbol name.*

        :API endpoint: ``GET /open/option/detail/v1/{}``
        :API doc: https://docs.coincall.com/#options-endpoint-get-option-details-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/option/detail/v1/{}".format(symbol)
        return self._request("GET", url_path, params)
    
    def get_depth(self, symbol):
        """
        |
        | **Get OrderBook**
        | *Get option order book for 100 depth.*

        :API endpoint: ``GET /open/option/order/orderbook/v1/{}``
        :API doc: https://docs.coincall.com/#options-endpoint-get-option-details-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/option/order/orderbook/v1/{}".format(symbol)
        return self._request("GET", url_path, params)
    
    def get_lasttrade(self, symbol):
        """
        |
        | **Get Last Trade**
        | *Get option last trade.*

        :API endpoint: ``GET /open/option/trade/lasttrade/v1/{}``
        :API doc: https://docs.coincall.com/#options-endpoint-get-last-trade-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/option/trade/lasttrade/v1/{}".format(symbol)
        return self._request("GET", url_path, params)
    
    def get_positions(self):
        """
        |
        | **Get Positions**
        | *Get all option positions.*

        :API endpoint: ``GET /open/option/position/get/v1``
        :API doc: https://docs.coincall.com/#options-endpoint-get-positions-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/option/position/get/v1"
        return self._request("GET", url_path, params)
    
    def place_order(self, symbol, qty, tradeSide, tradeType, clientOrderId=None, price=None):
        """
        |
        | **Place Order**
        | *Place an option order.*

        :API endpoint: ``POST /open/option/order/create/v1``
        :API doc: https://docs.coincall.com/#options-endpoint-place-order-signed
        :Parameter: request body
        |
        """

        params = {
            "symbol": symbol,
            "qty": qty,
            "tradeSide": tradeSide,
            "tradeType": tradeType
        }
        if clientOrderId:
            params['clientOrderId'] = clientOrderId
        if price:
            params['price'] = price
        url_path = "/open/option/order/create/v1"
        return self._request("POST", url_path, params)
    
    def cancel_order(self, orderId=None, clientOrderId=None):
        """
        |
        | **Cancel Order**
        | *Cancel an option order.*

        :API endpoint: ``POST /open/option/order/cancel/v1``
        :API doc: https://docs.coincall.com/#options-endpoint-cancel-order-signed
        :Parameter: request body
        |
        """

        params = {}
        if orderId:
            params['orderId'] = orderId
        if clientOrderId:
            params['clientOrderId'] = clientOrderId
        url_path = "/open/option/order/cancel/v1"
        return self._request("POST", url_path, params)
    
    def cancel_orders(self, symbol, version='v1'):
        """
        |
        | **Cancel Orders**
        | *Cancel option orders by symbol.*

        :API endpoint: ``GET /open/option/order/cancelOpenOrders/{version}/{symbol}``
        :API doc: https://docs.coincall.com/#options-endpoint-cancel-orders-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/option/order/cancelOpenOrders/{}/{}".format(version,symbol)
        return self._request("GET", url_path, params)
    
    def get_open_orders(self, symbol=None, page=1, pageSize=20):
        """
        |
        | **Get Open Orders**
        | *Get option open orders.*

        :API endpoint: ``GET /open/option/order/pending/v1``
        :API doc: https://docs.coincall.com/#options-endpoint-get-open-orders-signed
        :Parameter: query string
        |
        """

        params = {
            "page": page,
            "pageSize": pageSize
        }
        if symbol:
            params["symbol"] = symbol
        url_path = "/open/option/order/pending/v1"
        return self._request("GET", url_path, params)
    
    def get_order_by_id(self, orderId=None, clientOrderId=None):
        """
        |
        | **Get Order Info**
        | *Get an order information by orderId or clientOrderId.*

        :API endpoint: ``GET /open/option/order/singleQuery/v1``
        :API doc: https://docs.coincall.com/#options-endpoint-get-order-info-signed
        :Parameter: query string
        |
        """

        params = {}
        if orderId:
            params['orderId'] = orderId
        if clientOrderId:
            params['clientOrderId'] = clientOrderId
        url_path = "/open/option/order/singleQuery/v1"
        return self._request("GET", url_path, params)
    
    def get_order_history(self, fromId=None, startTime=None, endTime=None, pageSize=10):
        """
        |
        | **Get Order Details**
        | *Get option order history.*

        :API endpoint: ``GET /open/option/order/history/v1/{}``
        :API doc: https://docs.coincall.com/#options-endpoint-get-order-details-signed
        :Parameter: query string
        |
        """

        params = {
            "pageSize": pageSize
        }
        if fromId:
            params['fromId'] = fromId
        if startTime:
            params['startTime'] = startTime
        if endTime:
            params['endTime'] = endTime
        url_path = "/open/option/order/history/v1"
        return self._request("GET", url_path, params)

    def get_trade_history(self, fromId=None, startTime=None, endTime=None, pageSize=None):
        """
        |
        | **Get Transaction details**
        | *Get option transaction history.*

        :API endpoint: ``GET /open/option/trade/history/v1``
        :API doc: https://docs.coincall.com/#options-endpoint-get-transaction-details-signed
        :Parameter: query string
        |
        """

        params = {}
        if fromId:
            params['fromId'] = fromId
        if startTime:
            params['startTime'] = startTime
        if endTime:
            params['endTime'] = endTime
        if pageSize:
            params['pageSize'] = pageSize
        url_path = "/open/option/trade/history/v1"
        return self._request("GET", url_path, params)