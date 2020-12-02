
import pytest
import allure
import requests
import random
import time
from test_case.test_basic_data import *

@allure.title('新增旅客')
@allure.story('新增旅客')
def test_add_travel():
    rand = random.randint(300000,900000)
    cardNum = '430822'+ str(rand)
    fullName = 'a'+str(rand)
    lastName = 'b'+str(rand)
    firstName = 'c'+str(rand)
    start = time.mktime((1971,1,1,0,0,0,0,0,0))
    end = time.mktime((2020,4,30,2,3,5,9,5,9))
    t = random.randint(start, end)
    date_touple = time.localtime(t)
    birthday = time.strftime("%Y-%m-%d", date_touple)

    r = requests.post(test_mic+'/micro-service/ms/traveller/'+str(userid),
                      headers = headers,
                      json={
                          "userCode": msUserCode,
                          "id": "",
                          "code": "",
                          "fullName": fullName,
                          "lastName": lastName,
                          "firstName": firstName,
                          "sex": "1",
                          "phone": "",
                          "email": "",
                          "birthday": birthday,
                          "nationalityId": 334,
                          "nationality": "中国大陆(CN)",
                          "cardVoList": [
                              {
                                  "cardTypeName": "身份证",
                                  "validityTime": "2024-06-01",
                                  "cardNum": cardNum,
                                  "cardType": "carda",
                                  "id": ""
                              }
                          ]
                      })
    print('新增旅客：',r.json())
    assert r.json()['message'] == '成功'
    assert r.json()['data']

@allure.title('查看旅客详情')
@allure.story('查看旅客详情')
def test_edit_travel(test_query_travel):
    travelCode = test_query_travel[0]
    r = requests.get(test_mic+'/micro-service/ms/traller/detail/'+travelCode,
                     headers=headers)
    result = r.json()['data']['code']
    print('查看旅客详情：',r.json())
    assert result == travelCode

