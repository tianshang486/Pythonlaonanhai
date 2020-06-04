# def wrapper(f):
# 	def inner(*args,**kwargs):
# 		print(111)
# 		ret = f(*args,**kwargs)
# 		print(222)
# 		return ret
# 	return inner
#
# @wrapper  # func = wrapper(func)
# def func():
# 	print('in func')
# func()

# 编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’。


# def wrapper(f):
#     def inner(*args,**kwargs):
#         print('每次执行被装饰函数之前都得先经过这里')
#         ret = f(*args,**kwargs)
#         return ret
#     return inner
#
# @wrapper  # func = wrapper(func)
# def func():
#     print('in func')
# func()

# 为函数写一个装饰器，把函数的返回值 +100 然后再返回。
# def wrapper(f):  # f = func
#     def inner(*args,**kwargs):
#         ret = f(*args,**kwargs) # func()
#         # print(ret)
#         return ret + 100
#     return inner
#
# @wrapper  # func = wrapper(func)
# def func():
#     return 7
#
# result = func()  # inner()
# print(result)

# 请实现一个装饰器，通过一次调用是函数重复执行5次。

# def wrapper(f):
#     def inner(*args,**kwargs):
#         for i in range(5):
#             f(*args,**kwargs)
#     return inner
# @wrapper
# def func():
#     print('in func')
# func()  # inner()



# 请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中。
#
# 可用代码：
# import time
# struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time)) # 当前时间节点
#
# def wrapper():
#     pass
#
# def func1(f):
#     print(f.__name__)
# func1(wrapper)
# 函数名通过： 函数名.__name__获取。
import time
def wrapper(f):
    def inner(*args,**kwargs):
        with open('log',encoding='utf-8',mode='a') as f1:
            struct_time = time.localtime()
            f1.write(f'北京时间：{time.strftime("%Y-%m-%d %H:%M:%S",struct_time)}执行了 {f.__name__}函数\n')
        ret = f(*args,**kwargs)
        return ret
    return inner

@wrapper
def wcnb():
    print('in wcnb')
wcnb()
time.sleep(2)
wcnb()
time.sleep(1)
wcnb()