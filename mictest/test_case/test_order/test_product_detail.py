
import allure
import requests
from test_case.test_basic_data import *


@allure.title('默认线路团期')
@allure.story('默认线路团期')
def test_line_tourprice(test_product_basic):
    lineid = test_product_basic[0]

    r = requests.get(test_mic+'/micro-service/tourprice/tourprices/'+str(lineid),
                     headers = headers)
    result = r.json()['data']
    assert len(result)>0

@allure.title('默认线路信息简介')
@allure.story('默认线路信息')
def test_line_simple(test_product_basic):
    lineid = test_product_basic[0]
    r = requests.get(test_mic+'/micro-service/line/trip/simple/'+str(lineid),
                     headers = headers)
    result = r.json()
    assert result['message'] == '成功'

@allure.title('默认线路特色')
@allure.story('默认线路特色')
def test_line_characteristic(test_product_basic):
    lineid = test_product_basic[0]
    r = requests.get(test_mic+'/micro-service/line-characteristics/'+str(lineid),
                     headers = headers)
    result = r.json()
    assert result['message'] == '成功'

@allure.title('默认线路行程')
@allure.story('默认线路行程')
def test_line_trip(test_product_basic):
    lineid = test_product_basic[0]
    r = requests.get(test_mic+'/micro-service/line/trip/detail/'+str(lineid),
                     headers = headers,
                     params = {'rankdays':1})
    result = r.json()['data']
    assert result['1']

@allure.title('默认线路费用信息')
@allure.story('默认线路费用信息')
def test_line_cost(test_product_basic):
    lineid = test_product_basic[0]
    r = requests.get(test_mic+'/micro-service/cost',
                     headers = headers,
                     params = {'lineId':lineid})
    result = r.json()['data']
    assert result['contains'] and result['nocontains']

#
# @allure.title('产品详情更多推荐')
# @allure.story('产品详情更多推荐')
# def test_sameproduct(test_get_list):
#     proidtmp = test_get_list[0]
#     r = requests.get(test_mic+'/micro-service/sameproduct',
#                      headers = headers,
#                      params = {"cityId":9980939,
#                                "productId":proid,
#                                "price":1,
#                                "days":1})
#     result = r.json()['data']
#     assert len(result) == 6


