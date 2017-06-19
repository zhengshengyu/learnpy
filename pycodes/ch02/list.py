#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 数据结构
## 基本数据结构之序列sequence(数组，序列索引从0开始，-1表示最后一个位置)：列表 元组 字符串 buffer对象 xrange对象
## 高级数据结构之映射：字典

### 序列运算符：切片(起始位置 终止位置 步长) 序列+序列 序列*数字 in len min max

#### list: 
##### list构造 赋值x[10]=100(list x长度必须大于10) 
##### del x[10] append(一个) extend(一组) x.count(100) 
##### x.index(100) x.remove('1000')
##### x.insert(1,'1000') x.pop(0)  
##### x.reverse()(就地完成) x.sort(cmp, key=len, reverse=True)(就地完成,返回None) y=sorted(x)

#### tuple(不可变的list)：映射的键值 & 函数的返回值