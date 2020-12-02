
import allure
import pytest
import requests
import random
import datetime
from test_case.test_basic_data import *

@allure.title('添加出游需求')
@allure.story('添加出游需求')
def test_add_demand():
    rand = random.randint(200, 999)
    name = 'abc' + str(rand)

    str_start = random.choice(['135', '136', '138'])
    str_end = ''.join(random.sample('0123456789', 8))
    str_phone = str_start + str_end

    date = (datetime.datetime.now()).strftime('%Y-%m-%d')
    tripDate= (datetime.datetime.strptime(date,'%Y-%m-%d').date()+datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    r = requests.post(test_mic+'/micro-service/customized-demand',
                      headers=headers,
                      json={"userCode":msUserCode,
                            "contactIds":[],
                            "name":name,
                            "mobile":str_phone,
                            "email":"",
                            "qq":"",
                            "departure":"99272985",
                            "destination":"99273089",
                            "tripDate":tripDate,
                            "days":"","population":"","preBudget":"","source":"MINI_APP"})
    result = r.json()['data']
    assert result

@allure.title('删除出游需求')
@allure.story('删除出游需求')
def test_del_demand(test_query_demand):
    demandid = test_query_demand[0]
    r = requests.delete(test_mic+'/micro-service/customized-demand/'+str(demandid),
                        headers=headers)
    result = r.json()['data']
    assert result == demandid