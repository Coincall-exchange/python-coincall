import unittest
from coincall import User

class userTest(unittest.TestCase):
    def setUp(self):
        api_key = 'xdtHWn32rsuDQConutzl9JDZB+Y1leitFl356YHrmts='
        api_secret_key = 'LIvSQPOTSS+CaxqrsbbWnM/R02WksxA/W2JdYK62AxE='
        self.userApi = User.UserAPI(api_key, api_secret_key, use_server_time=False)


    def test_get_server_time(self):
        print(self.userApi.get_user_info())

    def test_get_config(self):
        print(self.userApi.get_account_summary())

if __name__ == '__main__':
    unittest.main()