import allure
from test_case.test_basic_data import *
import requests

@allure.title('小程序首页')
@allure.story('小程序首页')
def test_home():
    r = requests.get(test_host+'/micro-service/homepage/detail',
                     headers = headers,
                     params = {'cityName':'长沙'})
    result = r.json()['data']
    #首页banner
    assert len(result['homePageBanner'])>0
    #banner下icon
    assert len(result['homePageIconType'])==4
    #首页类别
    assert len(result['homePageMianType'])==8
    #热门推荐产品
    assert len(result['homePageProductDtos'])>0
    #目的地icon
    assert len(result['homePageTravelType'])==4
    assert len(result['homePageDestinationTypes'])==4
    #遇见甄选产品
    assert len(result['homePageSelectionProduct'])>0

@allure.title('个人中心')
@allure.story('个人中心')
def test_user_center():
    r = requests.get(test_host+'/micro-service/order/list/count/707827',
                     headers=headers)
    result = r.json()['data']['total']
    assert result