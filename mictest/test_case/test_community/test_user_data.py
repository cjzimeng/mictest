import allure
import requests
from test_case.test_basic_data import *

@allure.title("查看自己的笔记中心")
@allure.story("查看自己的笔记中心")
def test_user_self():
    r = requests.post(test_host1+'/community/query-user-data',
                      headers=headers1,
                      json={
                          "userId": userid,
                          "notePageNum": 1,
                          "notePageSize": 6,
                          "collectionPageNum": 1,
                          "collectionPageSize": 6,
                          "loginUserId": userid
                      })
    result = r.json()['message']
    assert result=='成功'
    userdata = r.json()['data']['userData']
    print('用户信息：',userdata)
    assert userdata

@allure.title("查看他人的笔记中心")
@allure.story("查看他人的笔记中心")
def test_user_other():
    r = requests.post(test_host1+'/community/query-user-data',
                      headers=headers1,
                      json={
                          "userId": 88,
                          "notePageNum": 1,
                          "notePageSize": 6,
                          "collectionPageNum": 1,
                          "collectionPageSize": 6,
                          "loginUserId": userid
                      })
    result = r.json()['message']
    assert result=='成功'
    userdata = r.json()['data']['userData']
    print('查看的用户信息：',userdata)
    assert userdata