import allure
import requests
import datetime
from test_case.test_basic_data import *

@allure.title("保存草稿")
@allure.story("保存草稿")
def test_save_draft():
    tmp = (datetime.datetime.now()).strftime('%Y-%m-%d-%H-%M-%S')
    r = requests.post(test_host1+'/community/note/draft',
                      headers=headers1,
                      json={
                          "userId": userid,
                          "msUserCode": msUserCode,
                          "type": "IMAGE",
                          "title": tmp,
                          "content": "草稿内容"+tmp,
                          "position": "",
                          "longitude": "",
                          "latitude": "",
                          "noteVideo": {
                              "aliVideoId": "",
                              "videoCover": ""
                          },
                          "noteImgList": [
                              {"imgUrl": "https://meetyoutest.oss-cn-shenzhen.aliyuncs.com/fs/community/image/20201201/1606812658381.png"}]
                      })
    print("保存草稿：",r.json())
    result = r.json()['data']
    assert result

@allure.title("查看草稿列表")
@allure.story("查看草稿列表")
def test_draft_list():
    r = requests.get(test_host1+'/community/note/me/draft?pageSize=12&pageNum=1&userId='+str(userid),
                     headers=headers1)
    result = r.json()['data']['total']
    print("草稿列表笔记数：",result)
    assert result > 0