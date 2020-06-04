#名称空间；命名空间。

# a = 1
# b = 2
# def func():
#     f = 5
#     print(f)
# c = 3
# func()

# 内置名称空间：python源码给你提供的一些内置的函数，print input
# print(666)
# python分为三个空间：
    # 内置名称空间（builtins.py）
    # 全局名称空间（当前py文件）
    # 局部名称空间（函数，函数执行时才开辟）

# 加载顺序：
# 内置名称空间 ---> 全局名称空间  ----> 局部名称空间（函数执行时）
# def func():
#     pass
# func()
# a = 5
# print(666)

# 取值顺序（就近原则） 单向不可逆
# LEGB原则
# input = '太白金星'
def func():
    # input = 'alex'
    print(input)
# func()

# （从局部找时）局部名称空间  ---> 全局名称空间  --->  内置名称名称空间


# input = '太白金星'
# def func():
#     input = 'alex'
#
# func()
# print(input)

# 作用域：
# 两个作用域：
    # 全局作用域 ：内置名称空间 全局名称空间
    # 局部作用域：局部名称空间

#  局部作用域可以引用全局作用域的变量
# date = '周五'
# def func():
#     a = 666
#     print(date)
# print(a)
# func()
# print(a)

# 局部作用域不能改变全局变量。
# count = 1
# # def func():
# #     count += 2
# #     print(count)
# # func()  # local variable 'count' referenced before assignment
# 局部作用域不能改变全局作用域的变量，当python解释器读取到局部作用域时，发现了你对一个变量进行修改的操作，
# 解释器会认为你在局部已经定义过这个局部变量了，他就从局部找这个局部变量，报错了。

# 使用可以，不能改变
# def func():
#     count = 1
#     def inner():
#         print(count)
#     inner()
# func()

def func():
    count = 1
    def inner():
        count += 1
        print(count)
    inner()
func()







