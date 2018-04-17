#coding:utf-8

files = file('wu.txt','r+')
s=files.read()
files.seek(0,0)
files.write(s.replace('one','two'))

files.close()
