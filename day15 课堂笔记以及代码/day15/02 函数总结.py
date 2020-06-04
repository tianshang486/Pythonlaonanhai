# 仅限关键字参数。
# def func(a,b,*args,c):
#     print(a,b)
#     print(c)
# func(1,2,3,4,c=666)

# *
# a,b = (1,2)
# a,b,*c = (1,2,4,5,6,7,8)
# print(a,b,c)
#
# a,*b,c = [11,22,33,44,55,66,77]
# print(a,b,c)
# a,*b,c = range(10)
# print(a,b,c)

# def func():
#     global name
#     name = 'alex'
#
# print(name)
# func()

# name = '太白'
# def func():
#     global name
#     name = 'alex'
#
# print(name)
# func()
# print(name)
# print(name)
# print(name)
# print(name)

# def func():
#     name = '太白'
#     def inner():
#         nonlocal name
#         name = 'alex'
#     print(name)
#     inner()
#     print(name)
# func()
#
# name
# def func():
# #     pass
# # # func()

# def wrapper(a):
#     name = '太白'
#     def inner():
#         print(a)
#         print(name)
#     return inner
# ret = wrapper('烧饼')
# print(ret.__code__.co_freevars)

