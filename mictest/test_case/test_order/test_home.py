import allure
from test_case.test_basic_data import *
import requests

@allure.title('小程序首页')
@allure.story('小程序首页')
def test_home():
    r = requests.get(test_mic+'/micro-service/homepage',
                     headers = headers,
                     params = {'cityName':'长沙',"userId":userid})
    result = r.json()['data']['list']
    #首页banner
    # assert len(result['homePageBanner'])>0
    assert (result[0])['componentGroupType'] == 'BANNER'
    #banner下icon
    # assert len(result['homePageIconType'])==4
    assert (result[1])['componentGroupType'] =='ICON'

@allure.title('个人中心')
@allure.story('个人中心')
def test_user_center():
    r = requests.get(test_mic+'/micro-service/order/list/count/'+str(msUserCode),
                     headers=headers)
    result = r.json()['data']['total']
    print("个人中心：",r.json())
    assert result