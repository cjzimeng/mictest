import pytest
import requests
from test_case.test_basic_data import *

@pytest.fixture()
def test_get_note():
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
    note_list = r.json()['data']['note']['list']
    noteid = []
    for i in note_list:
        noteid.append(i['id'])
    return noteid