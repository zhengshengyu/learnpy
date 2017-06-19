#!/usr/bin/env python
# -*- coding: utf-8 -*-

#使用字符串
## 基本的序列操作：索引 切片 乘法 in len max min等
## 格式化 %  Template
print "hello, %s! bye, %s？" % ("python", "Lua")
# print "hello, %s! bye, %s？" % "python", "Lua" #Error
from math import pi
print "Pi with three decimal: %.3f" % pi

from string import Template
s = Template('$x ++++ ${x}some!')
print s.substitute(x='hand')
