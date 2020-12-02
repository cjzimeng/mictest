

import allure
import pytest
import requests
import random
from test_case.test_basic_data import *

@allure.title("未登录发现页进入笔记详情")
@allure.story("未登录发现页进入笔记详情")
def test_foundlist():
    r = requests.get(test_host1+'/community/note/found',
                      headers=headers1,
                      params={"pageSize":10,"pageNum":1,"userId":None})
    note_list = r.json()['data']['foundNoteList']['list']
    assert note_list

    noteid_list = []
    for i in note_list:
        noteid_list.append(i['id'])

    #第一页发现列表返回的笔记数据中随机取一个笔记id
    note_id = random.choice(noteid_list)

    r1 = requests.get(test_host1+'/community/note/detail/'+note_id+'-0',
                      headers=headers1)
    result = r1.json()['data']['title']
    assert result

@allure.title("已登录发现页进入笔记详情")
@allure.story("已登录发现页进入笔记详情")
def test_foundlist_login():
    pass
