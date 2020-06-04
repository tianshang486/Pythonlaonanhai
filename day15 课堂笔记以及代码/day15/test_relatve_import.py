"""
测试相对导入
"""
import os
import sys

# 把项目所在的父路径加到sys.path中
sys.path.append(os.path.dirname(__file__))

from xx.y import yy
print(yy.age2)
yy.f2()

# print(yy.zz.age)
# yy.zz.f()

print(yy.age)
yy.f()






