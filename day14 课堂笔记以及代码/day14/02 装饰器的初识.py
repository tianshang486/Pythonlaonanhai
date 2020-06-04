# 装饰器：装饰，装修，房子就可以住，如果装修，不影响你住，而且体验更加，让你生活中增加了很多功能：洗澡，看电视，沙发。
# 器：工具。
# 开放封闭原则：
# 开放：对代码的拓展开放的， 更新地图，加新枪，等等。
# 封闭：对源码的修改是封闭的。闪躲用q。就是一个功能，一个函数。 别人赤手空拳打你，用机枪扫你，扔雷.....这个功能不会改变。

# 装饰器：完全遵循开放封闭原则。
# 装饰器： 在不改变原函数的代码以及调用方式的前提下，为其增加新的功能。
# 装饰器就是一个函数。


# 版本一： 大壮 写一些代码测试一下index函数的执行效率。
import time
# def index():
#     '''有很多代码.....'''
#     time.sleep(2) # 模拟的网络延迟或者代码效率
#     print('欢迎登录博客园首页')
#
# def dariy():
#     '''有很多代码.....'''
#     time.sleep(3) # 模拟的网络延迟或者代码效率
#     print('欢迎登录日记页面')

# print(time.time())  # 格林威治时间。
# print(111)
# time.sleep(3)
# print(222)
# 版本一有问题： 如果测试别人的代码，必须重新赋值粘贴。
# start_time = time.time()
# index()
# end_time = time.time()
# print(end_time-start_time)
#
# start_time = time.time()
# dariy()
# end_time = time.time()
# print(end_time-start_time)
#
#
# start_time = time.time()
# # dariy()
# end_time = time.time()
# print(end_time-start_time)

# 版本二：利用函数，解决代码重复使用的问题
# import time
# def index():
#     '''有很多代码.....'''
#     time.sleep(2) # 模拟的网络延迟或者代码效率
#     print('欢迎登录博客园首页')
# # index()
# def dariy():
#     '''有很多代码.....'''
#     time.sleep(3) # 模拟的网络延迟或者代码效率
#     print('欢迎登录日记页面')
#
# def timmer(f):  # f= index
#     start_time = time.time()
#     f()  # index()
#     end_time = time.time()
#     print(f'测试本函数的执行效率{end_time-start_time}')
# timmer(index)

# 版本二还是有问题： 原来index函数源码没有变化，给原函数添加了一个新的功能测试原函数的执行效率的功能。
# 满足开放封闭原则么？原函数的调用方式改变了。


# 版本三：不能改变原函数的调用方式。
# import time
# def index():
#     '''有很多代码.....'''
#     time.sleep(2) # 模拟的网络延迟或者代码效率
#     print('欢迎登录博客园首页')
#
# def timmer(f):  # f = index  (funciton index123)
#     def inner():  # inner :(funciton inner123)
#         start_time = time.time()
#         f()  # index() (funciton index123)
#         end_time = time.time()
#         print(f'测试本函数的执行效率{end_time-start_time}')
#     return inner  # (funciton inner123)
# timmer(index)  # index()
# ret = timmer(index)  # inner
# ret()  # inner()
# index = timmer(index)  # inner (funciton inner123)
# index()  # inner()
# def func():
#     print('in func')
#
# def func1():
#     print('in func1')
#
# # func()
# # func1()
# func()
# func = 666
# func(0)

# 版本四：具体研究：
# import time
# def index():
#     '''有很多代码.....'''
#     time.sleep(2) # 模拟的网络延迟或者代码效率
#     print('欢迎登录博客园首页')
#
# def timmer(f):
#     f = index
#     # f = <function index at 0x0000023BA3E8A268>
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print(f'测试本函数的执行效率{end_time-start_time}')
#     return inner
#
# index = timmer(index)
# index()

# 版本五：python做了一个优化；提出了一个语法糖的概念。 标准版的装饰器
# import time
# # timmer装饰器
# def timmer(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print(f'测试本函数的执行效率{end_time-start_time}')
#     return inner
#
# # @timmer # index = timmer(index)
# def index():
#     '''有很多代码.....'''
#     time.sleep(0.6) # 模拟的网络延迟或者代码效率
#     print('欢迎登录博客园首页')
#     return 666
# ret = index()
# print(ret)

# def dariy():
#     '''有很多代码.....'''
#     time.sleep(3) # 模拟的网络延迟或者代码效率
#     print('欢迎登录日记页面')
# dariy()
# # index = timmer(index)
# # index()
# # dariy = timmer(dariy)  @timmer
# dariy()


# # 版本六： 被装饰函数带返回值
#
# import time
# # timmer装饰器
# def timmer(f):
#     # f = index
#     def inner():
#         start_time = time.time()
#         # print(f'这是个f():{f()}!!!') # index()
#         r = f()
#         end_time = time.time()
#         print(f'测试本函数的执行效率{end_time-start_time}')
#         return r
#     return inner
#
# @timmer # index = timmer(index)
# def index():
#     '''有很多代码.....'''
#     time.sleep(0.6) # 模拟的网络延迟或者代码效率
#     print('欢迎登录博客园首页')
#     return 666
# # 加上装饰器不应该改变原函数的返回值，所以666 应该返回给我下面的ret，
# # 但是下面的这个ret实际接收的是inner函数的返回值，而666返回给的是装饰器里面的
# # f() 也就是 r,我们现在要解决的问题就是将r给inner的返回值。
# ret = index()  # inner()
# print(ret)


# 版本八： 被装饰函数带返回值

import time
# timmer装饰器
# def timmer(f):
#     # f = index
#     def inner(*args,**kwargs):
#         #  函数的定义：* 聚合  args = ('李舒淇',18)
#         start_time = time.time()
#         # print(f'这是个f():{f()}!!!') # index()
#         r = f(*args,**kwargs)
#         # 函数的执行：* 打散：f(*args) --> f(*('李舒淇',18))  --> f('李舒淇',18)
#         end_time = time.time()
#         print(f'测试本函数的执行效率{end_time-start_time}')
#         return r
#     return inner
#
# @timmer # index = timmer(index)
# def index(name):
#     '''有很多代码.....'''
#     time.sleep(0.6) # 模拟的网络延迟或者代码效率
#     print(f'欢迎{name}登录博客园首页')
#     return 666
# index('纳钦')  # inner('纳钦')

# @timmer
# def dariy(name,age):
#     '''有很多代码.....'''
#     time.sleep(0.5) # 模拟的网络延迟或者代码效率
#     print(f'欢迎{age}岁{name}登录日记页面')
# dariy('李舒淇',18)  # inner('李舒淇',18)


# 标准版的装饰器；

# def wrapper(f):
#     def inner(*args,**kwargs):
#         '''添加额外的功能：执行被装饰函数之前的操作'''
#         ret = f(*args,**kwargs)
#         ''''添加额外的功能：执行被装饰函数之后的操作'''
#         return ret
#     return inner

