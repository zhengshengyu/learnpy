#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 基本语句：print import 赋值 条件(if elif else) 循环 断言 and or not is(一致性判断) in(成员判断)

# 迭代工具 zip enumerate reversed sorted
## 并行迭代
names = ['zzz', 'xxx', 'yyy']
ages = [1,2,3]
for i in xrange(len(names)):
    print names[i] + 'is' + str(ages[i])
for name,age in zip(names, xrange(10,1,-1)):
    print name, 'is', age
## 按索引迭代序列 
for index, name in enumerate(names):
    print index, name
## 反转 
for name in list(reversed(names)):
    print name
## 排序 
for name in sorted(names):
    print name

# 列表推到式
print [x*y for x in range(0,5) for y in range(5,10) if y%2 == 0]

# 三人行 pass, del, exec python语句, eval python表达式