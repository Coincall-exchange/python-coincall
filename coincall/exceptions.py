# coding=utf-8


class CcAPIException(Exception):

    def __init__(self, response):
        self.code = 0
        try:
            json_res = response.json()
        except ValueError:
            self.message = 'Invalid JSON error message from Coincall: {}'.format(response.text)
        else:
            if "code" in json_res.keys() and "msg" in json_res.keys():
                self.code = json_res['code']
                self.message = json_res['msg']
            else:
                self.code = 'None'
                self.message = 'System error'

        self.status_code = response.status_code
        self.response = response
        self.request = getattr(response, 'request', None)

    def __str__(self):  # pragma: no cover
        return 'API Request Error(code=%s): %s' % (self.code, self.message)


class CcRequestException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'CcRequestException: %s' % self.message


class CcParamsException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'CcParamsException: %s' % self.message
