#!/usr/bin/env python
# -*- coding: utf-8 -*-

print ord('A'), chr(65)
print u'ABC'.encode('utf-8'), 'abc'.decode('utf-8'), u'中文'.encode('utf-8')
print len(u'abc'), len('abc')
