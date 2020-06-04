# 面向对象的回顾
# 类
# class 类名:
#     静态变量 = '值'
#     def 函数(self):
#         '函数体的内容'
#         pass
# 所有的变量和函数的地址都存储在类的命名空间里

# 对象
    # 对象 = 类名()
# 怎么用
    # 类能做什么用?
        # 1.实例化对象
        # 2.操作静态变量
    # 什么时候是对类中的变量赋值,或者去使用类中的变量
        # 类名.名字 = '值'
        # print(类名.名字)
        # print(对象名.名字) # 如果对象本身没有这个名字
    # 什么时候是对对象中的变量赋值
        # 对象.名字的时候
        # self.名字的时候
# class A:
#     role = []
#     def __init__(self):
#         self.l = []
#     def append(self,obj):
#         self.l.append(obj)
#     def pop(self,index=-1):
#         self.l.pop(index)
# print(A.role)
# a = A()

# class B:
#     def append(self):print('bbbb')
# class C:
#     def append(self):print('cccc')
# b = B()
# d = C()
# b.obj = []
# b.obj.append(1)
# b = B()
# b.append()
# c = B()
# c.append()
# d = C()
# d.append()

# class Queue:
#     def __init__(self):
#         self.lst = []
#     def append(self,value):
#         pass
#     def pop(self):
#         pass
#
# q = Queue()
# q.lst.append(10)
# q.append(5)
# print(q.lst)
# q.pop()
# print(q.lst)
# 所有的对象调用方法 就看这个对象是哪一个类的对象
# 不要担心所有的类的方法都是一样的名字,并不影响的

# 怎么继承
# class A:
#     def func(self):print('a')
# class B(A):
#     def func(self):print('b')
# A是父类,B是子类
# 写代码的时候,是先有的父类还是先有的子类?
    # 在加载代码的过程中 需要先加载父类 所以父类写在前面
    # 从思考的角度出发 总是先把子类都写完 发现重复的代码 再把重复的代码放到父类中
# b = B()
# b.func()   # b  自己有不用父类的

# 例2
# class A:
#     def func(self):print('a')
# class B(A):pass
# b = B()
# b.func()   # a  自己没有用父类的

# 例3
# class A:
#     def func(self):print('a')
# class B(A):
#     def func(self):
#         A.func(self)
#         print('b')
# b = B()
# b.func()     # a,b  先执行B.func,调用了A.func打印a,然后回到B.func打印b

# 例4
# class A:
#     def func(self):print('a')
# class B(A):
#     def func(self):
#         print('b')
#         A.func(self)
# b = B()
# b.func()     # b,a

# 例4
# class A:
#     lst = []
#     def func(self):
#         self.lst.append(1)
# class B(A):
#     lst = []
#     def func(self):
#         self.lst.append(2)
# b = B()
# b.func()
# print(A.lst)   # []
# print(B.lst)   #  [2]

# 例5
# class A:
#     lst = []
#     def func(self):
#         self.lst.append(1)
# class B(A):
#     def func(self):
#         self.lst.append(2)
# b = B()
# b.func()
# print(A.lst)   # [2]
# print(B.lst)   # [2]

# 例6
# class A:
#     lst = []
#     def __init__(self):
#         self.lst = []
#     def func(self):
#         self.lst.append(1)
# class B(A):
#     def __init__(self):
#         self.lst= []
#     def func(self):
#         self.lst.append(2)
# b = B()
# b.func()
# print(A.lst)  # []
# print(B.lst)  # []

# 栈 队列 默写
# mypickle 仿照这个类写一个myjson(可以dump多次,load多次)
# 所有的例子 把内存关系图画出来