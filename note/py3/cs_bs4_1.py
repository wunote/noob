import urllib.request
from bs4 import BeautifulSoup 

html = urllib.request.urlopen("http://www.pythonscraping.com/pages/warandpeace.html") 
bsObj = BeautifulSoup(html,'html.parser')

nameList = bsObj.findAll(class_="green")

for name in nameList:      
    print(name.get_text())
