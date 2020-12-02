import pytest
import allure
import requests

from test_case.test_basic_data import *

@allure.title("未登录的关注列表")
@allure.story("未登录的关注列表")
def test_concern():
    r = requests.get(test_host1 + '/community/note/recommend/concern',
                      headers=headers1,
                      params={"pageSize": 10, "pageNum": 1, "userId": None})
    recommend_user = r.json()['data']['list']
    assert recommend_user

@allure.title("已登录未关注用户的关注列表")
@allure.story("已登录未关注用户的关注列表")
def test_concern_login():
    r = requests.get(test_host1+'/community/note/recommend/concern',
                     headers=headers1,
                     params={"pageSize": 10, "pageNum": 1, "userId": userid})
    recommend_user = r.json()['data']['list']
    assert recommend_user

@allure.title("已登录已关注用户的关注列表")
@allure.story("已登录已关注用户的关注列表")
def test_focus_login():
    r = requests.get(test_host1+'/community/note/focus',
                     headers=headers1,
                     params={"pageSize": 10, "pageNum": 1, "userId": userid})
    note_list = r.json()['data']['list']
    assert note_list
