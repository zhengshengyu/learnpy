#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
# 为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

# 面向对象的程序设计把计算机程序视为一组对象的集合，
# 每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
# 面向对象的设计思想是抽象出Class，根据Class创建Instance。

# 定义类
class Student(object): # (object)，表示该类是从哪个类继承下来的
    def __init__(self, name = 'hanmei', score = '100'): # 第一个参数永远是self，表示创建的实例本身
        self.name = name # public
        self.__score = score # private，外部仍可通过_Student__score来访问
    	self.__doc__ = 'zhengshengyu first py class' # 特殊变量可以直接访问的
    def get_score(self): # 数据封装，访问统一走此接口
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
# 实例化
bart = Student()
bart.sex = 'F' # 不同于静态语言，可以直接添加新的变量、函数

from types import MethodType
def set_sex(self, sex):
    self.sex = sex
bart.set_sex = MethodType(set_sex, bart, Student) # 给实例绑定一个方法
Student.set_sex = MethodType(set_sex, None, Student) # 给class绑定方法
bart.set_sex('M')
print bart.sex

print bart.get_score(), bart.get_grade()
print bart.name
# print bart.__score
print bart._Student__score 
print bart.__doc__


# 继承和多态
# 继承好处：1.子类获得了父类的全部功能 2.实现多态，覆盖父类方法
class Animal(object):
    def __init__(self):
        self.__birth = 'Friday'
    def run(self):
        print 'Animal is running...'
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'
class Cat(Animal):
    pass

l = list() # l是list类型
a = Animal() # a是Animal类型
c = Cat()
d = Dog() # d是Dog类型
c.run()
d.run()

# 子类型对象是父类类型， 但是父类型对象不是子类类型
print isinstance(d, Dog), isinstance(d, Animal), isinstance(d, object)
print isinstance(a, Dog)

# 任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行
# 多态好处：当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
# 			因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
#			由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法
def run_twice(animal):
    animal.run()
    animal.run()
# 多态性：对于传入参数，只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定
run_twice(Dog()) # 如此调用ok

class Tortoise(Animal): #当新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
    def run(self):
        print 'Tortoise is running slowly...'
# “开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
run_twice(Tortoise()) 


# 获取对象信息：
# 对象是什么类型 -- type(obj) -- isinstance(obj, type)
import types
print type('abc')==types.StringType, type(u'abc')==types.UnicodeType, type([])==types.ListType
print type(int)==type(str)==types.TypeType # 所有类型本身的类型就是TypeType
print type(l), type(a), type(c), type(d)
print isinstance(u'a', (str, unicode)), isinstance(u'a', basestring) #str和unicode都是从basestring继承下来的
# 对象的所有属性和方法，-- dir(obj)
# 配合使用getattr()、setattr()以及hasattr()，以直接操作一个对象的状态
print dir(d)
print getattr(d, 'run')
setattr(d, 'age', 0)
if hasattr(d, 'age'):
    print getattr(d, 'age')
else:
    print 'no attr'
