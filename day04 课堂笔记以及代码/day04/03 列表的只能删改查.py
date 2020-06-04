# 列表的创建
# 方式一
# l1 = [1, 2, 'Alex']

# 方式二
# l1 = list()
# l1 = list('fhdsjkafsdafhsdfhsdaf')
# print(l1)

# 方式三：列表推导式 后面讲

# 增删改查
l1 = ['太白', '女神', 'xiao','吴老师', '闫龙']
# 增：
# append:追加
# l1.append('xx')
# print(l1.append('xx'))  # 不能打印它
# print(l1)

# 举例：
# l1 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
# while 1:
#     name = input('请输入新员工姓名：(Q或者q退出程序)')
#     if name.upper() == 'Q': break
#     l1.append(name)
# print(l1)

# insert 插入
# l1.insert(2,'wusir')
# print(l1)
#extend 迭代着追加
# l1.extend('abcd')
# l1.extend(['alex',])
# l1.extend(['alex', 1, 3])
# print(l1)

# 删
# pop 按照索引位置删除
# l1.pop(-2)  # 按照索引删除 （返回的是删除的元素）
# print(l1.pop(-2))
# l1.pop()  # 默认删除最后一个
# print(l1)

# remove  指定元素删除,如果有重名元素，默认删除从左数第一个
# l1.remove('xiao')
# print(l1)

# clear(了解)
# l1.clear() # 清空
# print(l1)

# del
    # 按照索引删除
# del l1[-1]
# print(l1)
    # 按照切片(步长)删除
# del l1[::2]
# print(l1)

# 改
# 按照索引改值
# l1[0] = '男神'
# 按照切片改（了解）
# l1[2:] = 'fsdafsdafsdfdsfsadfdsfdsgsfdag'
# print(l1)
# 按照切片（步长）（了解）
# l1[::2] = 'abc'
# l1[::2] = 'abcd'
# print(l1)

# 查：
# 索引，切片（步长）
# for i in l1:
#     print(i)

