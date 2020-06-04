# 定义一个圆形类,半径是这个圆形的属性,实例化一个半径为5的圆形,一个半径为10的圆形
# 完成方法
        # 计算圆形面积
        # 计算圆形周长
# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         return pi * self.r ** 2
#     def perimeter(self):
#         return pi * self.r * 2
# c = Circle(5)
# print(c.r)
# print(c.area())
# print(c.perimeter())
#
# c.r = 10
# print(c.area())
# print(c.perimeter())

# 定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码
        # 登陆成功之后才创建用户对象
        # 设计一个方法 修改密码
import os
def login(name,passwd,filepath = 'userinfo'):
    with open(filepath,encoding='utf-8') as f:
        for line in f:
            user,pwd = line.strip().split('|')
            if user == name and passwd == pwd:
                return True
        else:
            return False

class User:
    def __init__(self,username,password):
        self.user = username
        self.pwd = password

    def change_pwd(self):
        oldpwd = input('输入原密码 :')
        newpwd = input('输入新密码 :')
        flag = False
        with open('userinfo',encoding='utf-8') as f1,open('userinfo.bak',mode='w',encoding='utf-8') as f2:
            for line in f1:
                username,password = line.strip().split('|')
                if username == self.user and password == oldpwd:
                    line = '%s|%s\n'%(username,newpwd)
                    flag = True
                f2.write(line)
        os.remove('userinfo')
        os.rename('userinfo.bak','userinfo')
        return flag
name = input('user : ')
passwd = input('pwd : ')
ret = login(name,passwd)
if ret:
    print('登录成功')
    obj = User(name,passwd)
    res = obj.change_pwd()
    if res:print('修改成功')











