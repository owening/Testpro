from HttpAPI.request_wework.api.baseapi import BaseApi


class WeWork(BaseApi):

    # 获取token
    def get_token(self, secret):
        corpid = "wwc21827e63c44f94f"
        corpsecret = secret
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        return self.send_api(data)["access_token"]
