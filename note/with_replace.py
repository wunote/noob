#coding:utf-8

with open('wu.txt', 'r+') as files:
    s=files.read()
    files.seek(0,0)
    files.write(s.replace('one','two'))

