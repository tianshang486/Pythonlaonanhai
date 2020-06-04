# def func():
#     print(666)
#
# # func()
# # 1. 函数名指向的是函数的内存地址。
# # 函数名 + ()就可以执行次函数。
# # a = 1
# # a()
# # func()
# # a = {'name': 'alex'}
# # b = {'age' : 18}
# # a = 1
# # b = 2
# # print(a + b)
# print(func,type(func))  # <function func at 0x000001BA864E1D08>
# func()

# 2, 函数名就是变量。
# def func():
#     print(666)

# a = 2
# b = a
# c = b
# print(c)
# f = func
# f1 = f
# f2 = f1
# f()
# func()
# f1()
# f2()
#
# def func():
#     print('in func')
#
# def func1():
#     print('in func1')
#
# func1 = func
# func1()
# a = 1
# b = 2
# a = b
# print(a)

# 3. 函数名可以作为容器类数据类型的元素

# def func1():
#     print('in func1')
#
# def func2():
#     print('in func2')
#
# def func3():
#     print('in func3')
# # a = 1
# # b = 2
# # c = 3
# # l1 = [a,b,c]
# # print(l1)
# l1 = [func1,func2,func3]
# for i in l1:
#     i()

# 4. 函数名可以作为函数的参数

# def func(a):
#     print(a)
#     print('in func')
# b = 3
# func(b)
# print(func)

# def func():
#     print('in func')
#
# def func1(x):
#     x()  # func()
#     print('in func1')
#
# func1(func)

# 5. 函数名可以作为函数的返回值
def func():
    print('in func')

def func1(x): # x = func
    print('in func1')
    return x

ret = func1(func)  # func
ret()  # func()
