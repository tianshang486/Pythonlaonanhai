# 封闭的东西： 保证数据的安全。

# 方案一：
# l1 = []  # 全局变量 数据不安全
# li = []
# def make_averager(new_value):
#     l1.append(new_value)
#     total = sum(l1)
#     averager = total/len(l1)
#     return averager
# print(make_averager(100000))
# print(make_averager(110000))
# # 很多代码.....
# l1.append(666)
# print(make_averager(120000))
# print(make_averager(90000))

# 方案二： 数据安全，l1不能是全局变量。
# 每次执行的时候，l1列表都会重新赋值成[]
# li = []
# def make_averager(new_value):
#     l1 = []
#     l1.append(new_value)
#     total = sum(l1)
#     averager = total/len(l1)
#     return averager
# print(make_averager(100000))
# print(make_averager(110000))
# # 很多代码.....
# print(make_averager(120000))
# print(make_averager(90000))

# 方案三： 闭包

#
def make_averager():
    l1 = []
    def averager(new_value):
        l1.append(new_value)
        print(l1)
        total = sum(l1)
        return total/len(l1)
    return averager

# avg = make_averager()  # averager
# print(avg(100000))
# print(avg(110000))
# print(avg(120000))
# print(avg(190000))

# def func():
#     return 666
#
# ret = func()
# print(globals())

# 闭包： 多用于面试题： 什么是闭包？ 闭包有什么作用。
# 1，闭包只能存在嵌套函数中。
# 2， 内层函数对外层函数非全局变量的引用（使用），就会形成闭包。
# 被引用的非全局变量也称作自由变量，这个自由变量会与内层函数产生一个绑定关系，
# 自由变量不会再内存中消失。
# 闭包的作用：保证数据的安全。

# 如何判断一个嵌套函数是不是闭包

# 1，闭包只能存在嵌套函数中。
# 2， 内层函数对外层函数非全局变量的引用（使用），就会形成闭包。
# 例一：
# def wrapper():
#     a = 1
#     def inner():
#         print(a)
#     return inner
# ret = wrapper()

#
# # 例二：
# a = 2
# def wrapper():
#     def inner():
#         print(a)
#     return inner
# ret = wrapper()


# # 例三：
#   也是闭包！
# def wrapper(a,b):
#     def inner():
#         print(a)
#         print(b)
#     return inner
# a = 2
# b = 3
# ret = wrapper(a,b)
# print(ret.__code__.co_freevars)  # ('a', 'b')
# 如何代码判断闭包？

def make_averager():
    l1 = []
    def averager(new_value):
        l1.append(new_value)
        print(l1)
        total = sum(l1)
        return total/len(l1)
    return averager

avg = make_averager()  # averager
print(avg.__code__.co_freevars)