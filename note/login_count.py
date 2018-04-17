#coding=utf-8
import re,time

def deal(file_path):
    global count
    log=open(file_path,'r')
    C=r'\.'.join([r'\d{1,3}']*4)
    find=re.compile(C)
    count={}
    for i in log:
	for ip in find.findall(i):
	    count[ip]=count.get(ip,1)+1

if __name__=='__main__':
    print time.clock()
    num=0
    deal(r'/var/log/secure')
    R=count.items()
    for i in R:
	if i[1]>0:
	    print i
	    num+=1
    print '%s ip count %s' %(num,time.clock())


