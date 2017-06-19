#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Windowa 将 D:\git_repository\learnpy\pycodes\site-packages 添加到系统变量PYTHONPATH中
# Linux 将 模块路径添加到.bashrc中
def hello():
	print 'hello python'
def test():
	hello()
if __name__ == '__main__': # 在"主程序"中才执行，被导入不执行
	test()