#coding:utf-8

import urllib.request
from bs4 import BeautifulSoup
import re
import os

Base = "https://www.autohome.com.cn"

def get_page(url):
    req = urllib.request.urlopen(url)
    page = req.read().decode('GBK')
    return page


choose = ['慰领','朗逸','速腾','凌渡']
n = 0
f = open('list','r')
f1 = open("log.txt", "a+")
for flg in f.readlines():
    html = get_page(flg)
    print(choose[n],file=f1)
    n += 1
    print('=============================================',file=f1)
    carlist = re.findall(r'<a href="(/spec/(\w+)/#pvareaid=\w+)">(.*?)</a>',html)
    for Link,Id,name in carlist:
        url = "https://dealer.api.autohome.com.cn/dealerrest/price/GetMinPriceBySpecSimple?specids="+str(Id)+"&_appId=cms&cityid=510100&_callback=DealerBySpec" 
        count = str(urllib.request.urlopen(url).read())
        price = re.findall(r'"MinPrice":(\w+)',count)
        print(name,"\t",int(price[0])/10000,"万元起",file=f1)

print('=============================================')        
f.close()
f1.close()

