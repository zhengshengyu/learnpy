#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
## 2.x: 字符串用'xxx'表示str，Unicode字符串用u'xxx'表示unicode; 3.x: 所有字符串都被视为unicode
from __future__ import division
## 2.x: / 是地板除法，要做精确除法，必须把其中一个数变成浮点数; 3.x: 所有的除法都是精确除法，地板除用//表示

' a test module '
__author__ = 'zhengshengyu'
# 一个.py文件就称之为一个模块（Module）。
# 如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。

import os
import sys
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

def test():
    args = sys.argv # 运行python module.py Michael获得的sys.argv就是['module.py', 'Michael]。
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':
    test()

# 函数、变量 作用域
## 命名习惯
## 私有：仅在模块内部使用，类似_xxx
## 公有：只有外部需要引用的函数才定义为public，类似xxx
## 特殊：类似__xxx__

# 模块搜索路径: 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块
print sys.path

# 使用__future__
print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)
print 10 // 3, 10 / 3
