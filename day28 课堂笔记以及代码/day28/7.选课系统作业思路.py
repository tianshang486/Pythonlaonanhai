class Student(object):
    def __init__(self,name):
        self.name = name

class Course(object):
    def __init__(self,name,price,period,teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher   # 老师只写一个姓名

class Admin(object):
    def __init__(self,name):
        self.name = name

# 管理员登录  admin 123
# 创建 学生(让用户输入学生信息,然后实例化,然后写到文件里)
#      课程(让用户输入课程信息,然后实例化,然后写到文件里)
# 学生可以选多门课程 怎么存呢?
# 学生只要选课 - 文件修改(麻烦)

# 用上反射就简单
# 能不能 不管是学生登录 还是管理员登录 这个地方不要用if else -- 进阶需求

from 模块 import 一个类
# import sys
# getattr(sys.modules[__name__],'名字') 反射本模块中的内容