#!/usr/bin/python
import os

for root,dirs,files in os.walk('/opt/admin'):
    for name in files:
        print (os.path.join(root,name))
