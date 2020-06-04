"""
本文件：研究内置函数：globals locals
"""
a = 1
b = 2
def func():
    name = 'alex'
    age = 73
    print(globals())  # 返回的是字典：字典里面的键值对：全局作用域的所有内容。
    print(locals())  # 返回的是字典：字典里面的键值对：当前作用域的所有的内容。
# print(globals())  # 返回的是字典：字典里面的键值对：全局作用域的所有内容。
# print(locals())  # # 返回的是字典：字典里面的键值对：当前作用域的所有的内容。
func()