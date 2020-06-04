# class Foo(object):
#     def __init__(self, num):
#         self.num = num
#
# v1 = [Foo for i in range(10)]      # 10个类的地址
# v2 = [Foo(5) for i in range(10)]   # 10个不同的对象的地址
# v3 = [Foo(i) for i in range(10)]   # 10个不同的对象的地址
#
# print(v1)
# print(v2)
# print(v3)

# obj1 = Foo(10)
# print(obj1)
# obj2 = Foo(10)
# print(obj2)


# Person1  Person2
# name = name
# age = age

# class Person(object):
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#     def __eq__(self, other):   # 两个对象作比较的时候会自动调用这个方法
#         return self.name == other.name and self.age == other.age
#     def __gt__(self, other):
#         print('执行gt啦')
#     def __lt__(self, other):
#         print('执行lt啦')
# alex = Person('alex',83)
# alex222 = Person('alex',84)
# print('-'*20)
# print(alex == alex222)
#     # == 符号刚好会调用alex对象对应的类的__eq__方法,alex222会被当做other参数传入方法
#     # alex == alex222的结果就是__eq__方法的返回值
# print('*'*20)
# # print(alex is alex222)
# alex<alex222
# alex>alex222