"""
collections模块

namedtuple():命名元组
defaultdict():默认值字典.
Counter():计数器
"""

from collections import namedtuple,defaultdict,Counter
# namedtuple()
# Rectangle = namedtuple('Rectangle_class',['length','width'])
# #
# r = Rectangle(10,5)
# # 通过属性访问元组的元素
# print(r.length)
# print(r.width)
#
# # 通过索引的方式访问元素
# print(r[0])
# print(r[1])

# defautldict:
# 创建一个字典的方式:
# d = {'name':'Andy','age':10}
# d = dict([('name','Andy'),('age',10)])
# d = {k:v for k,v in [(1,2),(3,4)]}
# print(d)
# defaultdict()
# d = defaultdict(int,name='Andy',age=10)
# print(d['name'])
# print(d['age'])
# print(d['addr'])            # {'addr':0} 也会被添加
# print(d)

# 自定义函数充当第一个参数:
# 要求,不能有参数
# def f():
#     return 'hello'
#
# d = defaultdict(f,name='Andy',age=10)
# print(d['addr'])
# print(d)

# Counter:计数器
c = Counter('abcdefabccccdd')
print(c)
print(c.most_common(3))

