
from test_case.test_basic_data import *
import requests
import random
import datetime

# r = requests.post(test_host1+'/micro-service/note/recommend/concern',
#                   headers = headers1,
#                   json={"pageSize":10,"pageNum":1,"userId":None})
# recommend_user = r.json()['data']['list']
# print(r.json()['data']['list'])
# noteid = '5fc5e794f9eeca15e33b0dfe'
#
# r1 = requests.delete(test_host1+'/community/note/'+noteid+'-114',
#                          headers=headers1)
# print(r1.json())
# print(datetime.datetime.now().strftime("%Y-%m-%d"))

r = requests.post(test_host1+'/community/query-user-data',
                      headers=headers1,
                      json={
                          "userId": userid,
                          "notePageNum": 1,
                          "notePageSize": 6,
                          "collectionPageNum": 1,
                          "collectionPageSize": 6,
                          "loginUserId": userid
                      })
note_list = r.json()['data']['note']['list']
print(len(note_list))
noteid = []
for i in note_list:
    noteid.append(i['id'])
print(noteid)