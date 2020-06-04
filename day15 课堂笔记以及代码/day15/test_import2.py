"""
导入模块的多种方式：


"""

# 把自定义模块的路径添加到sys.path中
import os
import sys
sys.path.append(os.path.dirname(__file__) + '/aa')

# 使用import xxx 导入
# import my_module
# print(my_module.age)

# 使用from。。。import xxx的方式导入
# age = 1000
# from my_module import age
# print(age)

# 使用别名避免命名冲突
# from my_module import age as a
# age = 1000
# print(age)
# print(a)


# 给模块起别名
# import my_module as m
# print(m.age)
# m.f1()

# 验证__all__控制的成员
# from my_module import *

# 使用如下方式，可以绕过__all__的限制
# import my_module as m
#
# print(m.age)
# print(m.age2)
# print(m.age3)


