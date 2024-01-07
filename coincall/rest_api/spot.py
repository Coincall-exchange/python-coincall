from .client import Client


class SpotAPI(Client):
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

    def get_symbols(self, symbol=None, limit=None):
        """
        |
        | **Get Instruments**
        | *Query for the instrument specification of online trading pairs..*

        :API endpoint: ``GET /open/spot/market/instruments``
        :API doc: https://docs.coincall.com/#spot-endpoint-get-instruments-signed
        :Parameter: request body
        |
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
        if limit:
            params["limit"] = limit
        url_path = "/open/spot/market/instruments"
        return self._request("GET", url_path, params)

    def get_kline(self, symbol, interval, start=None, end=None, limit=None):
        """
        |
        | **Get Kline**
        | *Query for historical klines (also known as candles/candlesticks).*

        :API endpoint: ``GET /open/spot/market/klines``
        :API doc: https://docs.coincall.com/#spot-endpoint-kline-signed
        :Parameter: request body
        |
        """
        params = {"symbol": symbol, "interval": interval}
        if start:
            params["start"] = start
        if end:
            params["end"] = end
        if limit:
            params["limit"] = limit
        url_path = "/open/spot/market/klines"
        return self._request("GET", url_path, params)

    def get_orderbook(self, symbol, depth=None):
        """
        |
        | **Get Orderbook**
        | *Query for orderbook depth data..*

        :API endpoint: ``GET /open/spot/market/orderbook``
        :API doc: https://docs.coincall.com/#spot-endpoint-get-orderbook-signed
        :Parameter: request body
        |
        """

        params = {"symbol": symbol}
        if depth:
            params["depth"] = depth
        url_path = "/open/spot/market/orderbook"
        return self._request("GET", url_path, params)

    def get_public_trades(self, symbol, limit=None):
        """
        |
        | **Get Public Trading History**
        | *Query recent public trading data.*

        :API endpoint: ``GET /open/spot/market/histories``
        :API doc: https://docs.coincall.com/#spot-endpoint-get-public-trading-history-signed
        :Parameter: request body
        |
        """

        params = {"symbol": symbol}
        if limit:
            params["limit"] = limit
        url_path = "/open/spot/market/histories"
        return self._request("GET", url_path, params)

    def get_tickers24hr(self, symbol=None):
        """
        |
        | **Get Tickers 24hr**
        | *Query for the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.*

        :API endpoint: ``GET /open/spot/market/overviewV2``
        :API doc: https://docs.coincall.com/#spot-endpoint-get-tickers-24hr-signed
        :Parameter: request body
        |
        """

        params = {}
        if symbol:
            params["symbol"] = symbol
        url_path = "/open/spot/market/overviewV2"
        return self._request("GET", url_path, params)

    def place_order(
        self, symbol, qty, tradeSide, tradeType, clientOrderId=None, price=None
    ):
        """
        |
        | **Place Order**
        | *Create a new order.*

        :API endpoint: ``POST /open/spot/trade/order/v1``
        :API doc: https://docs.coincall.com/#spot-endpoint-place-order-signed
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
        url_path = "/open/spot/trade/order/v1"
        return self._request("POST", url_path, params)

    def cancel_order(self, orderId=None, clientOrderId=None):
        """
        |
        | **Cancel Order**
        | *Cancel an open order.*

        :API endpoint: ``POST /open/trade/spot/cancel/v1``
        :API doc: https://docs.coincall.com/#spot-endpoint-cancel-order-signed
        :Parameter: request body
        |
        """

        params = {}
        if orderId:
            params["orderId"] = orderId
        if clientOrderId:
            params["clientOrderId"] = clientOrderId
        url_path = "/open/spot/trade/cancel/v1"
        return self._request("POST", url_path, params)

    def cancel_orders(self, symbol):
        """
        |
        | **Cancel Orders**
        | *Cancels all active orders on one symbol.*

        :API endpoint: ``POST /open/spot/trade/cancelAll/v1``
        :API doc: GET https://docs.coincall.com/#spot-endpoint-cancel-orders-signed
        :Parameter: request body
        |
        """

        params = {"symbol": symbol}
        url_path = "/open/spot/trade/cancelAll/v1"
        return self._request("POST", url_path, params)

    def get_order_info(self, orderId=None, clientOrderId=None):
        """
        |
        | **Query Order**
        | *Check an order's status.*

        :API endpoint: ``GET /open/spot/trade/order/v1``
        :API doc: https://docs.coincall.com/#spot-endpoint-query-order-signed
        :Parameter: request body
        |
        """

        params = {}
        if orderId:
            params["orderId"] = orderId
        if clientOrderId:
            params["clientOrderId"] = clientOrderId
        url_path = "/open/spot/trade/order/v1"
        return self._request("GET", url_path, params)

    def get_open_orders(self, symbol=None):
        """
        |
        | **Query Open Orders**
        | *Get all open orders.*

        :API endpoint: ``GET /open/spot/trade/orders/v1``
        :API doc: https://docs.coincall.com/#spot-endpoint-query-open-orders-signed
        :Parameter: request body
        |
        """

        params = {}
        if symbol:
            params["symbol"] = symbol
        url_path = "/open/spot/trade/orders/v1"
        return self._request("GET", url_path, params)

    def get_all_orders(self, symbol=None, limit=None, startTime=None, endTime=None):
        """
        |
        | **Query All Orders**
        | *Get all orders; active, canceled, or filled.*

        :API endpoint: ``GET /open/spot/trade/allorders/v1``
        :API doc: https://docs.coincall.com/#spot-endpoint-query-all-orders-signed
        :Parameter: request body
        |
        """

        params = {}
        if symbol:
            params["symbol"] = symbol
        if limit:
            params["limit"] = limit
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
        url_path = "/open/spot/trade/allorders/v1"
        return self._request("GET", url_path, params)

    def get_fills(
        self, symbol=None, orderId=None, limit=None, startTime=None, endTime=None
    ):
        """
        |
        | **Query Fill List**
        | *Get fills trade list.*

        :API endpoint: ``GET /open/spot/trade/fills/v1``
        :API doc: https://docs.coincall.com/#spot-endpoint-query-fill-list-signed
        :Parameter: request body
        |
        """

        params = {}
        if symbol:
            params["symbol"] = symbol
        if orderId:
            params["orderId"] = orderId
        if limit:
            params["limit"] = limit
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
        url_path = "/open/spot/trade/fills/v1"
        return self._request("GET", url_path, params)
