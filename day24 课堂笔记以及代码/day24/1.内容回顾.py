# class A:
#     Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
#     def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#     def Country(self):
#         return self.Country
#
# a = A('alex',83,'印度')
# b = A('wusir',74,'泰国')
# print(a.Country)
# print(a.Country())

# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#
#     def area(self):
#         return 3.14*self.r**2
#
#     def perimeter(self):
#         return 2*3.14*self.r
#
# class Ring:
#     def __init__(self,outer_r,inner_r):
#         outer_r,inner_r = (outer_r,inner_r) if outer_r > inner_r else (inner_r,outer_r)
#         self.out_c  = Circle(outer_r)
#         self.in_c = Circle(inner_r)
#
#     def area(self):
#         return self.out_c.area() - self.in_c.area()
#
#     def perimeter(self):
#         return self.out_c.perimeter() + self.in_c.perimeter()
#
# r = Ring(10,8)
#
# class Ring:
#     def __init__(self,outer_r,inner_r):
#         outer_r,inner_r = (outer_r,inner_r) if outer_r > inner_r else (inner_r,outer_r)
#         self.out_c  = outer_r
#         self.in_c = inner_r
#
#     def area(self):
#         return self.out_c**2 *3.14 - self.in_c**2 *3.14
#
#     def perimeter(self):
#         return self.out_c*2 *3.14  +  self.in_c*2 *3.14
#
# r = Ring(10,8)
# 1.传递的半径大小的顺序问题
# 2.为什么要用组合

# 程序里有两个需求 :和圆形相关  和环形相关  求环形相关的内容的时候用到了圆形的公式
# 圆柱形类 圆锥形类

# 命名空间
    # 在类的命名空间里 : 静态变量 绑定方法
    # 在对象的命名空间里 : 类指针 对象的属性(实例变量)

    # 调用的习惯
        # 类名.静态变量
        # 对象.静态变量 (对象调用静态变量的时候,不能对变量进行赋值操作 对象.静态变量 = 1UI27)

        # 绑定方法
        # 对象.绑定方法() # ==> 类名.绑定方法(对象)

        # 对象.实例变量
# 组合
    # 一个类的对象是另一个类对象的属性
    # 两个类之间 有 什么有什么的关系 : 班级有学生 学生有班级 班级有课程 图书有作者 学生有成绩

    # 学生 和 课程
    # 班级 和 课程
    # 圆形 和 圆环