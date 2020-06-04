"""
datetime:日期时间模块

封装了一些和日期,时间相关的类.

date
time
datetime
timedelta
"""
import datetime
# date类:
# d = datetime.date(2010,10,10)
# print(d)
# # 获取date对象的各个属性
# print(d.year)
# print(d.month)
# print(d.day)

# time类:
# t = datetime.time(10,48,59)
# print(t)
# # time类的属性
# print(t.hour)
# print(t.minute)
# print(t.second)

# datetime
# dt = datetime.datetime(2010,11,11,11,11,11)
# print(dt)

# datetime中的类,主要是用于数学计算的.
# timedelta:时间的变化量
# td = datetime.timedelta(days=1)
# # print(td)
# # 参与数学运算
# # 创建时间对象:
# # 只能和以下三类进行数学运算: date,datetime,timedelta
# d = datetime.date(2010,10,10)
# res = d - td
# print(res)

# 时间变化量的计算是否会产生进位?
# t = datetime.datetime(2010,10,10,10,10,00)
# td = datetime.timedelta(seconds=3)
# res = t - td
# print(res)

# 练习:计算某一年的二月份有多少天.
# 普通算法:根据年份计算是否是闰年.是:29天,否:28
# 用datetime模块.
# 首先创建出指定年份的3月1号.然后让它往前走一天.
year = int(input("输入年份:"))
# 创建指定年份的date对象
d = datetime.date(year,3,1)
# 创建一天 的时间段
td = datetime.timedelta(days=1)
res = d - td
print(res.day)

# 和时间段进行运算的结果 类型:和另一个操作数保持一致
# d = datetime.date(2010,10,10)
# d = datetime.datetime(2010,10,10,10,10,10)
# d = datetime.timedelta(seconds=20)
# td = datetime.timedelta(days=1)
# res = d + td
# print(type(res))

