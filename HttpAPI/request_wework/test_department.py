import requests


# 获取access_token
def test_getToken():
    res = None
    corpid = "wwc21827e63c44f94f"
    corpsecret = "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    return res.json()["access_token"]


# 获取部门列表
def test_get_departmentlist():
    res = None
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_getToken()}")
    print(res.json())


# 创建部门
def test_create_department():
    res = None
    data = {
        "name": "深圳一号中心",
        "parentid": 1
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_getToken()}", json=data)
    print(res.json())


# 更新部门
def test_update_department():
    res = None
    data = {
        "name": "深圳科技中心",
        "id": 2
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_getToken()}", json=data)
    print(res.json())


# 删除部门
def test_delete_department():
    res = None
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_getToken()}&ID=3")
    print(res.json())