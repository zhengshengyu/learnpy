#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 抽象
# 函数化：callable判断函数是否可调用
## 参数：整数 字符串 元组均不可变，函数里面动了外面不会随之修改；list dict则会一块变动
def fibs(nums):
    '文档字符串：获取斐波那契数列'
    result=[0,1]
    for i in range(nums-2):
        result.append(result[-1]+result[-2])
    return result

if callable(fibs):
    print fibs.__doc__
    print fibs(10)

### 位置参数name
### 关键字参数punctuation：带默认值，但是比C#更灵活，可以定向添加某个参数
def hello(name, greeting='hello', punctuation='!'):
    print "%s %s%s" % (greeting, name, punctuation)
hello('python', punctuation='.')
### 收集参数params(转为元组) params2(转为字典):可以处理关键字参数
def print_params(title, *params, **params2):
    print title
    print params
    print params2
print_params(1,2,3,4, zsy='zhengshengyu', whf='wanghuifang')
### 收集参数的逆过程(调用加*)
def add(x,y,m=0,n=0):
    return x+y+m+n
def call_add(*params1, **params2):
    print 'call add-------------'
    print params1, params2
    localscope = locals()
    print localscope
    return add(*params1, **params2)
print call_add(1,2, m=6, n=7)
p1=(1,2)
p2={'m':3,'n':4}
p22=dict(m=3,n=4)
p222=dict([('m',3),('n',4)])
print call_add(*p1, **p222)

# 作用域：函数内的局部作用域locals() 整个脚本的全局作用域globals()
scope = vars() #返回变量和值的不可见字典  
# print scope['p1'], scope['p2'], scope['add']
globalscope = globals()
print globalscope
# 嵌套作用域closure
def multiplier(factor):
    def multiplyByFactor(num):
        return num*factor
    return multiplyByFactor
double = multiplier(2)
print double(100)

# 递归
def power(x,n):
    if n==0:
        return 1;
    else:
        return x*power(x,n-1)
def factorial(n):
    if n <= 1:
        return 1;
    else:
        return n*factorial(n-1)
print power(2,10), factorial(5)

import bisect
def binarysearch(sequence, value, lower, upper):
    mid = (lower+upper) // 2
    if sequence[mid] == value:
        return mid
    elif lower >= mid:
        return len(sequence)
    elif sequence[mid] < value:
        return binarysearch(sequence, value, mid+1, upper)
    else:
        return binarysearch(sequence, value, lower, mid-1)

sortedseq = sorted(range(1,10))
val = 20
print '%s index is %d' % (val, binarysearch(sortedseq, val, 0, len(sortedseq)-1))
print '%s index is %d' % (val, bisect.bisect_left(sortedseq,val))

# 函数式编程map filter reduce
print map(str, map(double, range(1,10)))
print filter(lambda s: s.isalnum(), ['fooo', '1223', 'sd_2', 'ssd3']) #找出由字母和数字组成的字符串
print reduce(lambda x,y: x+y, range(1,10)) #func(fuc(func(s[0],s[1]), s[2]), s[3])