import pytest
import allure
import requests
import random
from test_case.test_basic_data import *

@allure.title('添加联系人')
@allure.story('添加联系人')
def test_add_contact():
    rand = random.randint(200,999)
    name = 'a'+str(rand)

    str_start = random.choice(['135', '136', '138'])
    str_end = ''.join(random.sample('0123456789', 8))
    str_phone = str_start + str_end
    r = requests.post(test_host+'/micro-service/ms/person',
                      headers=headers,
                      json={"name":name,"mobile":str_phone,"sex":1,"userCode":707827})
    result = r.json()['data']
    assert result

@allure.title('删除联系人')
@allure.story('删除联系人')
def test_del_contact(test_query_contacts):
    contactid = test_query_contacts[0]
    r = requests.delete(test_host+'/micro-service/ms/person/'+str(contactid),
                        headers=headers)
    result = r.json()
    assert result['message'] == '成功'