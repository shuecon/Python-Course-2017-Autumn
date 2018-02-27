import requests
import pandas as pd 
from dateutil.parser import parse


#在Facebook Graph API Exploer取得token

token = 'EAACEdEose0cBALZC6iCNOAiDTjb1ZBWS0RqOstNO7KeZBC2GVZBs6I0kSUSp47osRZAYPSbvZCuo8pEvJ9S6XaRYapyni94g1zIwZBq0Omba4TSxurfNhum7Wv2RR1EGLXJUQsmqI2hNuFFXTsZAxtiPPX0JZA1SoLJS0dx9BW0swvJU74r90PZBTSOkePoTQ6B1e4nH5Yx3oieAZDZD' 


#在Facebook Graph API Exploer取得粉絲專頁的id與名稱，並將其包成字典dic

fanpage = {'145649977189':'7-ELEVEN',
           '111515882197852':'食尚玩家'} 


#建立一個空的list          

information_list = []


#使用for迴圈依序讀取粉絲頁的資訊，並使用format將id與token傳入{}裡

for ele in fanpage:
    res = requests.get('https://graph.facebook.com/v2.9/{}/posts?limit=100&access_token={}'.format(ele, token))
    
    
    #API最多一次呼叫100筆資料，因此使用while迴圈去翻頁取得所有的資料

    while 'paging' in res.json(): 
        for information in res.json()['data']:
            if 'message' in information:
                information_list.append([fanpage[ele], information['message'], parse(information['created_time']).date()])

        if 'next' in res.json()['paging']:
            res = requests.get(res.json()['paging']['next'])
        else:
            break


#最後將list轉換成dataframe，並輸出成csv檔

information_df = pd.DataFrame(information_list, columns=['粉絲專頁', '發文內容', '發文時間']) 
information_df.to_csv('20180103.csv', index=False) 