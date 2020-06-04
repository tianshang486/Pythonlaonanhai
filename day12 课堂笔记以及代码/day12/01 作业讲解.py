# 请写出下列代码的执行结果：﻿
# 例一：
#
# def func1():
#     print(**'in func1' **)
#
#
# def func2():
#     print(**'in func2' **)
#
#
# ret = func1
#
# ret()
#
# ret1 = func2
#
# ret1()
#
# ret2 = ret
#
# ret3 = ret2
#
# ret2()
#
# ret3()
#
# 执行结果：
#
# ​    例二：
#
# def func1():
#     print(**'in func1' **)
#
#
# def func2():
#     print(**'in func2' **)
#
#
# def func3(x, y):
#     x()
#
#     print(**'in func3' **)
#
#     y()
#
#
# print(111)
#
# func3(func2, func1)
#
# print(222)
#
# 执行结果：
#
#
#
# ​    例三（选做题）：
#
def func1():
    print('in func1')

def func2(x):  # x = func1
    print('in func2')
    return x

def func3(y):  # y = func2
    print('in func3')
    return y
# ret = func2(func1)
# ret()  # func1()
# ret2 = func3(func2)  # func2
# ret3 = ret2(func1)  # func2(func1)  func1
# ret3()  # func1()

# 执行结果：
#
# 看代码写结果：
#
# def func(arg):
#     return arg.replace('苍老师', '***')
#
#
# def run():
#     msg = "Alex的女朋友苍老师和大家都是好朋友"
#     result = func(msg)
#     print(result)
#
# run()

# def func(arg):
#     return arg.replace('苍老师', '***')
#
#
# def run():
#     msg = "Alex的女朋友苍老师和大家都是好朋友"
#     result = func(msg)
#     print(result)
#
#
# data = run()
# print(data)
# 看代码写结果：
#
# DATA_LIST = []
#
#
# def func(arg):
#     return DATA_LIST.insert(0, arg)
#
#
# data = func('绕不死你')
# print(data)
# print(DATA_LIST)
# 看代码写结果：
#
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
#
# func_list = [func, func, func]
#
# for item in func_list:
#     val = item()
#     print(val)
# 看代码写结果：
#
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
#
# func_list = [func, func, func]
#
# for i in range(len(func_list)):
#     val = func_list[i]()
#     print(val)
# 看代码写结果：
#
# def func():
#     return '烧饼'
#
#
# def bar():
#     return '豆饼'
#
#
# def base(a1, a2):
#     return a1() + a2()
#
#
# result = base(func, bar)
# print(result)
#
# 看代码写结果：
# for item in range(10):
#     print(item)
#
# print(item)
#
# 看代码写结果：
#
# def func():
#     for item in range(10):
#         pass
#     print(item)
# func()
# #
# 看代码写结果：
# item = '老男孩'
#
#
# def func():
#     item = 'alex'
#
#     def inner():
#         print(item)
#
#     for item in range(10):
#         pass
#     inner()
#
#
# func()
#
# 看代码写结果：
# l1 = []
# def func(args):
#     l1.append(args)
#     return l1
# print(func(1))  # [1,]
# print(func(2))  # [1,2]
# print(func(3))  # [1,2,3]
# print(l1)
#
# 看代码写结果：
# name = '太白'
#
#
# def func():
#     global name
#     name = '男神'
#
#
# print(name)
# func()
# print(name)
#
# 看代码写结果：
# name = '太白'
#
#
# def func():
#     print(name)
#
#
# func()
#
# 看代码写结果：
# name = '太白'
#
#
# def func():
#     print(name)
#     name = 'alex'
#
#
# func()
#
# 看代码写结果：
#
# def func():
#     count = 1
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#
#     print(count)
#     inner()
#     print(count)
#
#
# func()
#
# 看代码写结果：
#
def extendList(val, list=[]):
    list.append(val)
    return list


# list1 = extendList(10)  # [10,]
# list2 = extendList(123, [])
# list3 = extendList('a')
#
# print('list1=%s' % list1)
# print('list2=%s' % list2)
# print('list3=%s' % list3)

# 看代码写结果：
#
# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
#
# print('list1=%s' % extendList(10))
# print('list2=%s' % extendList(123, []))
# print('list3=%s' % extendList('a'))
#
# 用你的理解解释一下什么是可迭代对象，什么是迭代器。
# 如何判断该对象是否是可迭代对象或者迭代器？
# 写代码：用while循环模拟for内部的循环机制（面试题）。
# 写函数，传入n个数，返回字典
# {‘max’:最大值,’min’:最小值}﻿
# ﻿例如: min_max(2, 5, 7, 8, 4)
# 返回: {‘max’:8,’min’:2}(此题用到max(), min()内置函数)
# print(max([1,2,3,4]))
# max
# def func(*args):
#     return {'max':max(args),'min':min(args)}
# print(func(1,2,100,123,45,6,7,89))



# 写函数，传入一个参数n，返回n的阶乘﻿
# ﻿例如: cal(7)
# 计算7*6*5*4*3*2*1
#
# def func(num):
#     count = 1
#     for i in range(num, 0, -1):
#         count = count * i
# func(10)


# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组(选做题)﻿
# ﻿例如：[(‘红心’，2), (‘草花’，2), …(‘黑桃’，‘A’)]





# 写代码完成99乘法表.(选做题，面试题)
# 1 * 1 = 1
#
# 2 * 1 = 2
# 2 * 2 = 4
#
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
#
# ......
#
# 9 * 1 = 9
# 9 * 2 = 18
# 9 * 3 = 27
# 9 * 4 = 36
# 9 * 5 = 45
# 9 * 6 = 54
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81