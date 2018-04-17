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
url='http://www.3dmgame.com/zt/201801/3713941.html'
nums=1
while True:
    html=getHtml(url)
    
    re_jpg=re.compile(r'src="(http://img\..*?\.jpg)|(http://img\..*?\.gif)"')
    jpgList=re.findall(re_jpg,html)
    dirs = os.path.abspath('.')+'/'+'tu/'

    for jpgurl in jpgList:
        print jpgurl
        
        jpg = jpgurl[0]+jpgurl[1]
        if 'gif' in jpg:
            urllib.urlretrieve(jpg,dirs+"%s.gif" %nums)
            print  'file "%s.gif" done' %nums
            nums+=1
        elif 'jpg' in jpgurl:
            urllib.urlretrieve(jpg,dirs+"%s.jpg" %nums)
            print  'file "%s.jpg" done' %nums
            nums+=1


    tmp = re.compile(r"href='(.*?)'>下页")
    pages = re.findall(tmp,html)
    page = list(set(pages))
    if not len(page):
        break
    else:
        print page[0]    
    url='http://www.3dmgame.com/zt/201801/' + page[0]

