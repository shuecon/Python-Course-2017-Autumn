#e8-1-5抓取粉絲專頁資訊-貼文/讚數/分享數
import requests
import pandas as pd 
from dateutil.parser import parse
token = 'EAACEdEose0cBAHEuVZAL6YxzdlTRSZAG89WjmDrZAPGJwRZA3jHvEEbhmE3r0rMZBG6PWaUzcU0eYmuxxwPyF5arHZBFjQkKODDfRcVhHXM6vFj1ZAKcZBMeeE1hOeVN1VGKGuo4igxTu42yfKvzsEstxmazv0O47DOsiFVhCCSnHYg7FchgHI114A8YHXscWpXIlppnemhHmQZDZD'
fanpage_id = '46251501064'
res = requests.get('https://graph.facebook.com/v2.9/{}/posts?limit=100&access_token={}'.format(fanpage_id, token))
posts = []
page = 1
while 'paging' in res.json():
    print('目前正在抓取第%d頁' % page)
    for post in res.json()['data']:
        res2 = requests.get('https://graph.facebook.com/v2.8/{}?fields=likes.limit(0).summary(True), shares&access_token={}'.format(post['id'], token))
        if 'likes' in res2.json():
            likes = res2.json()['likes']['summary'].get('total_count')
        else:
            likes = 0
        if 'shares' in res2.json():
            shares = res2.json()['shares'].get('count')
        else:
            shares = 0
        posts.append([parse(post['created_time']),  post['id'], post.get('message'), post.get('story'), likes, shares])
    if 'next' in res.json()['paging']:
        res = requests.get(res.json()['paging']['next'])
        page += 1
    else:
        break
print('抓取結束!')
df = pd.DataFrame(posts)
df.columns = ['貼文時間', '貼文ID', '貼文內容', '分享內容', '讚數', '分享數']
df.to_csv('20180119-2