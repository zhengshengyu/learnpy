#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 更加抽象：创建自己的对象object -polymorphism -encapsulation -inheritance
 
__metaclass__=type
class Person():
    def __init__(self, name='None'):
        self.__name = name # 私有特性
    def setPrivateName(self, name):
        self.__privateName = name
    def getPrivateName(self):
        return self.__privateName
    def __unaccessible(self): # 私有方法
        print 'u can not access this method!', self.__name
    def accessible(self):
        print 'call the secret method'
        self.__unaccessible()

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print 'hello, i am %s.' %self.name

p1 = Person()
p1.setName('zsy') #Person.setName(p1, 'zsy')
p1.greet()
p1.name = 'zsy001' #特性name 外部可访问
p1.accessible()
# p1._Person__unaccessible()
