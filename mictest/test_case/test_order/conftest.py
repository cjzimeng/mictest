import pytest
import requests
from test_case.test_basic_data import *

#查询产品列表
@pytest.fixture()
def test_get_list():
    r = requests.post(test_mic+'/micro-service/productswx',
                      headers = headers,
                      params = {'pageNum': 1, 'pageSize': 10},
                      json={
                          "sort": 0,
                          "reserveCityId": 9980939,
                          "productThemeName": [],
                          "productTag": [],
                          "productFeatureName": [],
                          "travelDay": [],
                          "startPrice": None,
                          "endPrice": None,
                          "searchWord": None,
                          "suggestField": {
                              "filedName": None,
                              "govPoiId": None,
                              "docId": None,
                              "val": None,
                              "searchType": "must"
                          },
                          "topSearchField": {
                              "filedName": "001",
                              "val": ["周边", "国内长线"]
                          },
                          "size": 10,
                          "pageNum": 1
                      })
    prod_list = r.json()['data']['productList']
    assert len(prod_list)>0

    prodid = []
    if prod_list:
        for i in prod_list:
            prodid.append(i['id'])
    #返回产品id
    return prodid

#查询某产品下的线路id
@pytest.fixture()
def test_product_basic(test_get_list):
    prodidtmp = test_get_list[0]
    #prodid = 112
    r = requests.get(test_mic + '/micro-service/product/' + str(proid),
                     headers=headers)
    result = r.json()['data']
    print('产品名称', result['title'], result['productNumber'])
    assert result['title']!= None

    line_list = result['lineWXDtos']
    line_id = []
    for i in line_list:
        line_id.append(i['lineId'])
    #返回线路id
    return line_id

#查询订单列表
@pytest.fixture()
def test_order_list(request):
    queryType = request.param['queryType']
    r = requests.post(test_mic+'/micro-service/order/page/list',
                      headers = headers,
                      json = {'pageNum':1,'pageSize':10,'queryType':queryType,'userCode':msUserCode})
    assert r.json()['message'] == '成功'
    order_list = r.json()['data']['list']
    order_id = []
    for i in order_list:
        order_id.append(i['orderId'])
    return order_id

#查询旅客列表
@pytest.fixture()
def test_query_travel():
    r = requests.get(test_mic+'/micro-service/ms/traveller/list/'+str(msUserCode)+'/1/10',
                     headers=headers)
    result = r.json()['data']['list']
    travelcode = []
    for i in result:
        travelcode.append(i['trallerCode'])
    return travelcode

#查询联系人列表
@pytest.fixture()
def test_query_contacts():
    r = requests.post(test_mic+'/micro-service/ms/person/list',
                      headers=headers,
                      json={"userCode":msUserCode,"pageNum":1,"pageSize":15})
    result = r.json()['data']['list']
    contactid = []
    for i in result:
        contactid.append(i['id'])
    return contactid

#查询联系地址列表
@pytest.fixture()
def test_query_address():
    r = requests.post(test_mic+'/micro-service/person-data/address-list',
                      headers=headers,
                      json={"userCode":msUserCode,"pageNum":1,"pageSize":10})
    result = r.json()['data']['list']
    addressid = []
    for i in result:
        addressid.append(i['id'])
    return addressid

#查询发票列表
@pytest.fixture()
def test_query_invoice():
    r = requests.post(test_mic+'/micro-service/person-data/invoice-list',
                      headers=headers,
                      json={"userCode":msUserCode,"pageNum":1,"pageSize":10,"status":0})
    result = r.json()['data']['list']
    invoiceid = []
    for i in result:
        invoiceid.append(i['id'])
    return invoiceid

#查询出游需求列表
@pytest.fixture()
def test_query_demand():
    r = requests.post(test_mic+'/micro-service/customized-demand/list',
                      headers=headers,
                      json={"pageNum":1,"pageSize":10,"userCode":msUserCode})
    result = r.json()['data']['list']
    demandid = []
    for i in result:
        demandid.append(i['id'])
    return demandid