#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 文件和流
## 打开文件
import pprint
f = open(r'zsyread.txt', 'r+') # r w a b +
print f.read(3)
print f.read()
f.close()

f = open(r'zsywrite.txt', 'r+')
f.write('0000\n')
print f.tell()
f.seek(5,0) #0从文件头计算偏移量1(>=0)
# print f.tell()
f.write('start ')
f.seek(0,1) #1从文件当前位置计算偏移量-3 0 3
# print f.tell()
f.write('current ')
f.seek(0,2) #2从文件尾计算偏移量(<=0)
# print f.tell()
f.write('end\n')
f.close()
print '---------end---------'

try:
	f = open(r'zsyread.txt', 'r+')
	print f.readline()
	print f.readline(3)
	pprint.pprint(f.readlines())
finally:
	f.close()
# 精简版try finally(close())
with open(r'zsyread.txt', 'r+') as f:
	print f.readline()
	print f.readline(3)
	pprint.pprint(f.readlines())

def process(string):
	print 'processing:', string

with open(r'zsyread.txt', 'r+') as f:
	while True:
		line = f.readline()
		if not line:
			break
		process(line)
# while -> for
import fileinput
for line in fileinput.input('zsyread.txt'):
	process(str(fileinput.filelineno()) + ':' + line)

# 一次读取文件内容：然而在处理大数据文件时候，这个是不可取的，太大的内存会被占用
with open(r'zsyread.txt', 'r+') as f:
	for char in f.read():
		process(char)
with open(r'zsyread.txt', 'r+') as f:
	for line in f.readlines():
		process(line)

# 直接迭代文件
print '@@@@@@@@@@@@@@@@@@surprize'
for line in open(r'zsyread.txt', 'r+'):
	process(line)
for line in list(open(r'zsyread.txt', 'r+')):
	process(line)