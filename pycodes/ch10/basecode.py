#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 自带电池

## 模块
import math
print math.sin(math.pi/2)

### 创建包、模块
import sys, pprint
sys.path.append('D:\git_repository\learnpy\pycodes')
import site_packages # 导入包 site_packages文件夹下创建__init__.py
import site_packages.hellopy # 导入包里的模块
print  site_packages.hellopy.test()
from site_packages import hellopy # 导入包里的模块
print hellopy.hello()

sys.path.append('D:\git_repository\learnpy\pycodes\site_packages')
pprint.pprint(sys.path)
import hellopy # 直接导入模块
print  hellopy.test()

### 探究模块
import copy
copydir = dir(copy)
pprint.pprint(copydir)
print [d for d in copydir if not d.startswith('_')]
print copy.__all__
from copy import PyStringMap, dispatch_table, error
print copy.__all__
help(copy.copy)
print copy.copy.__doc__
print copy.__file__ #查看copy模块源代码路径

### 一些典型标准库
#### sys
sysdir = dir(sys)
print [d for d in sysdir if not d.startswith('_')]
##### sys.argv: 命令行调用脚本时会在后面接上一些参数，sys.argv[0]为脚本名，参数从1开始

#### os
import os
print '@@@@@@@@@@@@@',os.environ['CLASSPATH']
# os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') #打开谷歌浏览器

import webbrowser
# webbrowser.open('http://baidu.com') #打开固定网址

#### fileinput

#### set集合
print set([1,2,3,4,3,2,1,0])
a=set([1,2,3,4])
b=set([2,4,6,8])
print a&b, a|b, a^b, a-b #交 并 异或 差

mySets =[]
for i in xrange(1,10):
	subSet=set(range(i+5))
	# print subSet
	mySets.append(subSet)
# print mySets
print reduce(set.union, mySets)

#### heap堆
from heapq import *
from random import shuffle
data = range(10)
shuffle(data)
heap=[]
for n in data:
	heappush(heap,n)
heapify(heap)
print heap
print range(1,11)
for x in xrange(1,10):
	print heappop(heap)

#### deque
from collections import deque
q=deque(range(5))
q.append(5)
q.appendleft(-1)
print q
print q.pop(), q.popleft()
q.rotate(1)
print q

#### time
import time
print time.asctime(), time.asctime((2017,6,20,23,3,0,1,171,0))
print time.localtime(time.time()), time.gmtime(time.time())
print time.mktime(time.localtime(time.time()))
print time.strptime(time.asctime())
# print time.time()
# time.sleep(3)
# print time.time()

#### shelve
import shelve
s=shelve.open('test.dat')
s['zsy'] = ['z','s','y']
temp = s['zsy']
temp.append('whf')
s['zsy']=temp
print s['zsy']

#### re
import re
pattern = re.compile('[p-y]+')
print re.match(pattern, 'python'), re.match(pattern, 'hello, python')
print re.findall(pattern, 'hello, python, ppp')