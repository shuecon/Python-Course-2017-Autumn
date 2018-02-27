#e5-4-1-2自然語言處理
#載入jieba與jieba.analyse。
import jieba
import jieba.analyse

# 把檔案的內容讀出來，請將文章存在目錄的article.txt中
f = open('article1216-1.txt','r',encoding = 'utf8')
article = f.read()
seglist = jieba.cut(article, cut_all=False)
# 透過jieba內建的idf頻率庫, 我們可以計算文章中最重要的字詞
#tags = jieba.analyse.extract_tags(article, 10)
#print("最重要字詞", tags)
import json
hash = {}
for item in seglist: 
    if item in hash:
      hash[item] += 1
    else:
      hash[item] = 1
#json.dump(hash,open("count.json","w"))
#fd = open("count.csv","w")
#fd.write("word,count\n")

for k in hash:
#  fd.write("%s,%d\n"%(k.encode("utf8"),hash[k]))
  if len(k)>1 and hash[k]>5:
        print(k,hash[k])