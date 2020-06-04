# # python 提供了68个内置函数。
# # 今天讲的这部分大部分了解即可。
# # eval 剥去字符串的外衣运算里面的代码，有返回值。  **
# s1 = '1 + 3'
# # print(s1)
# # print(eval(s1))  **
# # s = '{"name": "alex"}'
# # print(s,type(s))
# # print(dict(s)) # 不行
# # print(eval(s),type(eval(s)))
# # 网络传输的str input 输入的时候,sql注入等等绝对不能使用eval。
#
# # exec 与eval几乎一样， 代码流。
# msg = """
# for i in range(10):
#     print(i)
# """
# # print(msg)
# # exec(msg)
# # hash 哈希值
# # print(hash('fsjkdafsda'))
#
# # help 帮助  **
# # s1 = 'fjdsls'
# # print(help(str))
# # print(help(str.upper))
# # s1 = 'sfsda'
# # s1.upper()
#
#
# s1 = 'fdsklfa'
# # s1()
# def func():
#     pass
# # func
# # # callable 判断一个对象是否可被调用  ***
# # print(callable(s1))
# # print(callable(func))

# int
# print(int(3.6))

# float
# print(type(3.6))

# print(complex(1,2))  # (1+2j)

# bin：将十进制转换成二进制并返回。  **
# print(bin(100))
# # oct：将十进制转化成八进制字符串并返回。  **
# print(oct(10))
# # hex：将十进制转化成十六进制字符串并返回。  **
# print(hex(10))
# print(hex(13))

# divmod  **
# print(divmod(10,3))
# round：保留浮点数的小数位数  **
# print(round(3.141592653, 2))  # 3.14
# pow：求x**y次幂。（三个参数为x**y的结果对z取余）
# print(pow(2,3))  **
# print(pow(2,3,3))  #   2**3 % 3

# bytes ***
s1 = '太白'
# b = s1.encode('utf-8')
# print(b)
# b = bytes(s1,encoding='utf-8')
# print(b)

# ord:输入字符找该字符编码的位置
# ascii Unicode
# print(ord('a'))  #
# print(ord('中'))  # 20013  Unicode
# # chr:输入位置数字找出其对应的字符 #  **
# # print(chr(97))
# print(chr(20013))  # Unicode

# repr:返回一个对象的string形式（原形毕露）。  ***
# s1 = '存龙'
# # # print(s1)
# # print(repr(s1))
# # msg = '我叫%s' %(s1)
# msg = '我叫%r' %(s1)
# print(msg)
# all：可迭代对象中，全都是True才是True
# l1 = [1, 2, '太白', True, [1,2,3], '']
# print(all(l1))
# any：可迭代对象中，有一个True 就是True
# l1 = [ 0, '太白', False, [], '',()]
# print(any(l1))

# print(self, *args, sep=' ', end='\n', file=None)
# print(1,2,3,4)
# print(1,2,3,4,sep='&')
# print(1, end=' ')
# print(2)

# list
# l1 = [1,2,3,4]
# l2 = list()
# l2 = list('fjfdsklagjsflag')
# print(l2)

# dict 创建字典的几种方式
# 直接创建
# 元组的解构
# dic = dict([(1,'one'),(2,'two'),(3,'three')])
# dic = dict(one=1,two=2)
# print(dic)
# fromkeys
# update
# 字典的推导式

# abs()  ***
# print(abs(-6))

# sum  ***
# l1 = [i for i in range(10)]
# s1 = '12345'
# print(sum(l1))
# print(sum(l1,100))
# print(sum(s1))  # 错误

# reversed  返回的是一个翻转的迭代器  ***
# l1 = [i for i in range(10)]
# # l1.reverse()  # 列表的方法
# # print(l1)
# l1 = [i for i in range(10)]
# obj = reversed(l1)
# print(l1)
# print(list(obj))

# zip 拉链方法  ***
# l1 = [1, 2, 3, 4, 5]
# tu1 = ('太白', 'b哥', '德刚')
# s1 = 'abcd'
# obj = zip(l1,tu1,s1)
# # # print(obj)
# # for i in obj:
# #     print(i)
# print(list(obj))
# *************  以下方法最最最重要
# min max
l1 = [33, 2, 3, 54, 7, -1, -9]
# print(min(l1))
# 以绝对值的方式去最小值
# l2 = []
# func = lambda a: abs(a)
# for i in l1:
#     l2.append(func(i))
# print(min(l2))
# def abss(a):
#     '''
#     第一次：a = 33  以绝对值取最小值  33
#     第二次：a = 2  以绝对值取最小值  2
#     第三次：a = 3  以绝对值取最小值  2
#     ......
#     第六次：a = -1   以绝对值取最小值  1
#
#     '''
#     return abs(a)
# print(min(l1,key=abss))
# 凡是可以加key的：它会自动的将可迭代对象中的每个元素按照顺序传入key对应的函数中，
# 以返回值比较大小。
dic = {'a': 3, 'b': 2, 'c': 1}
# 求出值最小的键
# print(min(dic))  # min默认会按照字典的键去比较大小。
# def func(args):
#     '''
#     第一次：
#      args:   'a'   返回值：dic['a']     记录：3
#     第二次：
#      args :   'b'   返回值：dic['b']     记录：2
#     第三次：
#      args:  'c'   返回值：dic['c']    记录：1
#     '''
#     return dic[args]
# print(min(dic,key=lambda args: dic[args]))

# func = lambda a:dic[a]
# print(min(dic,key=lambda a: dic[a]))

# l2 = [('太白',18), ('alex', 73), ('wusir', 35), ('口天吴', 41)]
# print(min(l2))
# print(min(l2,key=lambda x:x[1]))
# max pass

# sorted  加key
# l1 = [22, 33, 1, 2, 8, 7,6,5]
# l2 = sorted(l1)
# print(l1)
# print(l2)

l2 = [('大壮', 76), ('雪飞', 70), ('纳钦', 94), ('张珵', 98), ('b哥',96)]
# print(sorted(l2))
# print(sorted(l2,key= lambda x:x[1]))  # 返回的是一个列表，默认从低到高
# print(sorted(l2,key= lambda x:x[1],reverse=True))  # 返回的是一个列表，默认从低到高


# filter 列表推导式的筛选模式
# l1 = [2, 3, 4, 1, 6, 7, 8]
# print([i for i in l1 if i > 3])  # 返回的是列表
# ret = filter(lambda x: x > 3,l1)  # 返回的是迭代器
# print(ret)
# print(list(ret))

# map  列表推导式的循环模式
# l1 = [1, 4, 9, 16, 25]
# print([i**2 for i in range(1,6)])  # 返回的是列表
# ret = map(lambda x: x**2,range(1,6))  # 返回的是迭代器
# print(ret)
# print(list(ret))

# reduce
from functools import reduce
def func(x,y):
    '''
    第一次：x  y  : 11  2     x + y =     记录： 13
    第二次：x = 13   y  = 3    x +  y =   记录： 16
    第三次  x = 16   y = 4 .......
    '''
    return x + y

l = reduce(func,[11,2,3,4])
print(l)