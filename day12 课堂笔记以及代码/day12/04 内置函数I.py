# python 提供了68个内置函数。
# 今天讲的这部分大部分了解即可。
# eval 剥去字符串的外衣运算里面的代码，有返回值。
s1 = '1 + 3'
# print(s1)
# print(eval(s1))  **
# s = '{"name": "alex"}'
# print(s,type(s))
# print(dict(s)) # 不行
# print(eval(s),type(eval(s)))
# 网络传输的str input 输入的时候,sql注入等等绝对不能使用eval。

# exec 与eval几乎一样， 代码流。
msg = """
for i in range(10):
    print(i)
"""
# print(msg)
# exec(msg)
# hash 哈希值
# print(hash('fsjkdafsda'))

# help 帮助
# s1 = 'fjdsls'
# print(help(str))
# print(help(str.upper))
# s1 = 'sfsda'
# s1.upper()


s1 = 'fdsklfa'
# s1()
def func():
    pass
# func
# # callable 判断一个对象是否可被调用  ***
# print(callable(s1))
# print(callable(func))