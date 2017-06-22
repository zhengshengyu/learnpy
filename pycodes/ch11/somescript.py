#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
text = sys.stdin.read()
print text
words = text.split()
wordlen = len(words)
print 'wordlen:', wordlen