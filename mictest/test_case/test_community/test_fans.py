import allure
import requests
from test_case.test_basic_data import *

@allure.title("关注用户")
@allure.story("关注用户")
def test_focus_user():
    r = requests.post(test_host1+'/community/concern',
                      headers=headers1,
                      json={"concernUserId":88,"userId":userid,"status":"Y"})
    print('关注用户：',r.json())
    result = r.json()['data']
    assert result

@allure.title("取消关注用户")
@allure.story("取消关注用户")
def test_cancel_focus():
    r = requests.post(test_host1+'/community/concern',
                      headers=headers1,
                      json={"concernUserId":88,"userId":userid,"status":"N"})
    print("取消关注用户：",r.json())
    result = r.json()['data']
    assert result

@allure.title("关注列表")
@allure.story("关注列表")
def test_concern():
    r = requests.post(test_host1+'/community/concern-fans',
                      headers=headers1,
                      json={"userId":userid,"type":"CONCERN","pageNum":1,"pageSize":10})
    print("查看关注列表人数：",r.json()['data']['total'])
    result = r.json()['message']
    assert result=='成功'

@allure.title("粉丝列表")
@allure.story("粉丝列表")
def test_fans():
    r = requests.post(test_host1+'/community/concern-fans',
                      headers=headers1,
                      json={"userId":userid,"type":"FANS","pageNum":1,"pageSize":10})
    print("查看粉丝列表人数：",r.json()['data']['total'])
    result = r.json()['message']
    assert result


