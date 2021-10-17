from string import Template

import yaml

from HttpAPI.request_wework.api.baseapi import BaseApi
from HttpAPI.request_wework.api.wework import WeWork


class MemberCurd(BaseApi):

    def __init__(self):
        secret = "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"
        # 获取token
        self.token = WeWork().get_token(secret)
        # self.member_req_path = "C:/Users/Administrator/PycharmProjects/Testpro/HttpAPI/request_wework/data/test_member.yaml"
        # str(self.member_req_path)

    # 添加成员
    def create(self, token, userid, name, mobile):
        data = self.template("../data/member_request.yaml",
                             {"access_token": token, "userid": userid, "name": name, "mobile": mobile}, "add")
        print(data)
        return self.send_api(data)

    # 更新成员
    def update(self, token, userid, name, mobile):
        data = self.template("../data/member_request.yaml",
                             {"access_token": token, "userid": userid, "name": name, "mobile": mobile}, "edit")
        print(data)
        return self.send_api(data)

    # 读取成员信息
    def getMemberInfo(self, token, userid):
        data = self.template("../data/member_request.yaml",
                             {"access_token": token, "userid": userid}, "select")
        print(data)
        return self.send_api(data)

    # 删除成员
    def delete(self, token, userid):
        data = self.template("../data/member_request.yaml",
                             {"access_token": token, "userid": userid}, "delete")
        print(data)
        return self.send_api(data)


