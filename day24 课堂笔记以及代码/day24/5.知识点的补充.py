# object类 类祖宗
# 所有在python3当中的类都是继承object类的
# object中有init
# 所有的类都默认的继承object

# class A(object):
#     pass
# a = A()
# 开空间
# 调用init

# class A:pass
# print(A.__bases__)
# class C:pass
# class B(A,C):pass
# print(B.__bases__)

# 绑定方法和普通的函数
from types import FunctionType,MethodType
# FunctionType : 函数
# MethodType : 方法

# isinstance type
# a = 1
# b = 'abc'
# print(isinstance(a,int))
# print(isinstance(a,float))
# print(isinstance(b,str))

# a = 1
# b = 'abc'
# print(type(a) is int)
# print(type(b) is str)


# class Cat:
#     pass
# 小白 = Cat()
# print(type(小白) is Cat)
# print(isinstance(小白,Cat))

# class Animal:pass
# class Cat(Animal):pass
# 小白 = Cat()
# print(type(小白) is Cat)
# print(type(小白) is Animal)
# print(isinstance(小白,Cat))
# print(isinstance(小白,Animal))

# from types import FunctionType,MethodType
# # FunctionType : 函数
# # MethodType : 方法
# class A:
#     def func(self):
#         print('in func')
#
# print(A.func)  # 函数
# a = A()
# print(a.func)  # 方法
# print(isinstance(a.func,FunctionType))
# print(isinstance(a.func,MethodType))
# print(isinstance(A.func,FunctionType))
# print(isinstance(A.func,MethodType))


# class A:
#     role = '法师'
#     def func1(self):pass
#     def func2(self):pass
# class B:pass
# class C(B,A):pass
# print(A.__base__)
# print(C.__base__)
# print(C.__bases__)
# print(A.__dict__)
# print(A.__name__)
# print(A.__class__)
# print(B.__class__)
# print(C.__class__)
# print(C.__module__)
# import module

# __doc__
# def func():
#     '''
#     这个函数主要是用来卖萌
#     :return:
#     '''
#     pass

# print(func.__doc__)

# class Cat:
#     '''
#     这个类是用来描述游戏中的猫咪角色
#     '''
#     pass
# print(Cat.__doc__)