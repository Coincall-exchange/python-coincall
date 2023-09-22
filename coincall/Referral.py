from .client import Client

class ReferralAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', diff='3000', use_server_time=False, domain = 'https://api.coincall.com',debug = True):
        Client.__init__(self, api_key, api_secret_key, diff, use_server_time, domain, debug)

    def get_referrals(self, subAgentId=None, page=None):
        """
        |
        | **Get Referrals Record**
        | *Get referrals record.*

        :API endpoint: ``GET /open/referral/sub/v1``
        :API doc: https://docs.coincall.com/#referrals-referrals-record-signed
        :Parameter: query string
        |
        """

        params = {}
        if subAgentId:
            params["subAgentId"] = subAgentId
        if page:
            params["page"] = page
        url_path = "/open/referral/sub/v1"
        return self._request("GET", url_path, params)