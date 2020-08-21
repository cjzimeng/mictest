import json
import requests


headers = {
           'Accept-Encoding': 'gzip, deflate, br',
           'content-type': 'application/json;charset=UTF-8',
           'Connection': 'Keep-Alive',
           'Host': 'miniapptest.yujianmeihao.net',
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 wechatdevtools/1.02.1911180 MicroMessenger/7.0.4 Language/zh_CN webview/'}


class TestMicapptest:
    def test_login(self):
        r = requests.post('https://miniapptest.yujianmeihao.net/api/micro-service/relation/wx-user',
                          headers = headers,
                          json={
                              "openId": "onMss5Kh39RvesEx08eIloCgSsoo",
                              "mobile": "13058041296",
                              "userId": 86,
                              "nickName": "cecilia"
                          })
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert (r.json()['data'])['realName'] == '陈姣'

    def test_get_list(self):
        r = requests.post('https://miniapptest.yujianmeihao.net/api/micro-service/productswx',
                          headers=headers,
                          params={'pageNum': 1, 'pageSize': 10},
                          json={
                              'destinationCategorys': "02",
                              'features':None,
                              'higherPrice': None,
                              'lowerPrice': None,
                              'productId': None,
                              'purposePlaceId': None,
                              'reserveCityId': 9980939,
                              'setOutCityId': None,
                              'sort': None,
                              'tags': None,
                              'themes': None,
                              'themesNotNull': None,
                              'travelDay': []
                          })
        assert r.json()['message'] == '成功'
        #print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        li = (r.json()['data'])['list']
        return li[0]['productId']

    def test_prodetail(self):
        proid = str(self.test_get_list())
        r = requests.get('https://miniapptest.yujianmeihao.net/api/micro-service/product/'+proid,
                         headers=headers)
        assert r.json()['message'] == '成功'
        print(r.json())

    # def test_book(self):
    #     proid = self.test_get_list()
    #     # 查询产品线路ID
    #     r = requests.get('https://miniapptest.yujianmeihao.net/api/micro-service/lines',
    #                      headers=headers,
    #                      params={'productId':proid})
    #     assert r.json()['message'] == '成功'
    #     line = r.json()['data']
    #     lineid = line[0]['lineId']
    #     minprice = line[0]['lineLowerPrice']
    #
    #     # 创建订单
    #     r = requests.post('https://miniapptest.yujianmeihao.net/api/micro-service/order/draft/86',
    #                       headers=headers,
    #                       json={'token': 'onMss5Kh39RvesEx08eIloCgSsoo'})
    #     print(r.json()['data'])
    #     orderid = r.json()['data']
    #
    #     # 预订订单
    #     r = requests.post('https://miniapptest.yujianmeihao.net/api/micro-service/person-data/product-reserve',
    #                       headers=headers,
    #                       json={
    #                           "userId": 86,
    #                           "userCode": 707827,
    #                           "orderId": orderid,
    #                           "productId": proid,
    #                           "lineId": lineid,
    #                           "tripDate": "2020-08-21",
    #                           "reserveCityId": 9980939,
    #                           "departureCityId": 9980939,
    #                           "backDate": "2020-08-22",
    #                           "reserveNum": 0,
    #                           "minPrice": minprice,
    #                           "memo": "",
    #                           "contactPersonId": "",
    #                           "planDetail": [
    #                               {
    #                                   "planName": "基础方案",
    #                                   "planId": 0,
    #                                   "remark": None,
    #                                   "signEndTime": "2020-08-21 00:00:00",
    #                                   "priceDetail": [
    #                                       {
    #                                           "price": 120,
    #                                           "priceCategoryId": 1092,
    #                                           "priceCategory": "单房差",
    #                                           "startingAge": None,
    #                                           "endAge": None,
    #                                           "heightDescription": None,
    #                                           "reserveNum": 1
    #                                       },
    #                                       {
    #                                           "price": 399,
    #                                           "priceCategoryId": 1093,
    #                                           "priceCategory": "成人",
    #                                           "startingAge": 18,
    #                                           "endAge": 60,
    #                                           "heightDescription": None,
    #                                           "reserveNum": "1"
    #                                       },
    #                                       {
    #                                           "price": 399,
    #                                           "priceCategoryId": 1094,
    #                                           "priceCategory": "青少年",
    #                                           "startingAge": 12,
    #                                           "endAge": 18,
    #                                           "heightDescription": None
    #                                       },
    #                                       {
    #                                           "price": 159,
    #                                           "priceCategoryId": 1095,
    #                                           "priceCategory": "儿童",
    #                                           "startingAge": 2,
    #                                           "endAge": 12,
    #                                           "heightDescription": "身高1.2米以下",
    #                                           "reserveNum": 0
    #                                       },
    #                                       {
    #                                           "price": 0,
    #                                           "priceCategoryId": 1096,
    #                                           "priceCategory": "婴儿",
    #                                           "startingAge": 0,
    #                                           "endAge": 2,
    #                                           "heightDescription": None
    #                                       },
    #                                       {
    #                                           "price": 399,
    #                                           "priceCategoryId": 1097,
    #                                           "priceCategory": "老人",
    #                                           "startingAge": 60,
    #                                           "endAge": 80,
    #                                           "heightDescription": None
    #                                       }
    #                                   ],
    #                                   "show": True
    #                               }
    #                           ],
    #                           "confirmAgain": 1,
    #                           "trallers": [],
    #                           "singleRoomPlan": "ADVANCE"
    #                       })
    #     assert r.json()['message'] == '成功'
    #
    #     # 取消订单
    #     r = requests.put('https://miniapptest.yujianmeihao.net/api/micro-service/order/pre/cancel/' + str(orderid),
    #                      headers=headers)
    #     print(r.json()['data']['validCode'])
    #     validcode = r.json()['data']['validCode']
    #     r = requests.put('https://miniapptest.yujianmeihao.net/api/micro-service/order/miniapp-cancel/',
    #                      headers=headers,
    #                      json={
    #                          'orderId': orderid,
    #                          'validCode': validcode,
    #                          'operateUid': 86
    #                      })
    #     assert r.json()['message'] == '成功'


