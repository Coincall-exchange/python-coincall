import unittest
from coincall.user import UserAPI


class UserTest(unittest.TestCase):
    def setUp(self):
        api_key = "-1"
        api_secret_key = "-1"
        self.userApi = UserAPI(api_key, api_secret_key, use_server_time=False)

    def test_get_user_info(self):
        print(self.userApi.get_user_info())

    def test_get_account_summary(self):
        print(self.userApi.get_account_summary())


if __name__ == "__main__":
    unittest.main()
