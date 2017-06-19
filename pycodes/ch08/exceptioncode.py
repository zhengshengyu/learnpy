#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 异常对象表示异常，是异常类的实例

#内建异常类
import exceptions
print dir(exceptions) 

# 自定义异常类 一定要继承基类Exception
class MyOwnException(Exception):
	pass

# raise Exception
# raise Exception('0000000000') #引发异常
	
# 捕捉 try except
def division(x,y):
	try:
		print '11111111111111'
		print x/y
		print '22222222222'
	except ZeroDivisionError: #捕捉异常
		print 'The y Value is zero'
	except (TypeError, NameError), e: #捕捉异常对象
		print e
	except: #全捕捉
		print 'Something was wrong'
	else:
		print 'Ah ...    all went as planed'
	finally:
		print 'cleaning up ...'
# division(10, 0)
# division(10, '\s')
division(10, 10)
