# i1 = 2
# i2 = 3
# print(2 ** 3)
# print(10 // 3)
# print(10 % 3)
#
# print(3 != 4)
#
# count = 1
# count = count + 1
# count += 1
# print(count)


# and or not

# 1 在没有()的情况下，优先级：not > and > or，同一优先级从左至右依次计算
# 情况1：两边都是比较运算
# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)
# print(True or False)

# 情况2：两边都是整数
'''
x or y , x为真，值就是x，x为假，值是y
'''
# print(1 or 2)
# print(3 or 2)
# print(4 or 2)
# print(-1 or 2)
# print(0 or 2)

# print(1 and 2)

# str ---> int  : 只能是纯数字组成的字符串
s1 = '00100'
print(int(s1))
# int ----> str
i1 = 100
print(str(i1),type(str(i1)))

# int  ---> bool  : 非零即True ，0为False。
i = 0
print(bool(i))
# bool ---> int
print(int(True))  # 1
print(int(False))  # 0

# 面试题：
# print(1 and 2 or 3 and 4)

# 思考题：
# print(1 > 2 and 3 or 6)
# print(2**32)
# print(7.6 * 1024 * 1024 * 8)