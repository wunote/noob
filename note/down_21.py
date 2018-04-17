#coding:utf-8

import os
import re 
import urllib
import shutil

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

#url=raw_input("please input the source url:")
url='http://www.gamersky.com/handbook/201612/845807.shtml'
nums=1
while True:
    html=getHtml(url)
    
    re_jpg=re.compile(r'\?(http://img.*?\.jpg)"><img')
    jpgList=re.findall(re_jpg,html)
    dirs = os.path.abspath('.')+'/'+'tu/'

    for jpgurl in jpgList:
        print jpgurl
        urllib.urlretrieve(jpgurl,dirs+"%s.jpg" %nums)
        print  'file "%s.jpg" done' %nums
        nums+=1


    tmp = re.compile(r'href="(.*?)">下一页')
    pages = re.findall(tmp,html)
    if not len(page):
        print 'Get pic complete!'
        break
    url=pages[0]

