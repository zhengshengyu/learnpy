#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 映射mapping数据结构：字典
## 构建：{"zsy":123, "whf":124} dict([("zsy",123), ("whf",124)]) dict(name="zsy", age=123)
dict1 = {"name":"zsy1", "age":124}
dict2 = dict([("name", "zsy2"), ("age",125)])
dict3 = dict(name="zsy3", age=126)
print dict1, dict2, dict3

print "zsy1's age is %(age)s" % dict1

## 操作：clear copy(shallow) fromkeys get has_key d1.pop('name') d1.popitem() d1.setdefault('birth', 'N/A') d1.update(d2)
### items iteritms; keys iterkeys; values itervalues