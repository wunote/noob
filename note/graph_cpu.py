#!/usr/bin/env python                                                                                                                                   
#coding:utf8  
  
import rrdtool  
import time  
import os  
  
file_path =  os.path.split(os.path.realpath(__file__))[0] #该方法可以获取该运行文件所在的目录  
#local_path = os.path.abspath(".")  
#print local_path  
#data_path = os.path.abspath("MEMORY.rrd") #获取数据文件的绝对路径  
data_path = file_path + "/CPU.rrd"  
  
title = "CPU STATE ("+time.strftime('%Y-%m-%d',  
time.localtime(time.time()))+")"  
rrdtool.graph(file_path + "/CPU.png", "--start", "-1h", "--vertical-label=%", 
    "--x-grid", "MINUTE:5:MINUTE:1:MINUTE:5:0:%M",   
    "--width", "650", "--height", "230", "--title", title,  
    "DEF:used=%s:cpu_percent:AVERAGE" % data_path,    #指定CPU使用情况  
    "AREA:used#FFF000:Cpu Used", #以面积的方式绘制内存使用量  
    "HRULE:50#FF0000:Alarm value\\r", #绘制水平线，作为警告线  
    "COMMENT:\\r",  
    "COMMENT:\\r", #在网格下方输入一个换行符  
    "GPRINT:used:AVERAGE:Used in Cpu\:%6.2lf %S%%",  
)
