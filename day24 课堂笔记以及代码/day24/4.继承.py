# 猫
    # 吃
    # 喝
    # 睡
    # 爬树
# 狗
    # 吃
    # 喝
    # 睡
    # 看家

# class Cat:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print('%s is eating'%self.name)
#     def drink(self):
#         print('%s is drinking'%self.name)
#     def sleep(self):
#         print('%s is sleeping'%self.name)
#     def climb_tree(self):
#         print('%s is climbing'%self.name)
#
# class Dog:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print('%s is eating'%self.name)
#     def drink(self):
#         print('%s is drinking'%self.name)
#     def sleep(self):
#         print('%s is sleeping'%self.name)
#     def house_keep(self):
#         print('%s house keeping'%self.name)

# 小白 = Cat('小白')
# 小白.eat()
# 小白.drink()
# 小白.climb_tree()

# 小黑 = Dog('小黑')
# 小黑.eat()
# 小黑.drink()
# 小黑.house_keep()

# 继承 -- 需要解决代码的重复
# 继承语法
# class A:
#     pass
# class B(A):
#     pass
# B继承A,A是父类,B是子类
# A是父类 基类 超类
# B是子类 派生类

# 子类可以使用父类中的 : 方法 静态变量
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print('%s is eating'%self.name)
#     def drink(self):
#         print('%s is drinking'%self.name)
#     def sleep(self):
#         print('%s is sleeping'%self.name)
# class Cat(Animal):
#     def climb_tree(self):
#         print('%s is climbing'%self.name)

# class Dog(Animal):
#     def house_keep(self):
#         print('%s house keeping'%self.name)

# 小白 = Cat('小白')
    # 先开辟空间,空间里有一个类指针-->指向Cat
    # 调用init,对象在自己的空间中找init没找到,到Cat类中找init也没找到,
    # 找父类Animal中的init
# 小白.eat()
# 小白.climb_tree()
# 小黑 = Dog('小黑')
# 小黑.eat()

# 当子类和父类的方法重名的时候,我们只使用子类的方法,而不会去调用父类的方法了
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print('%s is eating'%self.name)
#     def drink(self):
#         print('%s is drinking'%self.name)
#     def sleep(self):
#         print('%s is sleeping'%self.name)
#
# class Cat(Animal):
#     def eat(self):
#         print('%s吃猫粮'%self.name)
#
#     def climb_tree(self):
#         print('%s is climbing'%self.name)
#
# 小白 = Cat('小白')
# 小白.eat()


# 子类想要调用父类的方法的同时还想执行自己的同名方法
# 猫和狗在调用eat的时候既调用自己的也调用父类的,
# 在子类的方法中调用父类的方法 :父类名.方法名(self)
# class Animal:
#     def __init__(self,name,food):
#         self.name = name
#         self.food = food
#         self.blood = 100
#         self.waise = 100
#     def eat(self):
#         print('%s is eating %s'%(self.name,self.food))
#     def drink(self):
#         print('%s is drinking'%self.name)
#     def sleep(self):
#         print('%s is sleeping'%self.name)
#
# class Cat(Animal):
#     def eat(self):
#         self.blood += 100
#         Animal.eat(self)
#     def climb_tree(self):
#         print('%s is climbing'%self.name)
#         self.drink()
#
# class Dog(Animal):
#     def eat(self):
#         self.waise += 100
#         Animal.eat(self)
#     def house_keep(self):
#         print('%s is keeping the house'%self.name)
# 小白 = Cat('小白','猫粮')
# 小黑 = Dog('小黑','狗粮')
# 小白.eat()
# 小黑.eat()
# print(小白.__dict__)
# print(小黑.__dict__)

# 继承语法 class 子类名(父类名):pass
# 父类和子类方法的选择:
    # 子类的对象,如果去调用方法
    # 永远优先调用自己的
        # 如果自己有 用自己的
        # 自己没有 用父类的
        # 如果自己有 还想用父类的 : 直接在子类方法中调父类的方法 父类名.方法名(self)


# 思考一:下面代码的输出?
# class Foo:
#     def __init__(self):
#         self.func()   # 在每一个self调用func的时候,我们不看这句话是在哪里执行,只看self是谁
#
#     def func(self):
#         print('in foo')
#
# class Son(Foo):
#     def func(self):
#         print('in son')
#
# Son()

# 思考二: 如果想给狗和猫定制个性的属性
# class Animal:
#     def __init__(self,name,food):
#         self.name = name
#         self.food = food
#         self.blood = 100
#         self.waise = 100
#     def eat(self):
#         print('%s is eating %s'%(self.name,self.food))
#     def drink(self):
#         print('%s is drinking'%self.name)
#     def sleep(self):
#         print('%s is sleeping'%self.name)
# class Cat(Animal):
#     def __init__(self,name,food,eye_color):
#         Animal.__init__(self,name,food)    # 调用了父类的初始化,去完成一些通用属性的初始化
#         self.eye_color = eye_color         # 派生属性

# 猫 : eye_color眼睛的颜色
# 狗 : size型号
# 小白 = Cat('小白','猫粮','蓝色')
# print(小白.__dict__)

# 单继承
# class D:
#     def func(self):
#         print('in D')
# class C(D):pass
# class A(C):
#     def func(self):
#         print('in A')
# class B(A):pass
# B().func()

# 多继承 有好几个爹
    # 有一些语言不支持多继承 java
    # python语言的特点 : 可以在面向对象中支持多继承
# class B:
#     def func(self):print('in B')
# class A:
#      def func(self):print('in A')
#
# class C(B,A):pass
# C().func()

# 单继承
# 调子类的 : 子类自己有的时候
# 调父类的 : 子类自己没有的时候
# 调子类和父类的 :子类父类都有,在子类中调用父类的

# 多继承
# 一个类有多个父类,在调用父类方法的时候,按照继承顺序,先继承的就先寻找