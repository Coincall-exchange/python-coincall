from .client import Client

class UserAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', diff='3000', use_server_time=False, domain = 'https://api.coincall.com',debug = True):
        Client.__init__(self, api_key, api_secret_key, diff, use_server_time, domain, debug)

    def get_user_info(self):
        """
        |
        | **Get User Info**
        | *User Info.*

        :API endpoint: ``GET /open/user/info/v1``
        :API doc: https://docs.coincall.com/#user-account-related-get-user-info-signed
        |
        """

        params = {}
        url_path = "/open/user/info/v1"
        return self._request("GET", url_path, params)
    
    def get_account_summary(self):
        """
        |
        | **Get Account Summary**
        | *Account summary.*

        :API endpoint: ``GET /open/account/summary/v1``
        :API doc: https://docs.coincall.com/#user-account-related-get-account-summary-signed
        |
        """

        params = {}
        url_path = "/open/account/summary/v1"
        return self._request("GET", url_path, params)