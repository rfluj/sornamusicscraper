
import requests

class Req:
    def __init__(self):
        self.session = requests.Session()

    def sendrequest(self, url, method="get", timeout=30, headers=None, data=None, allow_redirect=True):
        if method == 'get':
            try:
                response   = self.session.get(url, timeout=timeout, headers=headers, data=data, allow_redirects=allow_redirect)
                statuscode = response.status_code
                res        = response
                response.close()
                return statuscode, res
            except:
                return -2, False
        elif method == 'post':
            try:
                response   = self.session.post(url, timeout=timeout, headers=headers, data=data, allow_redirects=allow_redirect)
                statuscode = response.status_code
                res        = response
                response.close()
                return statuscode, res
            except:
                return -2, False
        else:
            return -1, False
