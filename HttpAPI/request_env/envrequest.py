from HttpAPI.request_env.env_api import EnvApi


class test_env(EnvApi):

    def envreq(self):
        data = {
            "method": "get",
            "url": "http://www.testing.fision:9999/demo.txt",
            "headers": None
        }
        return self.send(data)
