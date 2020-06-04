# 整理今天笔记，课上代码最少敲3遍。
#
# 用列表推导式做下列小题
#
# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
#
# 求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
#
# 求M中3,6,9组成的列表 M = [[1,2,3],[4,5,6],[7,8,9]]
# print([[i-2,i-1,i] for i in range(3,10,3)])
# M = [[1,2,3],[4,5,6],[7,8,9]]
# print([i[-1] for i in M])

# 求出50以内能被3整除的数的平方，并放入到一个列表中。
#
# 构建一个列表：['python1期', 'python2期', 'python3期', 'python4期',
# 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']

# 构建一个列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# print([(i,i+1) for i in range(6)])
# 构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#
# 有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']
# 将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']
# l1 = ['alex', 'WuSir', '老男孩', '太白']
# 有以下数据类型：
#
x = {'name':'alex',
     'Values':[{'timestamp':1517991992.94,'values':100,},
               {'timestamp': 1517992000.94,'values': 200,},
            {'timestamp': 1517992014.94,'values': 300,},
            {'timestamp': 1517992744.94,'values': 350},
            {'timestamp': 1517992800.94,'values': 280}],}

# 将上面的数据通过列表推导式转换成下面的类型：
# [[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
# print([[i['timestamp'],i['values']] for i in x.get('Values')])
# 用列表完成笛卡尔积
# 什么是笛卡尔积？ 笛卡尔积就是一个列表，
# 列表里面的元素是由输入的可迭代类型的元素对构成的元组，
# 因此笛卡尔积列表的长度等于输入变量的长度的乘积。
# [(),(),().....]
# ​	a. 构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色（列表里面的元素为元组类型)。
#
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# [('S','black'),('S','white')]
# print([() for size in ])
# l1 = []
# for color in colors:
#     for size in sizes:
#         l1.append((color,size))
# print(l1)
# print([(color,size) for color in colors for size in sizes])
# ​	b. 构建一个列表,列表里面的元素是扑克牌除去大小王以后，所有的牌类（列表里面的元素为元组类型）。
#
# l1 = [('A','spades'),('A','diamonds'), ('A','clubs'), ('A','hearts')......('K','spades'),('K','diamonds'), ('K','clubs'), ('K','hearts') ]
#
#
# 简述一下yield 与yield from的区别。
#
# 看下面代码，能否对其简化？说说你简化后的优点？
#

def chain(*args):
    # ('abc',(0,1,2))
    for it in args:
        for i in it:
            yield i
g = chain('abc',(0,1,2))
# 怎么让生成器产出值？
# next ，for 循环, 转化成list
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(list(g))
# print(list(g))  # 将迭代器转化成列表


def chain(*args):
    # ('abc',(0,1,2))
    for it in args:
        yield from it  # 'abc'  (0,1,2)
g = chain('abc',(0,1,2))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# yield from 优化了内层循环，提高了效率。

# print(list(g))
# def func():
#     # yield [1,2,3]
#     yield from [1,2,3]
#     '''
#     yield 1
#     yield 2
#     yield 3
#     '''
# g = func()
# print(next(g))
# print(next(g))
# print(next(g))

# 看代码求结果（面试题）：
v = [i % 2 for i in range(10)]
print(v)

v = (i % 2 for i in range(10))
print(v)
#
for i in range(5):
	print(i)
print(i)
# 看代码求结果：（面试题）
# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
# g2=(i for i in g1)
#
# print(list(g1))
# print(list(g2))
# 看代码求结果：（面试题）
# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# for n in [1,10]:
#     g=(add(n,i) for i in g)
#
# print(list(g))