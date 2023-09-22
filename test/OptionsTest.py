import unittest
from coincall import Options

class optionsTest(unittest.TestCase):
    def setUp(self):
        api_key = '-1'
        api_secret_key = '-1'
        self.optionsApi = Options.OptionsAPI(api_key, api_secret_key, use_server_time=False)


    def test_get_instruments(self):
        print(self.optionsApi.get_instruments('BTC'))

    def test_get_options_by_endtime(self):
        print(self.optionsApi.get_options_by_endtime(index='BTCUSD',endTime='1719561600000'))

    def test_get_option_by_name(self):
        print(self.optionsApi.get_option_by_name('BTCUSD-28JUN24-90000-P'))

    def test_get_depth(self):
        print(self.optionsApi.get_depth(symbol='BTCUSD-28JUN24-38000-C'))

    def test_get_lasttrade(self):
        print(self.optionsApi.get_lasttrade(symbol='BTCUSD-28JUN24-90000-P'))

    def test_get_positions(self):
        print(self.optionsApi.get_positions())

    def test_place_order(self):
        print(self.optionsApi.place_order(symbol='BTCUSD-28JUN24-38000-C',qty=0.5,tradeSide=1,tradeType=3,price=4000))

    def test_cancel_order(self):
        print(self.optionsApi.cancel_order(clientOrderId=1663004711982333952))

    def test_cancel_orders(self):
        print(self.optionsApi.cancel_orders(symbol='ETHUSD'))

    def test_get_open_orders(self):
        print(self.optionsApi.get_open_orders())

    def test_get_order_by_id(self):
        print(self.optionsApi.get_order_by_id(orderId=1663004711982333952))

    def test_get_order_history(self):
        print(self.optionsApi.get_order_history())

    def test_get_trade_history(self):
        print(self.optionsApi.get_trade_history())

if __name__ == '__main__':
    unittest.main()