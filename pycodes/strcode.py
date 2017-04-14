# -*- coding: utf-8 -*- #告诉Python解释器，按照UTF-8编码读取源代码
#!/usr/bin/env python  #告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释

import datetime, time
import functools

# 数据类型：bool int float unicode str None
# 字符编码
print ord('A'), chr(65)
print u'ABC'.encode('utf-8'), 'abc'.decode('utf-8'), u'中文'.encode('utf-8')
print len(u'abc'), len('abc')

# 格式化
print 'the num is %d-%d' % (1, 10)
print 'the num is {0}-{1}'.format(1, 10)

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
sum1 = 0
for x in range(101):
    sum1 = sum1 + x
print sum1

sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n - 2
print sum2

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
### 判断一个对象是否可以迭代
from collections import Iterable
print isinstance('abc', Iterable)
### 硬是要取下标
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

### 如果函数定义中包含yield关键字，那么这个函数就是一个generator
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

## 几个常用的高阶函数：map/reduce filter sorted
### map(函数(一个参数), 序列)，将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
print map(str, range(1,10))
### reduce(函数(两个参数), 序列)，把结果继续和序列的下一个元素做累积计算
print sum(range(1,10))
print reduce(lambda x,y: x+y, range(1,10))
def my_add(x,y):
	return x+y
print reduce(my_add, range(1,10))
### filter(函数, 序列)，把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, 'C', '  '])
### sorted
#### 通常规定：对于两个元素x和y，如果认为x < y，则返回-1；如果认为x == y，则返回0；如果认为x > y，则返回1
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

## 返回函数 --闭包（Closure）
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i # not ok, 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

def count_zhengjiu(): #硬要引用循环变量怎么办
	fs = []
	for i in range(1, 4):
		def f(j):
			def g():
				return j*j
			return g
		fs.append(f(i))
   	return fs
f1, f2, f3 = count_zhengjiu()
print f1(), f2(), f3()

## 匿名函数lambda x: x * x

## 装饰器（Decorator）：不改变函数定义，只在代码运行期间动态增加功能的方式，是一个返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log # @语法：把@log放到now()函数的定义处 + 2层嵌套 <==> 执行了语句now = log(now)
def now():
    print time.strftime('%Y-%m-%d',time.localtime(time.time()))
now()
print now.__name__

def log(text):
    def decorator(func):
    	@functools.wraps(func) # 恢复now本身的__name__属性
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute') # 3层嵌套 <==> 执行了语句now = log('execute')(now)
def now():
    print time.strftime('%Y-%m-%d',time.localtime(time.time()))
now()
print now.__name__

def log(text_begin, text_end):
	def decorator(func):
		@functools.wraps(func)
		def wrapper():
			print '%s %s():' % (text_begin, func.__name__)
			def g():
				return func(*args, **kw)
			print '%s %s():' % (text_end, func.__name__)
			return g
		return wrapper
	return decorator
@log('execute_begin', 'execute_end') # 3层嵌套 <==> 执行了语句now = log('execute')(now)
def now():
    print time.strftime('%Y-%m-%d',time.localtime(time.time()))
now()

## 偏函数：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
## 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数
print int('10010', base=2)
int2 = functools.partial(int, base=2) # <==>def int2(x, base=2): return int(x, base)
print int2('10010', base=2) # int2('10010', base=2, base=2)
print int2('10010') # <==> kw = { base: 2 } int('10010', **kw)
max2 = functools.partial(max, 100)
print max2(1,2,3) # <==> args = (100, 5, 6, 7) max(*args)


