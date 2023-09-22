import unittest
from coincall import Futures

class futuresTest(unittest.TestCase):
    def setUp(self):
        api_key = '-1'
        api_secret_key = '-1'
        self.futuresApi = Futures.FuturesAPI(api_key, api_secret_key, use_server_time=False)


    def test_get_symbols(self):
        print(self.futuresApi.get_symbols())

    def test_get_depth(self):
        print(self.futuresApi.get_depth(symbol='BTCUSD'))

    def test_get_lasttrade(self):
        print(self.futuresApi.get_lasttrade(symbol='BTCUSD'))

    def test_get_leverageh(self):
        print(self.futuresApi.get_leverage(symbol='BTCUSD'))

    def test_set_leverage(self):
        print(self.futuresApi.set_leverage(symbol='BTCUSD', leverage=1))

    def test_get_positions(self):
        print(self.futuresApi.get_positions())

    def test_place_order(self):
        print(self.futuresApi.place_order(symbol='BTCUSD',qty=0.5,tradeSide=1,tradeType=3,price=25000.1))

    def test_cancel_order(self):
        print(self.futuresApi.cancel_order(clientOrderId=1663004711982333952))

    def test_cancel_orders(self):
        print(self.futuresApi.cancel_orders(symbol='BTCUSD'))

    def test_get_open_orders(self):
        print(self.futuresApi.get_open_orders(symbol='BTCUSD'))

    def test_get_order_by_id(self):
        print(self.futuresApi.get_order_by_id(orderId=1663004711982333952))

    def test_get_order_history(self):
        print(self.futuresApi.get_order_history())

    def test_get_trade_history(self):
        print(self.futuresApi.get_trade_history())

if __name__ == '__main__':
    unittest.main()