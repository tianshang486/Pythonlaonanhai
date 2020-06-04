# def meet():
#     print('打开tantan')
#     print('进行筛选：性别：女')
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话....')
#     print('约....走起...')
#
# s1 = 'jfdsklafjsda'
# l1 = [1,2,3]
# len(s1)

# 函数的传参：让函数封装的这个功能，盘活。
# 实参，形参。

# def meet(sex):  #函数的定义：接受的参数形式参数
#     print('打开tantan')
#     print('进行筛选：性别：%s' %(sex))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话....')
#     print('约....走起...')
#
# meet('男')  # 函数的执行传的参数 ：实际参数

# 函数的传参：实参，形参
# 实参角度：
# 1.位置参数: 从左至右，一一对应。
# def meet(sex,age,skill):
#     print('打开tantan')
#     print('进行筛选：性别：%s,年龄：%s,%s' %(sex,age,skill))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话....')
#     print('约....走起...')
#
# meet('女',25,'python技术好的',)
#
# 写一个函数，只接受两个int的参数，函数的功能是将较大的数返回。
# def compile(a,b):
#     c = 0
#     if a > b:
#         return c
#     else:
#         return c
# print(compile(10,20))
# print(compile(1000,1))
# compile(1000,20)
#
# 三元与运算符： 简单的if else
# a = 1000
# b = 2000
# if a > b:
#     c = a
# else:
#     c = b
# print(c)
#
# a = 1000
# b = 2000
# c = a if a > b else b
# def complie(a,b):
#     # c = a if a > b else b
#     # return c
#     return a if a > b else b
#
# 2. 关键字参数
# 一一对应
# def meet(sex,age,skill,hight,weight,):
#     print('打开tantan')
#     print('进行筛选：性别：%s,年龄：%s,技术：%s,身高：%s,体重%s' %(sex,age,skill,hight,weight))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话....')
#     print('约....走起...')
#
# meet(age=25,weight=100,hight=174,skill='python技术好的',sex='女')
#
# 函数：传入两个字符串参数，将两个参数拼接完成后形成的结果返回。
# def func(a,b):
#     return a + b
# print(func(b='太白',a='无敌'))
# 混合参数
# 位置参数一定要在关键字参数的前面。
def meet(sex,age,skill,hight,weight,):
    print('打开tantan')
    print('进行筛选：性别：%s,年龄：%s,技术：%s,身高：%s,体重%s' %(sex,age,skill,hight,weight))
    print('左滑一下')
    print('右滑一下')
    print('找美女')
    print('悄悄话....')
    print('约....走起...')
    return '筛选结果：性别：%s,体重%s' %(sex,weight)

print(meet('女',25,weight=100,hight=174,skill='python技术好的'))
'''
实参角度：
    1. 位置参数 按照顺序，一一对应
    2. 关键字参数， 一一对应
    3. 混合参数：位置参数一定要在关键字参数的前面。
'''

# 形参角度：
# 1，位置参数 与实参角度的位置参数是一种。

# def meet(sex,age,skill):
#     print('打开tantan')
#     print('进行筛选：性别：%s,年龄：%s,%s' %(sex,age,skill))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话....')
#     print('约....走起...')
#
# meet('女',25,'python技术好的',)
#
# 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func(l):
#     if len(l) > 2:
#         return l[:2]
#     else:
#         return l
# # print(func([1,2,3,4,5]))
# print(func([1,]))
#
# def func(l):
#     c = l[:2] if len(l) > 2 else l
#     return c
# print(func([1,2,3,4,5]))
# print(func([1,]))
#
# def func(l):
#     return l[:2]
# # l1 = [1,]
# # print(l1[:2])

# 默认值参数
# 默认参数设置的意义：普遍经常使用的。
#
# def meet(age,skill='python技术好的',sex='女',):
#     print('打开tantan')
#     print('进行筛选：性别：%s,年龄：%s,技能：%s' %(sex,age,skill))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话....')
#     print('约....走起...')
#
# # meet(25,'python技术好的',)
# meet(25,'运维技术好的','男')
#
# open()

# 形参角度：
# 1. 位置参数
# 2. 默认参数  （经常使用的参数）
