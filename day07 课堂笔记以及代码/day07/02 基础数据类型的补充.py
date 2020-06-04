# str ：补充的方法练习一遍就行。
# s1 = 'taiBAi'
# capitalize 首字母大写，其余变小写
# print(s1.capitalize())
# swapcase  大小写翻转
# print(s1.swapcase())
# title
# msg= 'taibai say3hi'
# print(msg.title()) #每个单词的首字母大写

s1 = 'barry'
# 居中
# print(s1.center(20))
# print(s1.center(20,'*'))

# find :通过元素找索引，找到第一个就返回，找不到 返回-1
# index:通过元素找索引，找到第一个就返回，找不到 报错
# print(s1.find('a'))
# print(s1.find('r'))
# print(s1.find('o'))
# print(s1.index('o'))

# tuple
# 元组中如果只有一个元素，并且没有逗号，那么它不是元组，它与改元素的数据类型一致。 ***
# tu1 = (2,3,4)
# tu1 = (2)
# tu1 = ('太白')
# tu1 = ([1,2,3])
# tu1 = (1,)
# print(tu1,type(tu1))
# tu = (1,2,3,3,3,2,2,3,)
# # count 计数
# print(tu.count(3))
# tu = ('太白', '日天', '太白')
# # index
# print(tu.index('太白'))

# tuple


# list
# l1 = ['太白', '123', '女神', '大壮']
# count pass
# index
# print(l1.index('大壮'))
# sort  **
# l1 = [5, 4, 3, 7, 8, 6, 1, 9]
# # l1.sort()  # 默认从小到大排序
# # l1.sort(reverse=True)  # 从大到小排序  **
# l1.reverse()  # 反转  **
# print(l1)
# 列表可以相加
# l1 = [1, 2, 3]
# l2 = [1, 2, 3, '太白', '123', '女神']
# print(l1 + l2)

# 列表与数字相乘
# l1 = [1, 'daf', 3]
# l2 = l1*3
# print(l2)

l1 = [11, 22, 33, 44, 55]
# 索引为奇数对应的元素删除（不能一个一个删除，此l1只是举个例子，里面的元素不定）。
#  *** 重要
# 正常思路：
# 先将所有的索引整出来。
# # 加以判断，index % 2 == 1： pop（index）
# for index in range(len(l1)):
#     if index % 2 == 1:
#         l1.pop(index)
# print(l1)
# 列表的特性：
# l1 = [11, 22, 33, 44, 55]
# 最简单的：
# del l1[1::2]
# print(l1)
# l1 = [11, 22, 33, 44, 55]
# # 倒序法删除元素
# for index in range(len(l1)-1,-1,-1):
#     if index % 2 == 1:
#         l1.pop(index)
# print(l1)

# 思维置换
# l1 = [11, 22, 33, 44, 55]
# new_l1 = []
# for index in range(len(l1)):
#     if index % 2 ==0:
#         new_l1.append(l1[index])
# # print(new_l1)
# l1 = new_l1
# print(l1)

# 循环一个列表的时，最好不要改变列表的大小，这样会影响你的最终的结果。


# 字典的补充
# update ***
# dic = {'name': '太白', 'age': 18}
# # dic.update(hobby='运动', hight='175')
# # dic.update(name='太白金星')
# dic.update([(1, 'a'),(2, 'b'),(3, 'c'),(4, 'd')])  # 面试会考
# print(dic)
# dic1 = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex","weight":75}
# dic1.update(dic2)  # 更新，有则覆盖，无责添加
# print(dic1)  # {'name': 'alex', 'age': 18, 'sex': 'male', 'weight': 75}
# print(dic2)

# fromkeys
# dic = dict.fromkeys('abc', 100)
# dic = dict.fromkeys([1, 2, 3], 'alex')
# 坑：值共有一个,面试题
# dic = dict.fromkeys([1,2,3],[])
# dic[1].append(666)
# print(dic)
dic = {'k1': '太白', 'k2': 'barry', 'k3': '白白', 'age': 18}
# 将字典中键含有'k'元素的键值对删除。
# for key in dic:
#     if 'k' in key:
#         dic.pop(key)
# print(dic)

# 循环一个字典时，如果改变这个字典的大小，就会报错。
# l1 = []
# for key in dic:
#     if 'k' in key:
#         l1.append(key)
# print(l1)
# for i in l1:
#     dic.pop(i)
# print(dic)

# for key in list(dic.keys()):  # ['k1', 'k2', 'k3','age']
#     if 'k' in key:
#         dic.pop(key)
# print(dic)

# 0,''(),[],{},set(),None