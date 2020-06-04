# 8点之前 统计作业完成度,难点
# 作业笔记
    # 写每一个题的用时
    # 遇到的问题
    # 解决思路


#第一大题 : 读程序,标出程序的执行过程,画出内存图解,说明答案和为什么
# 请不要想当然,执行之后检查结果然后再确认和自己的猜想是不是一致
(1)
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

(2)
class A:
    Country = ['中国']     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
a.Country[0] = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

(3)
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
        self.Country = country
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

(4)
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def Country(self):
        return self.Country

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
print(a.Country)
print(a.Country())

# 第二大题:基于圆形类实现一个圆环类,要求接收参数 外圆半径和内圆半径
# 完成方法 :计算环形面积和环形周长(公式自己上网查)
# 要求,借助组合,要求组合圆形类的对象完成需求

# 第三大题:继续完成计算器和优化工作