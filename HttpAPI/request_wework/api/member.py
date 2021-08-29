from string import Template

import yaml

from HttpAPI.request_wework.api.baseapi import BaseApi
from HttpAPI.request_wework.api.wework import WeWork


class MemberCurd(BaseApi):

    def __init__(self):
        secret = "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"
        # 获取token
        self.token = WeWork().get_token(secret)

    # 添加成员
    def create(self, userid, name, mobile):
        data = self.template(userid, name, mobile)
        print(data)
        return self.send(data)

    # 更新成员
    def update(self, userid, name, mobile):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile}

        }
        return self.send(data)

    # 读取成员信息
    def getMemberlist(self, userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        return self.send(data)

    # 删除成员
    def delete(self, userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        return self.send(data)
