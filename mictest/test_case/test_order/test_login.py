import json

import allure
import requests

from test_case.test_basic_data import *

#
# @allure.description("测试登录")
# @allure.title('测试登录用例')
# @allure.testcase('http://calapi.51jirili.com/dream/categoryList','登录用例地址')
# def test_login():
#     r = requests.post(test_host+'/micro-service/relation/wx-user',
#                       headers = headers,
#                       json={
#                           "openId":openId,
#                           "mobile": "13058041296",
#                           "userId": 86,
#                           "nickName": "cecilia"
#                       })
#     print(json.dumps(r.json(), indent=2, ensure_ascii=False))
#     assert (r.json()['data'])['realName'] == '陈姣'
