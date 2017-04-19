#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 把变量从内存中变成可存储或传输的过程称之为序列化(serialization/pickling), 反之为反序列化(unpicking)

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
try:
    import cPickle as pickle
except ImportError:
    import pickle
d = dict(name='Bob', age=20, score=88)
## 把任意对象序列化成一个str, 并写入到文件
_sstr = pickle.dumps(d) 
_filePath = 'serialize.txt'
with open(_filePath, 'w') as f:
    f.write(_sstr)
## 从文件中读内容到str，然后用pickle.loads()方法反序列化出对象
with open(_filePath, 'r') as f:
    _sstr = f.read()
d = pickle.loads(_sstr)
print d
# 精简版
## 对象序列化到文件
f2 = open(_filePath, 'wb')
pickle.dump(d, f2)
f2.close()
## 文件内容反序列化到对象
f2 = open(_filePath, 'rb')
d2 = pickle.load(f2)
f2.close()
print d2


# JSON
## 内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json
d = dict(name='Bob', age=20, score=88)
### Python对象变成一个JSON
json_ob = json.dumps(d) # 返回一个str，内容就是标准的JSON
print json_ob
### JSON反序列化为Python对象
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
py_ob = json.loads(json_str)
print py_ob

### class 对象序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Meimei', 20, 100)
# print(json.dumps(s, default=lambda obj: obj.__dict__))
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))  
### class 反序列化
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 100, "name": "Meimei"}'
print(json.loads(json_str, object_hook=dict2student))