#!/usr/bin/python
#
import os
import re 
import urllib
import shutil

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
def getjpg(html):
    r=r'src="(.*\.jpg)"'
    re_jpg=re.compile(r)
    jpgList=re.findall(re_jpg,html)

    dirs = os.path.abspath('.')+'/'+'tu/'
    if os.path.exists(dirs):
        shutil.rmtree(dirs)
    os.mkdir(dirs)

    filename=1
    for jpgurl in jpgList:
        urllib.urlretrieve(url+jpgurl,dirs+"%s.jpg" %filename)
        print  'file "%s.jpg" done' %filename
        filename+=1

url='http://www.77mei.com/'
html=getHtml(url)
getjpg(html)
