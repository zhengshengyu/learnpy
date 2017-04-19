#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IO编程
## 同步IO: CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行
## 异步IO: CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行 (略)

# 内置函数open()
## 读文件: read() read(size) readlines()
_fileReadPath = 'test.py'
### 繁琐写法
try:
    f = open(_fileReadPath, 'r')
    print f.read()
except IOError:
	print 'No such file or directory:%s' % _fileReadPath
finally:
    if f:
        f.close()
### 精简写法
with open(_fileReadPath, 'rb') as f: #with语句来会帮我们调用close()方法
    # print f.read()
	for line in f.readlines():
	    print line.strip() # 把末尾的'\n'删掉

## 写文件：写完一定要调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘
_fileWritePath = 'writefile.txt'
with open(_fileWritePath, 'w') as f:
    f.write('Hello, world!')


# 操作文件和目录
import os
print os.name #os.uname()  ##uname()函数在Windows上不提供
# print os.environ, os.getenv('PATH')

_curfold = os.path.abspath('.') #打印当前工作目录
# 路径合成，不要直接拼字符串，而要通过os.path.join()函数
# 拆分路径，也不要直接去拆字符串，而要通过os.path.split()函数
_newfold = os.path.join(_curfold, 'testfold1')
print os.path.split(_newfold)
print os.path.splitext(_newfold)

if os.path.isdir(_newfold):
	os.rmdir(_newfold)
else:
	os.mkdir(_newfold)

if os.path.isfile('writefile.py'):
	os.remove('writefile.py')
else:
	os.rename('writefile.txt', 'writefile.py')

# 列出当前目录下所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]
# 列出当前目录下所有的.py文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']


# 当前目录以及当前目录的所有子目录下查找文件名包含指定字符串substr的文件，并打印出完整路径
def search(substr):
	pass
