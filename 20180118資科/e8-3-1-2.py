#e8-3-1-2抓取台銀匯率資訊
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from time import localtime, strftime, strptime, mktime
from datetime import datetime
from os.path import exists
import matplotlib.pyplot as plt
html = urlopen("http://rate.bot.com.tw/xrt?Lang=zh-TW")
bsObj = BeautifulSoup(html, "lxml")
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0]
    currency_name = currency_name.replace("\r","")
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate1 = cell[1].contents[0]
    currency_rate2 = cell[2].contents[0]
    currency_rate3 = cell[3].contents[0]
    currency_rate4 = cell[4].contents[0]
    print(currency_name, currency_rate1, currency_rate2, currency_rate3, currency_rate4)
    file_name = "e8-3-1-2" + currency_name + ".csv"
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    if not exists(file_name):
        data = [['時間', '現金買入', '現金賣出', '即期買入', '即期賣出'], [now_time, currency_rate1, currency_rate2, currency_rate3, currency_rate4]]
    else:
        data = [[now_time, currency_rate1, currency_rate2, currency_rate3, currency_rate4]]
    f = open(file_name, "a")
    w = csv.writer(f)
    w.writerows(data)
    f.close()
