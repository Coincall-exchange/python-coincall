from .client import Client


class FuturesAPI(Client):
    def __init__(
        self,
        api_key="-1",
        api_secret_key="-1",
        diff="3000",
        use_server_time=False,
        domain="https://api.coincall.com",
        debug=True,
    ):
        Client.__init__(
            self, api_key, api_secret_key, diff, use_server_time, domain, debug
        )

    def get_funding_rate_history(self,symbol):
        """
        |
        | **Get Funding Rate History**
        | *Get Funding Rate History.*

        :API endpoint: ``GET /open/futures/market/symbol/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-funding-rate-details-signed
        |
        """

        params = {
            'symbol':symbol
        }
        url_path = "/open/settle/future/record/v1"
        return self._request("GET", url_path, params)

    def get_instruments(self):
        """
        |
        | **Get Symbol Information**
        | *Get futures symbol information.*

        :API endpoint: ``GET /open/futures/market/instruments/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-instruments
        |
        """

        params = {}
        url_path = "/open/futures/market/instruments/v1"
        return self._request("GET", url_path, params)
    
    def get_orderbook(self, symbol, depth=1):
        """
        |
        | **Get OrderBook**
        | *Get futures orderbook for 100 depth.*

        :API endpoint: ``GET /open/futures/order/orderbook/v1/{}``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-orderbook-signed
        :Parameter: request body
        |
        """

        params = {
            'symbol':symbol,
            'depth': depth
        }
        url_path = "/open/futures/market/orderbook"
        return self._request("GET", url_path, params)

    def get_symbols(self):
        """
        |
        | **Get Symbol Information**
        | *Get futures symbol information.*

        :API endpoint: ``GET /open/futures/market/symbol/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-symbol-information-signed
        |
        """

        params = {}
        url_path = "/open/futures/market/symbol/v1"
        return self._request("GET", url_path, params)

    def get_depth(self, symbol):
        """
        |
        | **Get OrderBook**
        | *Get futures orderbook for 100 depth.*

        :API endpoint: ``GET /open/futures/order/orderbook/v1/{}``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-symbol-information-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/futures/order/orderbook/v1/{}".format(symbol)
        return self._request("GET", url_path, params)

    def get_kline(self, symbol, period, start, end, limit=None):
        """
        |
        | **Get Kline**
        | *Query for historical klines (also known as candles/candlesticks).*

        :API endpoint: ``GET /open/futures/market/kline/history/v2/{symbol}``
        :API doc: https://docs.coincall.com/#futures-endpoint-kline-signed
        :Parameter: query string
        |
        """

        params = {"period": period, "start": start, "end": end}
        if limit:
            params["limit"] = limit
        url_path = "/open/futures/market/kline/history/v2/{}".format(symbol)
        return self._request("GET", url_path, params)

    def get_lasttrade(self, symbol):
        """
        |
        | **Get Last Trade**
        | *Get futures last trade.*

        :API endpoint: ``GET /open/futures/trade/lasttrade/v1/{}``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-last-trade-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/futures/trade/lasttrade/v1/{}".format(symbol)
        return self._request("GET", url_path, params)

    def get_leverage(self, symbol):
        """
        |
        | **Get leverage**
        | *Get current futrues leverage.*

        :API endpoint: ``GET /open/futures/leverage/current/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-leverage-signed
        :Parameter: request body
        |
        """

        params = {"symbol": symbol}
        url_path = "/open/futures/leverage/current/v1"
        return self._request("GET", url_path, params)

    def set_leverage(self, symbol, leverage):
        """
        |
        | **Set Leverage**
        | *Set futures leverage.*

        :API endpoint: ``POST /open/futures/leverage/set/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-leverage-signed
        :Parameter: request body
        |
        """

        params = {"symbol": symbol, "leverage": leverage}
        url_path = "/open/futures/leverage/set/v1"
        return self._request("POST", url_path, params)

    def get_positions(self):
        """
        |
        | **Get Positions**
        | *Get futures positions.*

        :API endpoint: ``GET /open/futures/position/get/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-positions-signed
        |
        """

        params = {}
        url_path = "/open/futures/position/get/v1"
        return self._request("GET", url_path, params)

    def place_order(
        self,
        symbol,
        qty,
        tradeSide,
        tradeType,
        clientOrderId=None,
        price=None,
        timeInForce=None,
    ):
        """
        |
        | **Place Order**
        | *Place a futures order.*

        :API endpoint: ``POST /open/futures/order/create/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-place-order-signed
        :Parameter: request body
        |
        """

        params = {
            "symbol": symbol,
            "qty": qty,
            "tradeSide": tradeSide,
            "tradeType": tradeType,
        }
        if clientOrderId:
            params["clientOrderId"] = clientOrderId
        if price:
            params["price"] = price
        if timeInForce:
            params["timeInForce"] = timeInForce
        url_path = "/open/futures/order/create/v1"
        return self._request("POST", url_path, params)

    def cancel_order(self, orderId=None, clientOrderId=None):
        """
        |
        | **Cancel Order**
        | *Cancel a futures order.*

        :API endpoint: ``POST /open/futures/order/cancel/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-cancel-order-signed
        :Parameter: request body
        |
        """

        params = {}
        if orderId:
            params["orderId"] = orderId
        if clientOrderId:
            params["clientOrderId"] = clientOrderId
        url_path = "/open/futures/order/cancel/v1"
        return self._request("POST", url_path, params)

    def cancel_orders(self, symbol, version="v1"):
        """
        |
        | **Cancel Orders**
        | *Cancel futures orders by symbol.*

        :API endpoint: ``GET /open/futures/order/cancelOpenOrders/{version}/{symbol}``
        :API doc: https://docs.coincall.com/#futures-endpoint-cancel-orders-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/futures/order/cancelOpenOrders/{}/{}".format(version, symbol)
        return self._request("GET", url_path, params)

    def get_open_orders(self, symbol=None, page=1, pageSize=20):
        """
        |
        | **Get Open Orders**
        | *Get futures open orders.*

        :API endpoint: ``GET /open/futures/order/pending/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-open-orders-signed
        :Parameter: request body
        |
        """

        params = {"page": page, "pageSize": pageSize}
        if symbol:
            params["symbol"] = symbol
        url_path = "/open/futures/order/pending/v1"
        return self._request("GET", url_path, params)

    def get_order_by_id(self, orderId=None, clientOrderId=None):
        """
        |
        | **Get Order Info**
        | *Get an order information by orderId or clientOrderId.*

        :API endpoint: ``GET /open/futures/order/singleQuery/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-order-info-signed
        :Parameter: request body
        |
        """

        params = {}
        if orderId:
            params["orderId"] = orderId
        if clientOrderId:
            params["clientOrderId"] = clientOrderId
        url_path = "/open/futures/order/singleQuery/v1"
        return self._request("GET", url_path, params)

    def get_order_history(self, fromId=None, startTime=None, endTime=None, pageSize=20):
        """
        |
        | **Get Order Details**
        | *Get futures order history.*

        :API endpoint: ``GET /open/futures/order/history/v1/{}``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-order-info-signed
        :Parameter: request body
        |
        """

        params = {"pageSize": pageSize}
        if fromId:
            params["fromId"] = fromId
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
        url_path = "/open/futures/order/history/v1"
        return self._request("GET", url_path, params)

    def get_trade_history(
        self, fromId=None, startTime=None, endTime=None, pageSize=None
    ):
        """
        |
        | **Get Transaction details**
        | *Get futrues transaction history.*

        :API endpoint: ``GET /open/futures/trade/history/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-transaction-details-signed
        :Parameter: request body
        |
        """

        params = {}
        if fromId:
            params["fromId"] = fromId
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
        if pageSize:
            params["pageSize"] = pageSize
        url_path = "/open/futures/trade/history/v1"
        return self._request("GET", url_path, params)
