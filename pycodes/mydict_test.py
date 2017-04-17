#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from mydict import Dict

class TestDict(unittest.TestCase): #测试类，从unittest.TestCase继承
    # setUp tearDown分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print 'setUp...'
    def tearDown(self):
        print 'tearDown...'

    def test_init(self): #以test开头的方法才会被认为是测试方法，测试的时候才会被执行
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1) #断言函数返回的结果与1相等
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError): #with --期待抛出指定类型的Error: 
            value = d['empty'] #d['empty']访问不存在的key时, 语句被执行

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError): #通过d.empty访问不存在的key时，期待抛出AttributeError
            value = d.empty

if __name__ == '__main__':
    unittest.main()