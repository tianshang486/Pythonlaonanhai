# 集合的创建：
# set1 = set({1, 3, 'Barry', False})
# set1 = {1, 3, '太白金星', 4, 'alex', False, '武大'}
# print(set1)

# 空集合：
# print({}, type({}))  # 空字典
# set1 = set()
# print(set1)

# 集合的有效性测试
# set1 = {[1,2,3], 3, {'name': 'alex'}}
# print(set1)

# set1 = {'太白金星', '景女神',  '武大', '三粗', 'alexsb', '吴老师'}
# 增：
# add
# set1.add('xx')
# print(set1)

# update迭代着增加
# set1.update('fdsafgsd')
# print(set1)

# 删
# remove
# remove 按照元素删除
# set1.remove('alexsb')
#
# print(set1)
# pop 随即删除
# set1.pop()
# print(set1)

# 变相改值
# set1.remove('太白金星')
# set1.add('男神')
# print(set1)

#关系测试：***
#  交集
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1 & set2)

# 并集：
# print(set1 | set2)

# 差集 -
# print(set1 - set2)

# 反交集
# print(set1 ^ set2)

# 子集
# set1 = {1,2,3}
# set2 = {1,2,3,4,5,6}
# # print(set1 < set2)
#
# # 超集
# print(set2 > set1)


# 列表的去重 ***
# l1 = [1,'太白', 1, 2, 2, '太白',2, 6, 6, 6, 3, '太白', 4, 5, ]
# set1 = set(l1)
# l1 = list(set1)
# print(l1)

# 用处：数据之间的关系，列表去重。