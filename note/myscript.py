#!/usr/bin/python
#coding=utf-8
#

import os
filename = os.environ.get('wu.txt')
if filename and os.path.isfile(filename):
    execfile(filename)
