import unittest
from coincall.rest_api.referral import ReferralAPI


class ReferralTest(unittest.TestCase):
    def setUp(self):
        api_key = "-1"
        api_secret_key = "-1"
        self.referralApi = ReferralAPI(api_key, api_secret_key, use_server_time=False)

    def test_get_referrals(self):
        print(self.referralApi.get_referrals())


if __name__ == "__main__":
    unittest.main()
