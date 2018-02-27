#e8-1-4抓取粉絲專頁資訊
import requests
import pandas as pd 
from dateutil.parser import parse

token = 'EAACEdEose0cBALZC6iCNOAiDTjb1ZBWS0RqOstNO7KeZBC2GVZBs6I0kSUSp47osRZAYPSbvZCuo8pEvJ9S6XaRYapyni94g1zIwZBq0Omba4TSxurfNhum7Wv2RR1EGLXJUQsmqI2hNuFFXTsZAxtiPPX0JZA1SoLJS0dx9BW0swvJU74r90PZBTSOkePoTQ6B1e4nH5Yx3oieAZDZD' 
fanpage = {'145649977189':'7-ELEVEN',
           '111515882197852':'食尚玩家'} 
information_list = []
for ele in fanpage:
    res = requests.get('https://graph.facebook.com/v2.9/{}/posts?limit=100&access_token={}'.format(ele, token))
    while 'paging' in res.json(): 
        for information in res.json()['data']:
            if 'message' in information:
                information_list.append([fanpage[ele], information['message'], parse(information['created_time']).date()])

        if 'next' in res.json()['paging']:
            res = requests.get(res.json()['paging']['next'])
        else:
            break
information_df = pd.DataFrame(information_list, columns=['粉絲專頁', '發文內容', '發文時間']) 
information_df.to_csv('e8-1-4.csv', index=False) 