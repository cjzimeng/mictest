import pytest
import allure
import requests
import random
import datetime
import time
from test_case.test_basic_data import *


@allure.title("发布图片笔记")
@allure.story("发布图片笔记")
@pytest.mark.run(order=1)
def test_picnote():
    tmp = (datetime.datetime.now()).strftime('%Y-%m-%d-%H-%M-%S')

    # 发布笔记  微信：cc
    content = [
        '七月流火，九月授衣。一之日觱发，二之日栗烈。无衣无褐，何以卒岁。三之日于耜，四之日举趾。同我妇子，馌彼南亩，田畯至喜。七月流火，九月授衣。春日载阳，有鸣仓庚。女执懿筐，遵彼微行，爰求柔桑。春日迟迟，采蘩祁祁。女心伤悲，殆及公子同归。七月流火，八月萑苇。蚕月条桑，取彼斧斨，以伐远扬，猗彼女桑。七月鸣鵙，八月载绩。载玄载黄，我朱孔阳，为公子裳。四月秀葽，五月鸣蜩。八月其获，十月陨萚。一之日于貉，取彼狐狸，为公子裘。二之日其同，载缵武功，言私其豵，献豣于公。六月食郁及薁，七月亨葵及菽，八月剥枣，十月获稻，为此春酒，以介眉寿。七月食瓜，八月断壶，九月叔苴，采荼薪樗，食我农夫。九月筑场圃，十月纳禾稼。黍稷重穋，禾麻菽麦。嗟我农夫，我稼既同，上入执宫功。昼尔于茅，宵尔索綯。亟其乘屋，其始播百谷。二之日凿冰冲冲，三之日纳于凌阴。四之日其蚤，献羔祭韭。九月肃霜，十月涤场。朋酒斯飨，曰杀羔羊。跻彼公堂，称彼兕觥，万寿无疆。',
        '鸱鸮鸱鸮，既取我子，无毁我室。恩斯勤斯，鬻子之闵斯。迨天之未阴雨，彻彼桑土，绸缪牖户。今女下民，或敢侮予？予手拮据，予所捋荼。予所蓄租，予口卒瘏，曰予未有室家。予羽谯谯，予尾翛翛，予室翘翘。风雨所漂摇，予维音哓哓！',
        '既破我斧，又缺我斨。周公东征，四国是皇。哀我人斯，亦孔之将。既破我斧，又缺我锜。周公东征，四国是吪。哀我人斯，亦孔之嘉。既破我斧，又缺我銶。周公东征，四国是遒。哀我人斯，亦孔之休。',
        '伐柯如何？匪斧不克。取妻如何？匪媒不得。伐柯伐柯，其则不远。我觏之子，笾豆有践。',
        '狼跋其胡，载疐其尾。公孙硕肤，赤舄几几。狼疐其尾，载跋其胡。公孙硕肤，德音不瑕？',
        '呦呦鹿鸣，食野之苹。我有嘉宾，鼓瑟吹笙。吹笙鼓簧，承筐是将。人之好我，示我周行。呦呦鹿鸣，食野之蒿。我有嘉宾，德音孔昭。视民不恌，君子是则是效。我有旨酒，嘉宾式燕以敖。呦呦鹿鸣，食野之芩。我有嘉宾，鼓瑟鼓琴。鼓瑟鼓琴，和乐且湛。我有旨酒，以燕乐嘉宾之心。',
        '四牡騑騑，周道倭迟。岂不怀归？王事靡盬，我心伤悲。四牡騑騑，啴啴骆马。岂不怀归？王事靡盬，不遑启处。翩翩者鵻，载飞载下，集于苞栩。王事靡盬，不遑将父。翩翩者鵻，载飞载止，集于苞杞。王事靡盬，不遑将母。驾彼四骆，载骤骎骎。岂不怀归？是用作歌，将母来谂。',
        '皇皇者华，于彼原隰。駪駪征夫，每怀靡及。我马维驹，六辔如濡。载驰载驱，周爰咨诹。我马维骐，六辔如丝。载驰载驱，周爰咨谋。我马维骆，六辔沃若。载驰载驱，周爰咨度。我马维骃，六辔既均。载驰载驱，周爰咨询。',
        '常棣之华，鄂不韡韡。凡今之人，莫如兄弟。死丧之威，兄弟孔怀。原隰裒矣，兄弟求矣。脊令在原，兄弟急难。每有良朋，况也永叹。兄弟阋于墙，外御其务。每有良朋，烝也无戎。丧乱既平，既安且宁。虽有兄弟，不如友生。傧尔笾豆，饮酒之饫。兄弟既具，和乐且孺。妻子好合，如鼓瑟琴。兄弟既翕，和乐且湛。宜尔室家，乐尔妻帑。是究是图，亶其然乎？',
        '伐木丁丁，鸟鸣嘤嘤。出自幽谷，迁于乔木。嘤其鸣矣，求其友声。相彼鸟矣，犹求友声。矧伊人矣，不求友生？神之听之，终和且平。伐木许许，酾酒有藇！既有肥羜，以速诸父。宁适不来，微我弗顾。於粲洒扫，陈馈八簋。既有肥牡，以速诸舅。宁适不来，微我有咎。伐木于阪，酾酒有衍。笾豆有践，兄弟无远。民之失德，乾餱以愆。有酒湑我，无酒酤我。坎坎鼓我，蹲蹲舞我。迨我暇矣，饮此湑矣。'
        ]
    r = requests.post(test_host1 + '/community/note/publish',
                      headers=headers,
                      json={
                          "userId": userid,
                          "msUserCode": msUserCode,
                          "type": "IMAGE",
                          "title": tmp,
                          "content": tmp + "分享图片笔记故事：" + random.choice(content),
                          "position": "您在哪里？",
                          "longitude": "",
                          "latitude": "",
                          "noteVideo": {
                              "aliVideoId": "",
                              "videoCover": ""
                          },
                          "noteImgList": [{
                              "imgUrl": "https://meetyoutest.oss-cn-shenzhen.aliyuncs.com/fs/community/image/20201110/1604992445384.jpg",
                              "imgId": 2962
                          }]
                      })
    noteid = r.json()['data']['noteId']
    print('发布图片笔记id：',noteid)
    assert noteid

    # time.sleep(1)

@allure.title("点赞笔记")
@allure.story("点赞笔记")
@pytest.mark.run(order=2)
def test_support(test_get_note):
    noteid = test_get_note[0]

    #点赞笔记
    r11 = requests.post(test_host1+'/community/supports',
                        headers = headers1,
                        json={"parentId":noteid,"type":"NOTE","userId":userid})
    print('点赞笔记：',r11.json())
    result11 = r11.json()['data']
    assert result11
    # time.sleep(1)

@allure.title("取消笔记点赞")
@allure.story("取消笔记点赞")
@pytest.mark.run(order=3)
def test_cancel_support(test_get_note):
    noteid = test_get_note[0]
    #取消点赞
    r12 = requests.delete(test_host1+'/community/supports/' + noteid + '/NOTE/'+str(userid),
                          headers = headers1)
    print('取消点赞：',r12.json())
    result12 = r12.json()['message']
    assert result12 == '成功'
    # time.sleep(1)

@allure.title("收藏笔记")
@allure.story("收藏笔记")
@pytest.mark.run(order=4)
def test_collection(test_get_note):
    noteid = test_get_note[0]
    #收藏笔记
    r13 = requests.post(test_host1+'/community/collection/'+ noteid +'/'+str(userid),
                        headers = headers1)
    print('收藏笔记：',r13.json())
    result13 = r13.json()['data']
    assert result13
    # time.sleep(1)

@allure.title("取消笔记收藏")
@allure.story("取消笔记收藏")
@pytest.mark.run(order=5)
def test_cancel_collection(test_get_note):
    noteid = test_get_note[0]
    #取消收藏
    r14 = requests.delete(test_host1+'/community/collection/'+noteid+'/'+str(userid),
                          headers=headers1)
    print('取消收藏笔记：',r14.json())
    result14 = r14.json()['message']
    assert result14=='成功'

@allure.title("评论笔记、回复评论、删除回复")
@allure.story("评论笔记、回复评论、删除回复")
@pytest.mark.run(order=6)
def test_reply(test_get_note):
    noteid = test_get_note[0]
    #评论笔记
    rand = random.randint(200, 999)
    comment = 'aaa' + str(rand)
    reply = 'bbb' +str(rand)
    r15 = requests.post(test_host1+'/community/reply',
                        headers=headers1,
                        json={"parentId":noteid,"content":comment,"fromUserId":userid,"type":"COMMENT"})
    print('评论笔记：',r15.json())
    result15 = r15.json()['data']
    assert result15
    time.sleep(1)

    #回复评论
    r16 = requests.post(test_host1+'/community/reply',
                        headers=headers1,
                        json={"parentId":result15,"content":reply,"fromUserId":userid,"type":"REPLY_COMMENT"})
    print('回复评论：',r16.json())
    result16 = r16.json()['data']
    assert result16
    time.sleep(1)

    #删除回复
    r17 =requests.delete(test_host1+'/community/reply/' + result16,
                         headers=headers1)
    print('删除回复：',r17.json())
    result17 = r17.json()['message']
    assert result17 == '成功'

@allure.title("分享笔记")
@allure.story("分享笔记")
@pytest.mark.run(order=7)
def test_share(test_get_note):
    noteid = test_get_note[0]
    #分享笔记
    r18 = requests.post(test_host1+'/community/share',
                        headers=headers1,
                        json={"userId":userid,"type":"NOTE","rtId":noteid,"channel":"WECHAT"})
    print("分享笔记：",r18.json())
    result18 = r18.json()['data']
    assert result18

@allure.title("生成海报")
@allure.story("生成海报")
@pytest.mark.run(order=8)
def test_dynamic(test_get_note):
    noteid = test_get_note[0]
    #生成海报
    r19 = requests.post(test_mic+'/micro-service/app/dynamic',
                        headers=headers1,
                        json={"page":"pages/note/noteDetails","scene":noteid})
    print('生成海报：',r19.json())
    result19 = r19.json()['data']
    assert result19
    # time.sleep(1)

@allure.title("删除笔记")
@allure.story("删除笔记")
@pytest.mark.run(order=9)
def test_delete(test_get_note):
    noteid = test_get_note[0]
    # 删除笔记
    r1 = requests.delete(test_host1 + '/community/note/' + noteid + '-'+ str(userid),
                         headers=headers1)
    print('删除笔记',r1.json())
    result = r1.json()['data']
    assert result


@allure.title("发布视频笔记")
@allure.story("发布视频笔记")
def test_videonote():
    tmp = (datetime.datetime.now()).strftime('%Y-%m-%d-%H-%M-%S')
    r = requests.post(test_host1+'/community/note/publish',
                      headers=headers1,
                      json={
                          "userId": userid,
                          "msUserCode": msUserCode,
                          "type": "VIDEO",
                          "title": tmp,
                          "content": "视频内容1"+tmp,
                          "position": "",
                          "longitude": "",
                          "latitude": "",
                          "noteVideo": {
                              "aliVideoId": "f260850cfffc48369c06a4415fcdf68a",
                              "videoCover": ""
                          },
                          "noteImgList": []
                      })
    print("发布视频笔记：",r.json())
    result = r.json()['data']['noteId']
    assert result

    r1 = requests.get(test_host1+'/community/note/detail/'+result+'-'+str(userid),
                      headers=headers1)
    videoid1 = r1.json()['data']['id']
    print("登录后查看视频笔记详情，笔记id：",videoid1)
    assert result == videoid1

    r2 = requests.get(test_host1+'/community/note/detail/'+result+'-0',
                      headers=headers1)
    videoid2 = r2.json()['data']['id']
    print("未登录查看视频笔记详情，笔记id：",videoid2)
    assert result == videoid2
