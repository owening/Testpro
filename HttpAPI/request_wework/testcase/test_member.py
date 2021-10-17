# -*- coding: utf-8 -*-
import allure
import pytest
import yaml

from HttpAPI.request_wework.api.member import MemberCurd
from HttpAPI.request_wework.testcase.test_base import TestBase

@allure.feature("成员接口测试")
class TestMember(TestBase):

    def setup(self):
        self.member = MemberCurd()
        self.test_getToken()

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("添加成员")
    @pytest.mark.parametrize("userid,name,mobile", yaml.safe_load(
        open("C:/Users/Administrator/PycharmProjects/Testpro/HttpAPI/request_wework/data/test_member.yaml",encoding="utf-8").read()))
    def test_create(self, userid, name, mobile):
        res = self.member.create(self.token, userid, name, mobile)
        assert res["errcode"] == 0
        assert "created" in res["errmsg"]

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("获取成员信息")
    def test_getmemberInfo(self):
       res= self.member.getMemberInfo(self.token,"Test003")
       assert res["userid"] == "Test003"
       assert "ok" in res["errmsg"]


