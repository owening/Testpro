import profile

import requests
from hamcrest import *
from jsonpath import jsonpath
from requests.auth import HTTPBasicAuth


class TestDemo:
    #get请求不带参数
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    #get请求带参数
    def test_query(self):
        payload = {'name': 'owen',
                   'age': 25
                   }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    # 添加post请求
    def test_post_form(self):
        payload = {'name': 'owen',
                   'age': 25
                   }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    # 添加请求头(headers)
    def test_heards(self):
        header = {'Newheader': 'yoyo'}
        r = requests.get('https://httpbin.testing-studio.com/get', headers=header)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['Newheader'] == 'yoyo'

    # 添加post请求,使用json传参
    def test_post_json(self):
        payload = {'name': 'owen',
                   'age': 25
                   }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['json']['age'] == 25

    # 使用json断言
    def test_hogwarts_json(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.json())
        assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
        assert jsonpath(r.json(), '$..name')[0] == '开源项目'

    # 使用hamcrest断言体系，assert_that断言
    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.json())
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('开源项目'))

    #请求时通过headers添加cookie
    def test_header_cookie(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        header = {
            'Cookie': 'test_token=test123456',
            'User-Agent': 'test-agent'
        }
        r = requests.get(url=url, headers=header)
        print(r.request.headers)
        assert r.request.headers['Cookie'] == 'test_token=test123456'

    #请求时通过cookies参数添加cookie
    def test_cookie_data(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        header = {'User-Agent': 'test-agent'}
        cookies_data = {"test_token": "test123456"}
        r = requests.get(url=url, headers=header, cookies=cookies_data)
        print(r.request.headers)
        assert_that(r.request.headers['Cookie'], equal_to('test_token=test123456'))

    #需要进行认证(Auth)的请求,请求时传auth参数进行认证
    def test_auth(self):
        r = requests.get(
            url="https://httpbin.testing-studio.com/basic-auth/owen/123456",
            auth= HTTPBasicAuth('owen','123456')
        )
        print(r.text)
        print(r.json()['authenticated'])
        assert_that(r.json()['authenticated'],equal_to(True))