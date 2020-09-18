import requests
from test_case.test_basic_data import *
import pytest
#
# @pytest.fixture()
# def test_get_list():
#     r = requests.post(test_host+'/micro-service/productswx',
#                       headers = headers,
#                       params = {'pageNum': 1, 'pageSize': 10},
#                       json={
#                           'destinationCategorys': None,
#                           'features': None,
#                           'higherPrice': None,
#                           'lowerPrice': None,
#                           'productId': None,
#                           'purposePlaceId': None,
#                           'reserveCityId': 9980939,
#                           'setOutCityId': None,
#                           'sort': None,
#                           'tags': None,
#                           'themes': None,
#                           'themesNotNull': '1',
#                           'travelDay': []
#                       })
#     prod_list = r.json()['data']['list']
#     prodid = []
#     if prod_list:
#         for i in prod_list:
#             prodid.append(i['productId'])
#     return prodid
#
#
# def test_proid(test_get_list):
#     print(test_get_list[0])
#


planDetail = [
    {
        "planName": "基础方案",
        "planId": 0,
        "remark": None,
        "signEndTime": "2020-09-16 00:00:00",
        "priceDetail": [
            {
                "price": 100,
                "priceCategoryId": 4039,
                "priceCategory": "单房差",
                "startingAge": None,
                "endAge": None,
                "heightDescription": None
            },
            {
                "price": 300,
                "priceCategoryId": 4040,
                "priceCategory": "成人",
                "startingAge": 18,
                "endAge": 60,
                "heightDescription": None
            },
            {
                "price": 200,
                "priceCategoryId": 4041,
                "priceCategory": "儿童",
                "startingAge": 2,
                "endAge": 12,
                "heightDescription": "身高1.2米以下"
            }
        ]
    },
    {
        "planName": "去程升级一等座",
        "planId": 326,
        "remark": "去程升级一等座",
        "signEndTime": "2020-09-16 00:00:00",
        "priceDetail": [
            {
                "price": 223,
                "priceCategoryId": 4039,
                "priceCategory": "单房差",
                "startingAge": None,
                "endAge": None,
                "heightDescription": None
            },
            {
                "price": 423,
                "priceCategoryId": 4040,
                "priceCategory": "成人",
                "startingAge": 18,
                "endAge": 60,
                "heightDescription": None
            },
            {
                "price": 322,
                "priceCategoryId": 4041,
                "priceCategory": "儿童",
                "startingAge": 2,
                "endAge": 12,
                "heightDescription": None
            }
        ]
    }
]

for i in planDetail:
    if i['planName'] == '基础方案':
         i['show'] = True
         for j in i['priceDetail']:
             if j['priceCategory'] == '单房差' or j['priceCategory'] == '成人':
                 j['reserveNum'] = 1
             else:
                 j['reserveNum'] = 0
    else:
        i['show'] = False
        for j in i['priceDetail']:
            j['reserveNum'] = 0
import datetime
datea = '2020-9-18'
# print(type((((datetime.datetime.strptime(datea, '%Y-%m-%d').date()))+datetime.timedelta(days=1)).strftime("%Y-%m-%d")))
# print(datea)
# r = requests.get('https://miniapptest.yujianmeihao.net/api/micro-service/product/483',
#                  headers = headers)
# travelDay = r.json()['data']['travelDay']
# print(type(travelDay))
# import request
# #
# @pytest.fixture()
# def test_order_list(request):
#     queryType = request.param['queryType']
#     r = requests.post(test_host+'/micro-service/order/page/list',
#                       headers = headers,
#                       json = {
#                           "userCode": 707827,
#                           "pageNum": 1,
#                           "pageSize": 10,
#                           "queryType": queryType
#                       })
#     order_list = (r.json()['data'])['list']
#     order_id = []
#     for i in order_list:
#         order_id.append(i['orderId'])
#     return order_id
#
# queryData = [{'queryType':2}]
#
# @pytest.mark.parametrize('test_order_list',queryData,indirect=True)
# def test_cancel_order(test_order_list):
#     orderida = test_order_list[0]
#     orderid = 3134
#     r2 = requests.put('https://miniapptest.yujianmeihao.net/api/micro-service/order/pre/cancel/'+str(orderid),
#                       headers=headers)
#     print(r2.json())


headersa = {
           'Accept-Encoding': 'gzip, deflate, br',
           'content-type': 'application/json;charset=UTF-8',
           'Connection': 'Keep-Alive',
           'Host': 'miniapptest.yujianmeihao.net',
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 wechatdevtools/1.02.1911180 MicroMessenger/7.0.4 Language/zh_CN webview/'}


r1 = requests.get('https://miniapptest.yujianmeihao.net/api/micro-service/order/list/count/707827',
                  headers = headers)

r = requests.post('https://miniapptest.yujianmeihao.net/api/micro-service/order/page/list',
                      headers = headersa,
                      json={"userCode":707827,"pageNum":1,"pageSize":10,"queryType":2})
# print(r.json())

r1 = requests.get('https://miniapptest.yujianmeihao.net/api/micro-service/order/list/count/707827',
                  headers = headers)
# print(r1.json())


r2 = requests.put('https://miniapptest.yujianmeihao.net/api/micro-service/order/pre/cancel/3134',
                         headers=headers)
# print(r2.json())
import random
rand = random.randint(300000,800000)
# print(rand)


import datetime
import time
s = (2000,4,1,0,0,0,0,0,0) #设置开始日期时间元组（2019-08-01 00：00：00）
e = (2020,4,30,2,3,5,9,5,9) #设置结束日期时间元组（2019-08-31 23：59：59)
start = time.mktime(s) #生成开始时间戳
end = time.mktime(e) #生成结束时间戳
t = random.randint(start, end) # 在开始和结束时间戳中随机取出一个
date_touple = time.localtime(t) # 将时间戳生成时间元组
date = time.strftime("%Y-%m-%d", date_touple)
# print(date)
#
# r = requests.get(test_host+'/micro-service/ms/traveller/list/707827/1/10',
#                      headers=headers)
# result = r.json()['data']['list']
# travelcode = []
# for i in result:
#     travelcode.append(i['trallerCode'])
# print(type(travelcode[0]))
#
#
# import random
#
# str_start=random.choice(['135','136','138'])
# str_end=''.join(random.sample('0123456789',8))
# str_phone=str_start+str_end
# print(str_phone)

r = requests.post(test_host+'/micro-service/ms/person/list',
                      headers=headers,
                      json={"userCode":707827,"pageNum":1,"pageSize":15})
result = r.json()['data']['list']
contactid = []
for i in result:
    contactid.append(i['id'])

r = requests.post(test_host+'/micro-service/person-data/address-list',
                      headers=headers,
                      json={"userCode":707827,"pageNum":1,"pageSize":10})
result = r.json()['data']['list']
addressid = []
for i in result:
    addressid.append(i['id'])

# print(type(addressid[0]))

print(type((datetime.datetime.now()).strftime('%Y-%m-%d')))
date = (datetime.datetime.now()).strftime('%Y-%m-%d')
a = (datetime.datetime.strptime(date,'%Y-%m-%d').date()+datetime.timedelta(days=10)).strftime("%Y-%m-%d")
print(a)