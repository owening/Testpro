# 获取access_token
import random
import re

import pytest
import requests


# 获取access_token
@pytest.fixture(scope="session")
def test_getToken():
    res = None
    corpid = "wwc21827e63c44f94f"
    corpsecret = "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    print("getToken")
    return res.json()["access_token"]


# 读取成员信息
def test_get_memberlist(userid, test_getToken):
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_getToken}&userid={userid}")
    return res.json()


# 添加成员
def test_create_member(userid, name, mobile, test_getToken):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [2]
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_getToken}", json=data)
    return res.json()


# 更新成员
def test_update_member(userid, name, mobile, test_getToken):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_getToken}", json=data)
    return res.json()


# 删除成员
def test_delete_member(userid, test_getToken):
    res = requests.get(
        f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_getToken}&userid={userid}")
    return res.json()


def test_create_data():
    # 生成列表数据方法一，有重复
    test_data = [(str(random.randint(0, 9999999)), "随机用户", str(random.randint(13752000001, 13752999999))
                  ) for x in range(10)
                 ]

    # 生成列表数据方法二
    data = [["test" + str(x), "诺亚方舟" + str(x), "136%08d" % x] for x in range(20)]
    return data


@pytest.mark.parametrize("userid,name,mobile", test_create_data())
def test_all(userid, name, mobile, test_getToken):
    # 捕捉创建失败进行处理
    try:
        assert "created" == test_create_member(userid, name, mobile, test_getToken)["errmsg"]
        print("正常添加成功")
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            re_userid = re.findall(":(.*)", e.__str__())[0]
            if re_userid.endswith('"') or re_userid.endswith("'"):
                #如果re_userid后面存在'or"就截取去除最后一位
                re_userid = re_userid[:-1]
            # 若存在相同手机号，先获取出来再删除
            assert "deleted" == test_delete_member(re_userid, test_getToken)["errmsg"]
            assert 60111 == test_get_memberlist(userid, test_getToken)["errcode"]
            assert "created" == test_create_member(userid, name, mobile, test_getToken)["errmsg"]
            print("特殊添加成功")
    assert name == test_get_memberlist(userid, test_getToken)["name"]
    assert "updated" == test_update_member(userid, "尤可", mobile, test_getToken)["errmsg"]
    assert "尤可" == test_get_memberlist(userid, test_getToken)["name"]
    assert "deleted" == test_delete_member(userid, test_getToken)["errmsg"]
    # 删除后userid不存在了
    assert 60111 == test_get_memberlist(userid, test_getToken)["errcode"]
