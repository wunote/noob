#coding:utf-8

from bs4 import BeautifulSoup
import urllib.request
from collections import deque,defaultdict
import re
import os


url='http://www.22mm.cc/'

def get_page(url):
    headers = {
    'Connection': 'Keep-Alive',
    'Accept': "image/png,image/*;q=0.8,*/*;q=0.5",
    'Accept-Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    'Referer':"http://www.22mm.cc/"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    responseutf8 = response.read().decode()
    responsegbk = responseutf8.encode('gbk', 'ignore')
    page = responsegbk.decode('gbk')
    return page

def get_first_link(page):
    queue=deque()
    filename=[]
    baseurl='http://22mm.xiuna.com'
    soup=BeautifulSoup(page)
    pic=soup.find(id = 'recshowBox')
    for child in pic.children:
         queue.append(baseurl+child['href'])
         filename.append(child['title'])
    return filename,queue

def get_all_links(filename, queue):
    d=defaultdict(set)
    n=0
    while queue:
        link2=[]
        linkss=link2[:]
        links=link2[:]
        link1=link2[:]
        baselink=queue.popleft()
        pagecode=get_page(baselink)
        soup=BeautifulSoup(pagecode)
        link=soup.find(class_="pagelist")
        for child in link.children:
            try:
                linkss.append(child['href'])
            except:
                continue
        links=linkss[1:-1]
        pattern=re.compile('http.*/')
        addurl=re.findall(pattern,baselink)
        link1=[addurl[0]+link for link in links]
        '''for link in links:
            link1.append(addurl[0]+link)
            link1.append(baselink)'''
        for value in link1:
            d[filename[n]].add(value)
        n+=1
    return d

def download_all_pic(d):
    for key in d:
        print("正在创建{}的目录".format(key))
        path='/opt/pics/'+key+'/'
        os.mkdir('%s'%path)
        print(path)
        print("开始下载{}的图集...".format(key))
        index=1
        for i in d[key]:
            #global index
            page1=get_page(i)
            pattern1=re.compile(r'arrayImg\[0\]=\"(http.*?jpg)')
            addurl1=re.findall(pattern1,page1)
            down=addurl1[-1].replace('big','pic')
            print("正在下载%s的第%d张图片" % (key,index))
            urllib.request.urlretrieve(down,'/opt/pics/%s/%d.jpg' % (key,index))
            print("下载完成")
            index+=1

def start(url):
    page=get_page(url)
    filename, queue=get_first_link(page)
    d=get_all_links(filename,queue)
    download_all_pic(d)

start(url)

