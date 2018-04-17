from urllib.request import urlopen 
from bs4 import BeautifulSoup 
import re 
 
note = open('3dm.txt','w')
pages = set() 
def getLinks(pageUrl):     
    global pages     
    html = urlopen(pageUrl)    
    bsObj = BeautifulSoup(html,'html.parser')     
    
    links = bsObj.findAll("a",href=re.compile(r"(.*?)"))
    #print(links)
    #read = input('Enter to continue')
    for link in links:       
        if 'href' in link.attrs:             
            if link.attrs['href'] not in pages:                 # 我们遇到了新页面                 
                newPage = link.attrs['href']                 
                print(newPage,file=note)                 
                pages.add(newPage)                 
                getLinks(newPage) 
 
getLinks("http://www.3dmgame.com/")
note.close()
