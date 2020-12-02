import allure
import pytest
import requests
import random
from test_case.test_basic_data import *

@allure.title('新增发票')
@allure.story('新增发票')
def test_add_invoice():
    rand = random.randint(200, 999)
    title1 = 'abc' + str(rand)

    #添加个人发票
    r1 = requests.post(test_mic+'/micro-service/person-data/add-invoice',
                       headers=headers,
                       json={"type":"PERSONAL","title":title1,"userCode":msUserCode})
    result1 = r1.json()['data']
    print('添加个人发票：',r1.json)
    assert result1

    title2 = 'qiyeaa'+str(rand)
    taxNumber = '321'+str(rand)
    registeAddress = 'address1'+str(rand)
    companyMobile = '2323' +str(rand)
    bank = 'bank'+str(rand)
    bankAccount = '6217088'+str(rand)
    #添加企业发票
    r2 = requests.post(test_mic+'/micro-service/person-data/add-invoice',
                       headers=headers,
                       json={"title":title2,"type":"COMPANY",
                             "taxNumber":taxNumber,
                             "needVat":"Y",
                             "registeAddress":registeAddress,
                             "companyMobile":companyMobile,
                             "bank":bank,
                             "bankAccount":bankAccount,"userCode":msUserCode})
    result2 = r2.json()['data']
    print('添加企业发票：',r2.json())
    assert result2

@allure.title('删除发票')
@allure.story('删除发票')
def test_del_invoice(test_query_invoice):
    invoiceid = test_query_invoice[0]
    r = requests.get(test_mic+'/micro-service/person-data/del-invoice/'+str(invoiceid),
                     headers=headers)
    result = r.json()
    print('删除发票：',r.json())
    assert result['message']=='成功'