# 基本结构
'''
while 条件:
    循环体
'''

# 初识
# while True:
#     print('狼的诱惑')
#     print('我们不一样')
#     print('月亮之上')
#     print('庐州月')
#     print('人间')

# 循环如何终止？
# flag 标志位
# flag = True
# while flag:
#     flag = False
#     print('狼的诱惑')
#     print('我们不一样')
#     print('月亮之上')
#     print('庐州月')
#     print('人间')

# # 练习题： 1~ 100 所有的数字
# count = 1
# flag = True
# while flag:
#     print(count)
#     count = count + 1
#     if count == 101:
#         flag = False

# count = 1
# while count < 101:
#     print(count)
#     count = count + 1
#

# # 1 + 2 + 3 + ...... 100  的最终结果：
#
# s = 0
# count = 1
# while count < 101:
#     s = s + count
#     count = count + 1
# print(s)

# break：循环中遇到break直接退出循环。
# while True:
#     print('狼的诱惑')
#     print('我们不一样')
#     print('月亮之上')
#     break
#     print('庐州月')
#     print('人间')
# print(111)

# 1~100 所有的偶数：%
# print(102 % 2)
# count = 2
# while True:
#     print(count)
#     count = count + 2
#     if count == 102:
#         break

# # 方法2：
# count = 1
# while count < 101:
#     if count % 2 == 0:
#         print(count)
#     count = count + 1

# continue ： 退出本次循环，继续下一次循环
flag = True
while flag:
    print(111)
    print(222)
    flag = False
    continue
    print(333)

# while else： while 循环如果被break打断，则不执行else语句。
count = 1
while count < 5:
    print(count)
    if count == 2:
        break
    count = count + 1
else:
    print(666)