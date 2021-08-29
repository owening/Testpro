import base64
import json

from HttpAPI.request_env import envrequest

class TestEnvReq:

    def setup(self):
        self.testenv = envrequest.test_env()


    def test_envreq(self):
        r = self.testenv.envreq()
        res = json.loads(base64.b64decode(r.content))
        print(res)
