# 先来定义模子,用来描述一类事物
# 具有相同的属性和动作
# class Person:       # 类名
#     def __init__(self,name,sex,job,hp,weapon,ad):
#         # 必须叫__init__这个名字,不能改变的,所有的在一个具体的人物出现之后拥有的属性
#         self.name = name
#         self.sex = sex
#         self.job = job
#         self.level = 0
#         self.hp = hp
#         self.weapon = weapon
#         self.ad = ad
# #
# alex = Person('alex','不详','搓澡工',260,'搓澡巾',1)     # alex 就是对象  alex = Person()的过程 是通过类获取一个对象的过程 - 实例化
# print(alex,alex.__dict__)
# wusir = Person('wusir','male','法师',500,'打狗棍',1000)
# # print(wusir,wusir.__dict__)
# print(alex.name)   # print(alex.__dict__['name'])  属性的查看
# alex.name = 'alexsb'    # 属性的修改
# print(alex.name)
# alex.money = 1000000     # 属性的增加
# print(alex.money)
# print(alex.__dict__)
# del alex.money           # 属性的删除
# print(alex.__dict__)
# 类名() 会自动调用类中的__init__方法

# 类和对象之间的关系?
    # 类 是一个大范围 是一个模子 它约束了事物有哪些属性 但是不能约束具体的值
    # 对象 是一个具体的内容 是模子的产物 它遵循了类的约束 同时给属性赋上具体的值

# Person是一个类 :alex wusir都是这个类的对象
# 类有一个空间,存储的是定义在class中的所有名字
# 每一个对象又拥有自己的空间,通过对象名.__dict__就可以查看这个对象的属性和值


# d = {'k':'v'}
# print(d,id(d))
# d['k'] = 'vvvv'
# print(d,id(d))

# 修改列表\字典中的某个值,或者是对象的某一个属性 都不会影响这个对象\字典\列表所在的内存空间


# class Person:       # 类名
#     def __init__(self,n,s,j,h,w,a):
#         # 必须叫__init__这个名字,不能改变的,所有的在一个具体的人物出现之后拥有的属性
#         self.name = n
#         self.sex = s
#         self.job = j
#         self.level = 0
#         self.hp = h
#         self.weapon = w
#         self.ad = a
# 实例化所经历的步骤
    # 1.类名() 之后的第一个事儿 :开辟一块儿内存空间
    # 2.调用 __init__ 把空间的内存地址作为self参数传递到函数内部
    # 3.所有的这一个对象需要使用的属性都需要和self关联起来
    # 4.执行完init中的逻辑之后,self变量会自动的被返回到调用处(发生实例化的地方)

# dog类 实现狗的属性 名字 品种 血量 攻击力 都是可以被通过实例化被定制的
# class Dog():
#     def __init__(self,name,blood,aggr,kind):
#         self.dog_name = name
#         self.hp = blood
#         self.ad = aggr
#         self.kind = kind
#
# 小白 = Dog('小白',5000,249,'柴犬')
# print(小白.dog_name)
# print(小白.__dict__)



# 定义一个圆形类,半径是这个圆形的属性,实例化一个半径为5的圆形,一个半径为10的圆形
    # 完成方法
    # 计算圆形面积
    # 计算圆形周长
# 定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码








