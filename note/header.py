#coding:utf-8

import re
import os
import urllib2

ua = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3373.400 QQBrowser/9.6.11998.400',
      'Connection':'Keep-Alive',
      'Accept-Language':'zh-CN,zh;q=0.8',
      #'Accept-Encoding':'gzip, deflate, sdch, br',   #gzip, deflate 返回数据会gzip压缩
      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Cache-Control':'max-age=0',
      'Content-Type':'Content-Type:text/html; charset=UTF-8'
      }

def get_html(url_address):
    req_http = urllib2.Request(url_address, headers = ua)
    html = urllib2.urlopen(req_http).read()
    return html

def get_pic(html):
    nums=100
    re_jpg=re.compile(r'src="(http://.*\.jpg)"')
    jpgList=re.findall(re_jpg,html)
    print jpgList
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

url = 'http://jandan.net/ooxx'
html = get_html(url)

with open('code.html','w+') as files:
    print >> files,html

print "Get html code success"
get_pic(html)
