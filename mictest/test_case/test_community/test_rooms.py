import pytest
import allure
import requests
from test_case.test_basic_data import *

@allure.title("直播列表")
@allure.story("直播列表")
def test_roomlist():
    r = requests.get(test_host1+'/community/rooms/group?start=0&limit=90',
                     headers=headers1)
    finished = r.json()['data']['FINISHED']
    assert finished