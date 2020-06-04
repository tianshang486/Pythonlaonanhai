# from tbjx import name
# from tbjx import read1
# from tbjx import read2
# print(name)
# print(globals())
# read1()

# 1, 容易产生冲突,后者将前者覆盖
# name = 'alex'
# from tbjx import name
# print(name)

#  当前位置直接使用read1和read2,执行时，仍然以tbjx.py文件全局名称空间
# from tbjx import read1
#
# def read1():
#     print(666)

# name = '大壮'
# read1()
# print(globals())

#
# from tbjx import change
# name = 'Alex'
# print(name)  # 'Alex'
# change()  # 'barry'
# from tbjx import name
# print(name)


'''
tbjx.py 部分代码: 
name = '太白金星'

def read1():
    print('tbjx模块：', name)

'''


# from tbjx import name
# from tbjx import read1
# from tbjx import read2

# 例题1:
# name = 'alex'
# print(name)
# name = 'alex'
# from tbjx import name
# print(name)
# print(globals())

#
# from tbjx import read1
# name = 'alex'
# read1()
name = 'alex'
def read1():
    print(666)

# from tbjx import *
# # 一般千万别么这写,必须要将这个模块中的所有名字全部记住
# # 但是可以配合一个变量使用
#
# print(name)
# read1()
#
# read2()

# from tbjx import read2
# read2()

# import tbjx


# 模块的搜索路径:
# import tbjx
# print(tbjx.name)

# import dz
# print(dz.name)

# 搜索的路径:
# import sm
import abc
# python 解释器会自动将一些内置内容(内置函数,内置模块等等)加载到内存中
import sys
# print(sys.modules)  # 内置内容(内置函数,内置模块等等)
import time

# print(sys.path)
#['D:\\python_22\\day17', 'C:\\Python\\Python36\\python36.zip', 'C:\\Python\\Python36\\DLLs', 'C:\\Python\\Python36\\lib', 'C:\\Python\\Python36', 'C:\\Python\\Python36\\lib\\site-packages']
# 'D:\\python_22\\day17' 路径是当前执行文件的相对路径
# import tbjx

# 我就想找到dz 内存没有,内置中,这两个你左右不了,sys.path你可以操作.
import sys
sys.path.append(r'D:\python_22\day16')
# sys.path 会自动将你的 当前目录的路径加载到列表中.
import dz

# 如果你想要引用你自定义的模块:
# 要不你就将这个模块放到当前目录下面,要不你就手动添加到sys.path





