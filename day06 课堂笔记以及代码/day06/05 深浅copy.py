# 赋值运算
# l1 = [1, 2, 3, [22, 33]]
# l2 = l1
# l1.append(666)
# print(l1)
# print(l2)

# 浅copy
# l1 = [1, 2, 3, [22, 33]]
# l2 = l1.copy()
# l1.append(666)
# print(l1,id(l1))
# print(l2,id(l2))


# l1 = [1, 2, 3, [22, 33]]
# l2 = l1.copy()
# l1[-1].append(666)
# print(id(l1[-1]))
# print(id(l2[-1]))
# print(id(l1[0]))
# print(id(l2[0]))
# print(l1)
# print(l2)


# l1 = [1, 2, 3, [22, 33]]
# l2 = l1.copy()
# l1[0] = 90
# print(l1)
# print(l2)



# 深copy
# import copy
# l1 = [1, 2, 3, [22, 33]]
# l2 = copy.deepcopy(l1)
# # print(id(l1))
# # print(id(l2))
# l1[-1].append(666)
# print(l1)
# print(l2)



# 相关面试题；
# l1 = [1, 2, 3, [22, 33]]
# l2 = l1[:]
# l1[-1].append(666)
# print(l1)
# print(l2)
# 浅copy： list dict: 嵌套的可变的数据类型是同一个。
# 深copy： list dict: 嵌套的可变的数据类型不是同一个 。