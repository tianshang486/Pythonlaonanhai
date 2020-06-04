# int  主要用于计算   + - * /
# 不同的进制之间的转换。10进制，2进制。
'''
二进制转换成十进制
0001 1010     ------> ?  26
'''
b = 1 * 2**4 + 1 * 2**3 + 0 * 2**2 + 1 * 2**1 + 0 * 2**0
# print(b)  # 26

'''
42  -----> 0010 1010
'''
# int
# bit_lenth 有效的二进制的长度
i = 4
print(i.bit_length())  # 3
i = 5
print(i.bit_length())  # 3
i = 42
print(i.bit_length())  # 4

# bool str int
# bool  <---> int
'''
True    1   False     0
非零即True    0 是 False
'''

# str   <--->   int  ***
'''
s1 = 10     int(s1)  : 必须是数字组成
i = 100     str(i)  
'''
# str  bool  ***
# 非空即True
s1 = ' '
print(bool(s1))

s1 = ''  # 空字符串
print(bool(s1))
# bool  ---> str  无意义
print(str(True))

s = input('输入内容')
if s:
    print('有内容')
else:
    print('没有输入任何内容')

