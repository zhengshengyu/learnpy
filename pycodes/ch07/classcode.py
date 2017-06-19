#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 更加抽象：类
# 特性、方法的__private(__init__函数中初始化) _protect public gloabal
class Person():
	"""docstring for ClassName"""
	personIndex = 0; #global
	def __init__(self, id, sex, name): #构造方法
		self.__id = id #private
		self._sex = sex
		self.name = name
		Person.personIndex +=1

personList = []	
for i in xrange(1,10):
	p = Person(i, 'm', 'zsy'+str(i))
	personList.append(p)
	p.personIndex = 10 + i
	setattr(p, 'name', 'whf'+str(i)) #通用接口设置特性
	if hasattr(p, 'name'): #检查特性是否存在
		print getattr(p, 'name', None) #通用接口获取特性、
	if callable(getattr(p, 'setId', None)): #检查方法是否可调用
		p.setId(100)
	print Person.personIndex, p.personIndex, p.name, p._sex, p.__dict__, dir(p)

class Filter(object):
	def init(self):
		self.blocked = ['zsy']
	def filter(self, filterseq):
		return [s for s in filterseq if s not in self.blocked]
class SmallFilter(Filter):
	def filter(self, filterseq):
		return [s for s in filterseq if s.lower() not in self.blocked]
class UpperFilter(Filter):
	def filter(self, filterseq):
		return [s for s in filterseq if s.upper() not in self.blocked]
class zsyFilter(SmallFilter, UpperFilter): #多重继承SmallFilter、UpperFilter，但filter是从SmallFilter类中继承的，UpperFilter的被覆盖了
	"""docstring for zsyFilter"""
	def init(self): #重写基类方法
		self.blocked = ['zsy', 'whf']
fbs=SmallFilter()
fbs.init()
print fbs.filter(['zsy', 'whf', 'Zsy', 'ZSY'])
fbs=UpperFilter()
fbs.init()
print fbs.filter(['zsy', 'whf', 'Zsy', 'ZSY'])
fsb=zsyFilter()
fsb.init()
print fsb.filter(['zsy', 'whf', 'Zsy', 'ZSY'])
		
print issubclass(Filter, zsyFilter), issubclass(zsyFilter, Filter) #A是否为B的子类
print zsyFilter.__bases__, Filter.__bases__  #查看类型的基类
print isinstance(fsb, zsyFilter), isinstance(fsb, Filter), isinstance(fbs, zsyFilter) #对象a是否为类A的实例
print type(fbs), fsb.__class__ #查看对象属于哪个类
