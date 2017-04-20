#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 集合模块collections
## namedtuple('名称', [属性list]), 微型的class
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print p, p.x, p.y

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(0,0,1)
print c, c.x, c.y, c.r

## deque 实现插入和删除操作的双向列表
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q
q.pop()
q.popleft()
print q

## defaultdict key不存在时，返回一个默认值
## dict 如果引用的Key不存在，就会抛出KeyError
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'a'
print dd['key1'], dd['key2']

## OrderedDict 保持Key的顺序（按照插入的顺序排列）
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('c', 2), ('b', 3)])
print d, od
### 实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)

luod = LastUpdatedOrderedDict(3)
luod['out'] = 0
luod['x'] = 11
luod['y'] = 22
luod['z'] = 33
print luod

## 一个简单的计数器Counter: 实际上是dict的一个子类
from collections import Counter
c = Counter()
for ch in 'hello python':
	c[ch] += 1
print c


# Base64 一种最常见的二进制编码方法: 常用于在URL、Cookie、网页中传输少量二进制数据
# 内置的base64可以直接进行base64的编解码
import base64
print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')
