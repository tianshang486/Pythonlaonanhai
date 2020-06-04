# 组合
    # 一个类的对象是另外一个类对象的属性

# 学生类
    # 姓名 性别 年龄 学号 班级 手机号
# 班级信息
    # 班级名字
    # 开班时间
    # 当前讲师
# class Student:
#     def __init__(self,name,sex,age,number,clas,phone):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.number = number
#         self.clas = clas
#         self.phone = phone
# class Clas:
#     def __init__(self,cname,begint,teacher):
#         self.cname = cname
#         self.begint = begint
#         self.teacher = teacher

# 查看的是大壮的班级的开班日期是多少
# 查看的是雪飞的班级的开班日期是多少
# py22 = Clas('python全栈22期','2019-4-26','小白')
# py23 = Clas('python全栈23期','2019-5-28','宝元')
# 大壮 = Student('大壮','male',18,27,py23,13812012012)
# 雪飞 = Student('雪飞','male',18,17,py22,13812012013)
# print(大壮.clas,py23)
# print(py23.begint)
# print(大壮.clas.begint)



# 练习 :
# 对象变成了一个属性
# 班级类
    # 包含一个属性 - 课程
# 课程
    # 课程名称
    # 周期
    # 价格

# 创建两个班级 linux57
# 创建两个班级 python22
# 查看linux57期的班级所学课程的价格
# 查看python22期的班级所学课程的周期

class Clas:
    def __init__(self,cname,begint,teacher):
        self.cname = cname
        self.begint = begint
        self.teacher = teacher
class Course:
    def __init__(self,name,period,price):
        self.name = name
        self.period = period
        self.price = price
py22 = Clas('python全栈22期','2019-4-26','小白')
linux57 = Clas('linux运维57期','2019-3-27','李导')
linux58 = Clas('linux运维58期','2019-6-27','李导')
python = Course('python','6 months',21800)
linux = Course('linux','5 months',19800)
py22.course = python
linux57.course = linux
linux58.course = linux
print(py22.course.period)
print(linux57.course.price)
linux.price = 21800
print(linux57.course.price)
print(linux58.course.price)

# class Clas:
#     def __init__(self,cname,begint,teacher,cprice,cperiod):
#         self.cname = cname
#         self.begint = begint
#         self.teacher = teacher
#         self.cprice = cprice    # 课程价格
#         self.cperiod = cperiod  # 课程周期
# linux57 = Clas('linux运维57期','2019-3-27','李导',19800,'5 months')
# linux58 = Clas('linux运维58期','2019-3-27','李导',19800,'5 months')
# linux59 = Clas('linux运维59期','2019-3-27','李导',19800,'5 months')
# linux60 = Clas('linux运维60期','2019-3-27','李导',19800,'5 months')
# linux61 = Clas('linux运维51期','2019-3-27','李导',19800,'5 months')
# linux57.cprice = 21800
# linux58.cprice = 21800