import requests
import allure
import pytest
from test_case.test_basic_data import *
#查询待付款列表
queryData = [{'queryType': 2}]
@allure.title('调用预支付')
@allure.story('调用预支付')
@pytest.mark.parametrize('test_order_list',queryData,indirect=True)
def test_pay(test_order_list):
    orderid = test_order_list[0]
    #获取订单信息
    r = requests.get(test_host+'/micro-service/order/payinfodetails/'+str(orderid),
                     headers = headers)
    result = r.json()['data']
    orderCode = result['orderCode']
    body = result['title']
    totalMoney = result['needPayTotal']

    #调用预支付
    r = requests.post(test_host+'/micro-service/wxjspay-unifiedorder',
                      headers = headers,
                      json = { "orderId": str(orderid),
                                 "orderCode": orderCode,
                                 "totalMoney": str(totalMoney),
                                 "body": body,
                                 "openid": openId})
    assert r.json()['message'] == '成功'
