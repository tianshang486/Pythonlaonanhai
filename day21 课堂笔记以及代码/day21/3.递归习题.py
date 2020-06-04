# 2.os模块:查看一个文件夹下的所有文件,这个文件夹下面还有文件夹,不能用walk
# 作业1 :
# outer-inner1
#      -inner2
# import os
# def show_file(path):
#     name_lst = os.listdir(path)
#     for name in name_lst:
#         abs_path = os.path.join(path,name)
#         if os.path.isfile(abs_path):
#             print(name)
#         elif os.path.isdir(abs_path):
#             show_file(abs_path)
#
# show_file('D:\python_22\day21')
# 3.os模块:计算一个文件夹下所有文件的大小.这个文件夹下面还有文件夹,不能用walk
# 4.计算斐波那契数列
    # 找第100个数
    # 1 1 2 3 5 8 13 21 34 55
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# ret= fib(100)
# print(ret)

# def fib(n,a=1,b=1):
#     if n == 1 or n == 2:
#         return b
#     else:
#         a,b = b,a+b
#         return fib(n-1,a,b)
# ret = fib(100)
# print(ret)

# def fib(n):
#     a,b = 1,1
#     while n>2:
#         a,b = b,a+b
#         n-=1
#     return b
# ret = fib(100)
# print(ret)

# def fib(n):
#     if n == 1:
#         yield 1
#     else:
#         yield from(1,1)
#         a,b = 1,1
#         while n>2:
#             a,b = b,a+b
#             yield b
#             n-=1
#
# for i in fib(4):
#     print(i)

# 5.三级菜单 可能是n级
    # 递归 循环
    # https://www.cnblogs.com/Eva-J/articles/7205734.html#_label4

# os
    # 文件和文件夹相关的
        # os.listdir
        # os.remove
        # os.rename
        # os.mkdir
        # os.rmdir
        # os.makedirs
        # os.removedirs
    # 和执行操作系统命令相关
        # os.popen/os.system
        # import os
        # os.system('dir')
        # ret = os.popen('dir')
        # print(ret.read())
    # 工作目录:在哪个文件下执行的这个py文件,哪一个目录就是你的工作目录
        # import os
        # os.chdir('D:\python_22\day21')
        # print('-->',os.getcwd())
        # open('s21day21tmp','w').close()
    # os.path
        # os.path.isfile
        # os.path.isdir
        # os.path.isexit

        # ps.path.basename  获取这个路径的最后一个值
            # D:\python_22\day21  --> day21
            # D:\python_22\day21\3.递归习题.py   --> 3.递归习题.py
        # os.path.dirname 获取这个路径的上一级目录
            # D:\python_22\day21  --> D:\python_22
            # D:\python_22\day21\3.递归习题.py --> D:\python_22\day21
        # os.path.split(path)
            # D:\python_22\day21\3.递归习题.py -->(D:\python_22\day21,3.递归习题.py)
        # os.path.join(dirname,basename)   跨平台的

        # os.path.getsize
        # oa.path.getmtime/getatimes

# sys 和python解释器交互的
    # sys.path 模块搜索路径
    # sys.argv 在运行python脚本的时候写在python命令后面的是啥,打印出来的就是啥
    # sys.modules 查看导入了哪些模块

# import sys
# if sys.argv[1] == 'alex' and sys.argv[2] == 'sb':
#     print('登录成功')
