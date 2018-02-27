import requests
import pandas as pd 
from dateutil.parser import parse


#在Facebook Graph API Exploer取得token以及粉絲專頁的ID


token = 'EAACEdEose0cBAAxT9yOUjnisfF7T4l0i3mTvQ2E6B05YdjnIU1ZCQRD1wj5NHjpBcOCMB9c8F9wzUEyFqQ80WWiSF0AMnrqSLDTUzb8MDFAKSQbJULNngELK9Q6cT0t0eicxyAIH3AMI0cSmcJ42V9CtWDZB3sQmUpAfZCp8f1GeH6cQd5sSuvtHp3PYLrJPODmBk64CAZDZD' 
fanpage_id = '111515882197852'

#建立一個空的list          


information_list = []


#目標頁面


res = requests.get('https://graph.facebook.com/v2.8/{}/posts?limit=100&access_token={}'.format(fanpage_id, token))
page = 1  


#API最多一次呼叫100筆資料，因此使用while迴圈去翻頁取得所有的文章


while 'paging' in res.json(): 
    for index, information in enumerate(res.json()['data']):
        print('正在爬取第{}頁，第{}篇文章'.format(page, index + 1))
        
        
        #判斷是否為發文，是則開始蒐集按讚ID


        if 'message' in information:
            res_post = requests.get('https://graph.facebook.com/v2.9/{}/likes?limit=1000&access_token={}'.format(information['id'], token))
            
            
            #判斷按讚人數是否超過1000人，若超過則需要翻頁擷取；當沒有人按讚時，按讚人名與ID皆為NO

            try:
                if 'next' not in res_post.json()['paging']:
                    for likes in res_post.json()['data']:
                        information_list.append([information['id'], information['message'], parse(information['created_time']).date(), likes['id'], likes['name']])                
                elif 'next' in res_post.json()['paging']:
                    while 'paging' in res_post.json():
                        for likes in res_post.json()['data']:
                            information_list.append([information['id'], information['message'], parse(information['created_time']).date(), likes['id'], likes['name']])
                        if 'next' in res_post.json()['paging']:
                            res_post = requests.get(res_post.json()['paging']['next'])
                        else:
                            break
            except:
                information_list.append([information['id'], information['message'], parse(information['created_time']).date(), "NO", "NO"])

    if 'next' in res.json()['paging']:                
        res = requests.get(res.json()['paging']['next'])
        page += 1
    else:
        break
        
print('爬取結束!')
import pandas as pd
df = pd.DataFrame(information_list, columns=['發文ID', '發文內容', '發文時間', '按讚ID', '按讚名字'])
df.to_csv('7-11.csv', index=False)