from HttpAPI.request_wework.api.wework import WeWork


class TestBase:
    def test_getToken(self):
        secret = "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"
        # 获取token
        self.token = WeWork().get_token(secret)
        return self.token
