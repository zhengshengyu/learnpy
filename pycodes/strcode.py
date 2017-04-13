# -*- coding: utf-8 -*- #告诉Python解释器，按照UTF-8编码读取源代码
#!/usr/bin/env python  #告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# 数据类型：bool int float unicode str None
# 字符编码
print ord('A'), chr(65)
print u'ABC'.encode('utf-8'), 'abc'.decode('utf-8'), u'中文'.encode('utf-8')
print len(u'abc'), len('abc')

# 格式化
print  'Age: %s. Gender: %s' % (25, True)

a = 'abc' 
#a是变量，而'abc'才是字符串对象！
# a本身是一个变量，它指向的对象的内容才是'abc'

# list(可变对象，传递时绑定同一个内存地址) & tuple(不可变)
ls1 = [1]
ls2 = ls1
ls3 = ls1[:]
ls1[0] = 10
print ls1, ls2, ls3

tp1 = (1,) #将名字tp1与内存中值为(1)的内存绑定在一起
tp2 = tp1 #变量tp2执行与tp1绑定的内存
tp1 = (10,) #创建一个内存值为(10,) 的内存地址与变量名字tp1进行绑定
# tp1[1] = 'charp' #不可变　'tuple' object does not support item assignment
print tp1, tp2

# 条件语句
age = 20
if age <10:
    print 'kid'
elif age < 18: #else if --Error
    print 'teenager'
else:
    print 'adult'

# 循环语句
sum = 0
for x in range(101):
    sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

# dict & set
# dict的key必须是不可变对象。
# set和dict类似，也是一组key的集合，但不存储value
t = (1,2,3)
l = [1,2,3]
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d[t] = 100
# d[l] = 1000 --Error
print d
s = set([1, 1, 2, 2, 3, 3])
print s

# 函数
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。
## 必选参数、默认参数、可变参数和关键字参数
### 默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]): #默认参数L也是一个变量，它指向对象[]
    L.append('END')
    return L
print add_end(), add_end()
### 可变参数：参数前面加1个*, 接收的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print calc(1,2), calc()
nums = [1,2,3]
# print calc(nums[0], nums[1], nums[2])
print calc(*nums)
### 关键字参数：参数前面加2个*, 接收的是一个dict
### 允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
person('Adam', 45, gender='M', job='Engineer')
kw = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack', 24, **kw)
## 尾递归：在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def fact_iter(num, product): # ok, 能防止栈溢出
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
def fact(n): #bad
    if n==1:
        return 1
    return n * fact(n - 1)
# print fact_iter(1000, 1) #但Python解释器没有做优化，所以这里还会导致栈溢出

##（Slice）操作符 --正数第一个元素的索引是0，倒数第一个元素的索引是-1
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:-1], L[::2], L[-2:-1]
## 迭代（Iteration）：通过for ... in循环来遍历str list tuple dict
# 判断一个对象是否可以迭代
from collections import Iterable
print isinstance('abc', Iterable)
# 硬是要取下标
for i, value in enumerate(['A', 'B', 'C']):
    pass
## 列表生成式（List Comprehensions）
L = [m + n for m in 'ABC' for n in 'XYZ']
print L
## 生成器（Generator）：一边循环一边计算的机制
g = (x * x for x in range(3))
print g
for n in g:
    print n

# 如果函数定义中包含yield关键字，那么这个函数就是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
print fib(6)

# 函数式编程（请注意多了一个“式”字）——Functional Programming
# 允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。