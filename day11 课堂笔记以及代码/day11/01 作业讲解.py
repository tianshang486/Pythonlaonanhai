# 写函数，函数可以支持接收任意数字（位置传参）并将所有数据相加并返回。
#
# 看代码写结果
#
#
# def func():
#     return 1, 2, 3
#
#
# val = func()
# print(type(val) == tuple)
# print(type(val) == list)
# 看代码写结果
#
#
# def func(*args, **kwargs):
#     print(args)  # ('武沛齐','金鑫','女神',[11,22,33],)
#     print(kwargs) # {'k1':'栈'}


# a. 请将执行函数，并实现让args的值为 (1,2,3,4)
# func(1,2,3,4)
# func(*[1,2,3,4])
# b. 请将执行函数，并实现让args的值为 ([1,2,3,4],[11,22,33])
# func([1,2,3,4],[11,22,33])
# c. 请将执行函数，并实现让args的值为 ([11,22],33) 且 kwargs的值为{'k1':'v1','k2':'v2'}
# func([11,22,],33,k1='v1',k2='v2')
# d. 如执行 func(*{'武沛齐','金鑫','女神'})，请问 args和kwargs的值分别是？
# func(*{'武沛齐','金鑫','女神'})
# e. 如执行 func({'武沛齐','金鑫','女神'},[11,22,33])，请问 args和kwargs的值分别是？

# f. 如执行 func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})，请问 args和kwargs的值分别是？
# func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})

# 看代码写结果
#
#
def func(name, age=19, email='123@qq.com'):
    pass

# # a. 执行 func('alex') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func('alex')
# # b. 执行 func('alex',20) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func('alex',20)
# # c. 执行 func('alex',20,30) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func('alex',20,30)
# # d. 执行 func('alex',email='x@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？

# # e. 执行 func('alex',email='x@qq.com',age=99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func('alex',email='x@qq.com',age=99)
# # f. 执行 func(name='alex',99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func(name='alex',99)
# # g. 执行 func(name='alex',99,'111@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func(99,'111@qq.com',name='alex',)
# 看代码写结果
#
#
# def func(users, name):
#     users.append(name)
#     return users
#
# result = func(['武沛齐', '李杰'], 'alex')
# print(result)  # ['武沛齐', '李杰','alex']
# 看代码写结果
#
#
# def func(v1):
#     return v1 * 2
#
#
# def bar(arg):
#     return "%s 是什么玩意？" % (arg,)
#
#
# val = func('你')  # '你你'
# data = bar(val)  # bar('你你')
# print(data)  # '你你 是什么玩意？'
# 看代码写结果
#
#
# def func(v1):
#     return v1 * 2
#
#
# def bar(arg):
#     msg = "%s 是什么玩意？" % (arg,)
#     print(msg)
#
#
# val = func('你')
# data = bar(val)
# print(data)
# 看代码写结果
#
# v1 = '武沛齐'
#
#
# def func():
#     print(v1)
#
#
# func()
# v1 = '老男人'
# func()
# 看代码写结果
#

#
#
# v1 = '武沛齐'
# def func():
#     v1 = '景女神'
#     def inner():
#         print(v1)
#     v1 = '肖大侠'
#     inner()
#
# func()
# print(v1)
# v1 = '老男人'
# func()
# print(v1)


# 看代码写结果【可选】
#
# def func():
#     data = 2 * 2
#     return data
#
#
# new_name = func
# val = new_name()
# print(val)
#
# # 注意：函数类似于变量，func代指一块代码的内存地址。
# 看代码写结果【可选】
#
# def func():
#     data = 2 * 2
#     return data
#
#
# data_list = [func, func, func]
# for item in data_list:
#     v = item()
#     print(v)
#
# # 注意：函数类似于变量，func代指一块代码的内存地址。
# 看代码写结果（函数可以做参数进行传递）【可选】
#
# def func(arg):
#     arg()
#
#
# def show():
#     print('show函数')
#
#
# func(show)
# 写函数，接收n个数字，求这些参数数字的和。（动态传参）
#
# 读代码，回答：代码中, 打印出来的值a, b, c分别是什么？为什么？
#
# a = 10
# b = 20
# def test5(a, b):
#     print(a, b)  # (20,10)
# # c = test5(b, a)
# c = test5(20, 10)
# print(c)  # None

# 读代码，回答：代码中, 打印出来的值a, b, c分别是什么？为什么？
# a = 10
# b = 20
# def test5(a, b):
#     a = 20
#     b = 10
#     a = 3
#     b = 5
#     print(a, b)
# # c = test5(b, a)
# c = test5(20, 10)
# print(c)
# 传入函数中多个列表和字典, 如何将每个列表的每个元素依次添加到函数的动态参数args里面？如何将每个字典的所有键值对依次添加到kwargs里面？
#
# 写函数, 接收两个数字参数, 将较小的数字返回.
#
# 写函数, 接收一个参数(此参数类型必须是可迭代对象), 将可迭代对象的每个元素以’_’相连接, 形成新的字符串, 并返回.
#
# 例如
# 传入的可迭代对象为[1, '老男孩', '武sir']
# 返回的结果为’1
# _老男孩_武sir’
#
# 19.
# 有如下函数:
#
#
# def wrapper():
#     def inner():
#         print(666)
#
#
# wrapper()
# 你可以任意添加代码, 执行inner函数.
#
# 相关面试题：
# 写出下列代码结果：
#
# def foo(a, b, *args, c, sex=None, **kwargs):
#     print(a, b)
#
#     print(c)
#
#     print(sex)
#
#     print(args)
#
#     print(kwargs)
#
# \  # foo(1,2,3,4,c=6)
#
# \  # foo(1,2,sex='男',name='alex',hobby='old_woman')
#
# \  # foo(1,2,3,4,name='alex',sex='男')
#
# \  # foo(1,2,c=18)
#
# \  # foo(2, 3, [1, 2, 3],c=13,hobby='喝茶')
#
# \  # foo(*[1, 2, 3, 4],**{'name':'太白','c':12,'sex':'女'})