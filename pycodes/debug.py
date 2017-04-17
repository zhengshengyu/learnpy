#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 错误处理: try...except...finally...
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e: #所有的错误类型都继承自BaseException
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'

## 常见错误类型: https://docs.python.org/2/library/exceptions.html#exception-hierarchy
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StandardError
#       |    +-- BufferError
#       |    +-- ArithmeticError
#       |    |    +-- FloatingPointError
#       |    |    +-- OverflowError
#       |    |    +-- ZeroDivisionError
#       |    +-- AssertionError
#       |    +-- AttributeError
#       |    +-- EnvironmentError
#       |    |    +-- IOError
#       |    |    +-- OSError
#       |    |         +-- WindowsError (Windows)
#       |    |         +-- VMSError (VMS)
#       |    +-- EOFError
#       |    +-- ImportError
#       |    +-- LookupError
#       |    |    +-- IndexError
#       |    |    +-- KeyError
#       |    +-- MemoryError
#       |    +-- NameError
#       |    |    +-- UnboundLocalError
#       |    +-- ReferenceError
#       |    +-- RuntimeError
#       |    |    +-- NotImplementedError
#       |    +-- SyntaxError
#       |    |    +-- IndentationError
#       |    |         +-- TabError
#       |    +-- SystemError
#       |    +-- TypeError
#       |    +-- ValueError
#       |         +-- UnicodeError
#       |              +-- UnicodeDecodeError
#       |              +-- UnicodeEncodeError
#       |              +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
# 	   +-- ImportWarning
# 	   +-- UnicodeWarning
# 	   +-- BytesWarning

# 调用堆栈
## 1.错误被Python解释器捕获，打印一个错误信息
## 2.让Python解释器来打印出错误堆栈logging.exception(e)
## 3.raise主动抛出错误，让调用者来处理相应的错误

# 调试
## print 直接查看, 优点:简单粗暴, 缺点:将来删除麻烦

## 断言assert 断言失败会抛出AssertionError
### 启动Python解释器时可以用-O参数来关闭assert: python -O err.py

## logging 有debug，info，warning，error等几个级别
### 设置日志输出级别 logging.basicConfig(level=logging.INFO)

## 启动调试器pdb: 
### 'l' 来查看代码, 'n' 单步执行代码, 'p 变量名' 查看变量, 'c' 继续运行, 'q' 结束调试
### python -m pdb err.py
### pdb.set_trace(): 可能出错的地方放置

## IDE的利用: PyCharm, Eclipse加上pydev插件


# 单元测试: 对一个模块、一个函数或者一个类来进行正确性检验的测试工作
## 运行单元测试: 在mydict_test.py的最后加上两行代码, python mydict_test.py
## 命令行通过参数-m unittest直接运行单元测试: python -m unittest mydict_test