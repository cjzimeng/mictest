
import allure
import requests
import json
import pytest
import datetime
from test_case.test_basic_data import *

@allure.title('产品预订测试')
@allure.testcase('http://calapi.51jirili.com/dream/categoryList','预订用例地址')
@allure.feature('产品预订')
def test_book(test_get_list):
    proid = test_get_list[0]
    # 查询产品线路ID
    r = requests.get(test_host + '/micro-service/lines',
                     headers=headers,
                     params={'productId': proid})
    assert r.json()['message'] == '成功'
    line = r.json()['data']
    lineid = line[0]['lineId']
    minprice = line[0]['lineLowerPrice']

    #查询线路ID对应的团期
    r = requests.get(test_host+'/micro-service/tourprice/tourprices/'+str(lineid),
                     headers = headers)
    line_tour = (r.json()['data'][0])['selectedTourPeriod']

    #查询产品方案及对应价格信息
    r = requests.post(test_host+'/micro-service/person-data/order-product',
                     headers = headers,
                     json = {'cityId':9980939,'lineId':lineid,'productImg':'','selectedTime':line_tour})
    planDetail = (r.json()['data']['productPlan'])['planDetail']
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

    # 创建订单
    r = requests.post(test_host + '/micro-service/order/draft/86',
                      headers=headers,
                      json={'token': 'onMss5Kh39RvesEx08eIloCgSsoo'})
    print(r.json()['data'])
    orderid = r.json()['data']

    #查询产品的天数
    r = requests.get(test_host+'/micro-service/product/'+str(proid),
                     headers = headers)
    travelDay = r.json()['data']['travelDay']
    backDate= (datetime.datetime.strptime(line_tour, '%Y-%m-%d').date()+datetime.timedelta(days=travelDay-1)).strftime("%Y-%m-%d")

    # 预订订单
    r = requests.post(test_host + '/micro-service/person-data/product-reserve',
                      headers=headers,
                      json={
                          "userId": 86,
                          "userCode": 707827,
                          "orderId": orderid,
                          "productId": proid,
                          "lineId": lineid,
                          "tripDate": line_tour,
                          "reserveCityId": 9980939,
                          "departureCityId": 9980939,
                          "backDate": backDate,
                          "reserveNum": 0,
                          "minPrice": minprice,
                          "memo": "",
                          "contactPersonId": "",
                          "planDetail": planDetail,
                          "confirmAgain": 1,
                          "trallers": [],
                          "singleRoomPlan": "ADVANCE"
                      })
    assert r.json()['message'] == '成功'
    assert r.json()['data'] == orderid

# @allure.title('取消订单')
# @allure.story('取消订单')
# def test_cancel():
#     orderid = '123'
#     r = requests.put(test_host + '/micro-service/order/pre/cancel/' + str(orderid),
#                      headers=headers)
#     print(r.json()['data']['validCode'])
#     validcode = r.json()['data']['validCode']
#     r = requests.put(test_host + '/micro-service/order/miniapp-cancel/',
#                      headers=headers,
#                      json={
#                          'orderId': orderid,
#                          'validCode': validcode,
#                          'operateUid': 86
#                      })
#     assert r.json()['message'] == '成功'