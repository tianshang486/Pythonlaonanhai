# class Course:
#     def __init__(self,name,price,period):
#         self.name = name
#         self.price = price
#         self.period = period
#     def __str__(self):
#         return self.name
# python = Course('python',21800,'6 months')
# linux = Course('linux',19800,'5 months')
# mysql = Course('mysql',12800,'3 months')
# go = Course('go',15800,'4 months')
# print(go)

# for index,c in enumerate(lst,1):
#     print(index,c)
# num = int(input('>>>'))
# course = lst[num-1]
# print('恭喜您选择的课程为 %s  价格%s元'%(course.name,course.price))

# class clas:
#     def __init__(self):
#         self.student = []
#     def append(self,name):
#         self.student.append(name)
#     def __str__(self):
#         return str(self.student)
#
# py22 = clas()
# py22.append('大壮')
# print(py22)
# print(str(py22))
# print('我们py22班 %s'%py22)
# print(py22)
# py22.append('大壮')
# print(py22)

# 在打印一个对象的时候 调用__str__方法
# 在%s拼接一个对象的时候 调用__str__方法
# 在str一个对象的时候 调用__str__方法

class clas:
    def __init__(self):
        self.student = []
    def append(self,name):
        self.student.append(name)
    def __repr__(self):
        return str(self.student)
    def __str__(self):
        return 'aaa'

py22 = clas()
py22.append('大壮')
print(py22)
print(str(py22))
print('我们py22班 %s'%py22)
print('我们py22班 %r'%py22)
print(repr(py22))
# 当我们打印一个对象 用%s进行字符串拼接 或者str(对象)总是调用这个对象的__str__方法
# 如果找不到__str__,就调用__repr__方法
# __repr__不仅是__str__的替代品,还有自己的功能
# 用%r进行字符串拼接 或者用repr(对象)的时候总是调用这个对象的__repr__方法
