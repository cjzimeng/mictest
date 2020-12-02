import pytest
import allure
import requests
import random
from test_case.test_basic_data import *

@allure.title('新增联系地址')
@allure.story('新增联系地址')
def test_add_address():
    rand = random.randint(200, 999)
    name = 'a' + str(rand)

    str_start = random.choice(['135', '136', '138'])
    str_end = ''.join(random.sample('0123456789', 8))
    str_phone = str_start + str_end

    detail = '详细地址b'+str(rand)
    r = requests.post(test_mic+'/micro-service/person-data/add-address',
                      headers=headers,
                      json={"name":name,
                            "mobile":str_phone,
                            "provinceId":4051,
                            "cityId":80939,
                            "divisionId":272755,
                            "detail":detail,"postcode":None,"division":"岳麓区",
                            "userCode":msUserCode})
    result = r.json()['data']
    assert result