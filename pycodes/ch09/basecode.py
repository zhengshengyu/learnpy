#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import exceptions
# 魔法方法 属性 迭代器

# 新旧式类: 
# 新类保证方法 1.添加__metaclass__=type于模块首行 2.继承object
class NewStyle(object):
	# pass
	def __init__(self, val=0):
		self.someval=val

class OldStyle():
	# pass
	def __init__(self, val=0):
		self.someval=val

n1 = NewStyle()
o1= OldStyle()
print dir(n1)
print dir(o1)

# 继承：重写方法 __init__ super
class Bird(object):
	"""docstring for Bird"""
	def __init__(self, arg = 'None'):
		super(Bird, self).__init__() #object.__init__(self) ##两种调用父类__init__的方法
		self.hungry = True
	def eat(self):
		if self.hungry:
			print 'Aaaaaaa'
			self.hungry = False
		else:
			print 'No, Thanks'

class SingBird(Bird):
	"""docstring for SingBird"""
	def __init__(self, arg = 'None'):
		super(SingBird, self).__init__() #Bird.__init__(self)
		self.sound = 'Squawk'

singbird = SingBird()
print singbird.eat()
print singbird.sound

# 基本序列和映射规则：__len__ __getitem__ __setitem__ __delitem__
# 属性property: 
# 装饰器decorator:让其他函数或类在不需要做任何代码修改的前提下增加额外功能，装饰器的返回值也是一个函数/类对象。它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景，装饰器是解决这类问题的绝佳设计
def use_logging1(func): #没有包装，直接调用了foo，不是装饰器
	func()
	logging.warn("%s is running" % func.__name__)
def foo():
	print('i am foo')
# use_logging1(foo)

def use_logging2(func): #就是一个装饰器, 把执行真正业务逻辑的函数 func 包裹在其中，看起来像 foo 被 use_logging 装饰了一样
    def wrapper():
        logging.warn("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper
# def foo():
# 	print('i am foo')
# foo = use_logging2(foo) # 直接调用装饰
# foo()
@use_logging2 # @装饰器的语法糖 等价于foo = use_logging2(foo)
def foo():
	print('i am foo')
foo()


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper
    return decorator

# @use_logging(level="warn") #带参数的装饰器 等价于@decorator
# def foo00(name='foo00'):
#     print("i am %s" % name)
# foo00()

def foo00(name='foo00'):
    print("i am %s" % name)
decorator = use_logging(level="warn")
foo00 = decorator(foo00)
foo00()

# 迭代器
class Fibs():
	"""docstring for Fibs
	0 1 2 3 4 5 6 7 8 9 10
	0 1 1 2 3 5 8 13 21 34
	"""
	def __init__(self):
		self.a = 0
		self.b = 1
	def next(self): #有了next方法，则该类对象就是迭代器
		self.a, self.b = self.b, self.a+self.b
		if self.a > 1000:
			raise StopIteration
		return self.a
	def __iter__(self): #有了__iter__方法，则该类对象就是可迭代的
		return self

fibs = Fibs()
# print list(fibs)
for f in fibs:
	if f > 10:
		print f, '____________'
		break
it=iter(fibs) #从迭代对象中获取迭代器
for x in xrange(1,10):
	print it.next()

# 生成器：任何包含yield语句的函数
def flatten(nested): #创建生成器
	for sublist in nested:
		for element in sublist:
			yield element
print flatten, flatten([[11,12],[1,2]]), list(flatten([[11,12],[1,2]]))
def recursionflatten(nested): #创建递归生成器
	try:
		try: 
			print nested + ""
		except TypeError:
			print nested
			pass
		else:
			raise TypeError
		for sublist in nested:
			for element in recursionflatten(sublist):
				yield element
	except TypeError:
		yield nested
print list(recursionflatten(['zsy',[[4,5],[[10],11]]]))


