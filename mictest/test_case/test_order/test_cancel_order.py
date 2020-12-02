# import pytest
# import allure
# import requests
# from test_case.test_basic_data import *
#
# queryData = [{'queryType':1}]
# #查询订单列表
# @allure.title('取消订单')
# @allure.story('取消订单')
# @pytest.mark.parametrize('test_order_list',queryData,indirect=True)
# def test_cancel_order(test_order_list):
#     orderid = test_order_list[0]
#     r = requests.put(test_mic+'/micro-service/order/pre/cancel/'+str(orderid),
#                          headers=headers)
#     # print(r.json()['data']['validCode'])
#     validcode = (r.json()['data'])['validCode']
#     r = requests.put(test_mic+'/micro-service/order/miniapp-cancel/',
#                      headers=headers,
#                      json={
#                          'orderId': str(orderid),
#                          'validCode': validcode,
#                          'operateUid': 86
#                      })
#     assert r.json()['message'] == '成功'
