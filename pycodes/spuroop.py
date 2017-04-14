#!/usr/bin/env python
# -*- coding: utf-8 -*-

from types import MethodType

# 多重继承、定制类、元类

## 使用__slots__:
class Student(object):
    __slots__ = ('name', 'age', 'set_age', '_score') # 允许动态绑定的属性名称。 仅对当前类起作用，对继承的子类是不起作用的   
    def __init__(self, score = 0):
        self._score = score
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

    # def get_score(self):
    #     return self._score
    # def set_score(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('score must be an integer!')
    #     if value < 0 or value > 100:
    #         raise ValueError('score must between 0 ~ 100!')
    #     self._score = value
    @property ## 使用@property装饰器:
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
### 动态绑定变量、函数
s = Student()
def set_age(self, age):
    self.age = age
# s.set_age = MethodType(set_age, s, Student) #针对实例
Student.set_age = MethodType(set_age, None, Student) #针对类
s.set_age(16)
s.name = 'Jack'
# s.sex = 'F' # not in slots
print s.name, s.age, s.set_age

## 使用@property装饰器: 负责把一个方法变成属性, 让调用者写出简短的代码
### 把一个getter方法变成属性，只需要加上@property就可以了(此时，@property本身又创建了另一个装饰器@score.setter)
### @score.setter，负责把一个setter方法变成属性赋值
s.score = 100
print s.score

## 多重继承: 一个子类就可以同时获得多个父类的所有功能。
class Animal(object):
    pass
### 大类:
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
### 功能类:
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
#### 各种动物:
class Dog(Mammal, Runnable):
    pass
class Bat(Mammal, Flyable):
    pass
class Parrot(Bird, Flyable):
    pass
class Ostrich(Bird, Runnable):
    pass

## 定制类: 几个特殊变量的使用
### __str__: 更改默认打印内容<__main__.Student object at 0x109afb190>
### __str__()返回用户看到的字符串，__repr__()返回程序开发者看到的字符串

### __iter__：一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
###          然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值
    
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print n

### __getitem__: 类想表现得像list那样按照下标取出元素
f = Fib()
print '{0}th element:{1}'.format(11, f[10])
print 'slice from {0}th to {1}th:{2}'.format(0, 10, f[0:11])