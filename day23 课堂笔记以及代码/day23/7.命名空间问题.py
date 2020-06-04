# 类的成员和命名空间
# class A:
#     Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
#     def __init__(self,name,age):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#     def func1(self):
#         print(self)
#     def func2(self):pass
#     def func3(self):pass
#     def func4(self):pass
#     def func5(self):pass
#
# a = A('alex',83)
# print(a.name)
# print(a.Country)

# print(A.Country)
# a.func1() # == A.func1(a)

# class A:
#     Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
#     def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#         self.Country = country
#     def func1(self):
#         print(self)
#     def func2(self):pass
#     def func3(self):pass
#     def func4(self):pass
#     def func5(self):pass
#
# a = A('alex',83,'印度')
# print(a.name)
# print(a.Country)
# print(A.Country)

# class A:
#     Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
#     def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#         self.country = country
#     def func1(self):
#         print(self)
#     def func2(self):pass
#     def func3(self):pass
#     def func4(self):pass
#     def func5(self):pass
#
# a = A('alex',83,'印度')
# b = A('wusir',74,'泰国人')
# a.Country = '日本人'
# print(a.Country)
# print(b.Country)
# print(A.Country)

# class A:
#     Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
#     def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#     def func1(self):
#         print(self)
#     def func2(self):pass
#     def func3(self):pass
#     def func4(self):pass
#     def func5(self):pass
#
# a = A('alex',83,'印度')
# b = A('wusir',74,'泰国人')
# A.Country = '日本人'
# print(a.Country)
# print(b.Country)
# print(A.Country)

# 类中的变量是静态变量
# 对象中的变量只属于对象本身,每个对象有属于自己的空间来存储对象的变量
# 当使用对象名去调用某一个属性的时候会优先在自己的空间中寻找,找不到再去对应的类中寻找
# 如果自己没有就引用类的,如果类也没有就报错
# 对于类来说,类中的变量所有的对象都是可以读取的,并且读取的是同一份变量

# 实现一个类,能够自动统计这个类实例化了多少个对象
# class A:pass
# A.Country = 123   # 属性的增加
# print(A.Country)  # 查看或者引用

# class A:
#     count = 0
#     def __init__(self):
#         A.count += 1
#
# a1 = A()
# print(a1.count)
# a2 = A()
# print(A.count)
# 类中的静态变量的用处
# 如果一个变量 是所有的对象共享的值,那么这个变量应该被定义成静态变量
# 所有和静态变量相关的增删改查都应该使用类名来处理
# 而不应该使用对象名直接修改静态变量








