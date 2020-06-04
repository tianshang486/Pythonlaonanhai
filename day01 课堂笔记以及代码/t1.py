# print('hello 老铁')

# print(1+2+3+4+5)
# print((1+2+3+4+5)*3/2)
# print((((1+2+3+4+5)*3/2)+100)/24)

x = 1+2+3+4+5
y = x*3/2
z = (y + 100) / 24
# print(x,y,z)

# x,y,z 变量

# 变量练习；
'''
x8 = 100  # True
b__ = 12  # True
4g = 32  # False
_ = 11  # True
*r = 12  # False
r3t4 = 10  # True
t_ = 66  # True
'''
# 变量的小高级：
age1 = 18
age2 = age1
age3 = age2
age2 = 12
# print(age1,age2,age3)  # 18 12 18 


# 常量
# 约定俗成不能改变
NAME = '太白'
# print(NAME)


# 基础数据类型
# int
'''
i = 100
i1 = 2
i2 = i*i1
print(i2)
'''


# str:
s1 = 'day01'
s2 = "Python22期"
s2 = '''Python22期'''

# 单双引号可以配合使用

# content = 'I am taibai, 18 year old'
# content = "I'm taibai, 18 year old"

# 三引号：换行的字符串
msg = '''
今天我想写首小诗，
歌颂我的同桌，
你看他那乌黑的短发，
好像一只炸毛鸡。
'''
# print(msg)

# str 可以否加减乘除? + *
# str + str  *** 字符串的拼接
s1 = 'alex'
s2 = 'sb'
# print(s1 + s2)


# str * int
# s1 = '坚强'
# print(s1*8)

# bool : True False
# print(2 > 1)
# print(3 < 1)
# print(True)
# print('True')

# s1 = '100'
# s2 = 100
# print(s1,type(s1))
# print(s2,type(s2))


# input: 出来的全部都是字符串类型。
'''
username = input('请输入用户名：')
password = input('请输入密码：')
print(username,type(username))
print(password,type(password))
'''
# 让用户输入姓名，年龄，性别，然后打印一句话'我叫： ，今年：，性别：'
'''
name = input('请输入姓名：')
age = input('请输入年龄：')
sex = input('请输入性别：')
msg = '我叫： ' + name + '，今年：' + age + '，性别：' + sex
print(msg)
'''

# if 

# 单独if
'''
print(111)
if 2 < 1:
    print(666)
    print(333)
print(222)
'''

# if else
'''
s1 = '100'
i1 = int(s1)
print(i1,type(l1))


age = input('请输入年龄：')
if int(age) > 18:
    print('恭喜你，成年了')
else:
    print('小屁孩儿')
'''

# if elif elif .... 多选一
'''
num = int(input('猜点数：'))

if num == 1:
    print('晚上请你吃饭')
elif num == 3:
    print('一起溜达')
elif num == 2:
    print('请你大宝剑')
'''
	
# if elif elif .... else 多选一
'''
num = int(input('猜点数：'))

if num == 1:
    print('晚上请你吃饭')
	
elif num == 3:
    print('一起溜达')
	
elif num == 2:
    print('请你大宝剑')
else:
    print('太笨了....')

print('组合')
'''


# 嵌套的if
'''
if 条件:
    if 条件：
	    if


username = input('请输入用户名：')
password = input('请输入密码：')
code = 'qwer'
your_code = input('请输入验证码：')

if your_code == code:
    if username == 'taibai' and password == '123':
	    print('登录成功')
    else:
	    print('账号或者密码错误')
else:
    print('验证码错误')


score = int(input("输入分数:"))

if score > 100:
    print("我擦，最高分才100...")
elif score >= 80:
    print("B")
elif score >= 90:
    print("A")
elif score >= 60:
    print("C")
elif score >= 40:
    print("D")
else:
    print("太笨了...E")

'''



