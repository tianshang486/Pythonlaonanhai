# s = 'alex'
# # # s2 = s.upper()
# #
# # s = s.upper()
# # print(s,s2)

# i = 100
# i = 101
# i = 102

# l1 = [1, 2, 3]
# l1.append(666)
# print(l1)

# dic = {'太白':
#      {'name': '太白金星','age': 18, 'sex': '男'},
#  'python22期':
#      ['朱光亚', '大壮', '雪飞', '岑哥'],
#  }
dict
# 字典的创建方式：
# 面试会考
# 方式一：
# dic = dict((('one', 1), ('two', 2), ('three', 3)))
# print(dic)  # {'one': 1, 'two': 2, 'three': 3}

# 方式二：
# dic = dict(one=1, two=2, three=3)
# print(dic)

# 方式三：
# dic = dict({'one': 1, 'two': 2, 'three': 3})
# print(dic)

# 验证字典的合法性：
# dic = {[1,2,3]: 'alex', 1: 666}  # 键要不可变的数据类型
# print(dic)
# dic = {1: 'alex', 1: '太白', 2: 'wusir'}  # 键要唯一
# print(dic)

# dic = {'name': '太白', 'age': 18}
# 键值对：
    # 酒店：
    # 键：房间号，0~99
    # 值： 房间： 里面放什么数据都可以。

# 字典的增删改查：
dic = {'name': '太白', 'age': 18, 'hobby_list': ['直男', '钢管', '开车']}
# 增：
# 直接增加 有则改之，无则增加
# dic['sex'] = '男'
# dic['age'] = 23  # 改
# print(dic)
# setdefault  有则不变，无则增加
# dic.setdefault('hobby')
# dic.setdefault('hobby', '球类运动')
# dic.setdefault('age', 45)
# print(dic)

# 删
# pop 按照键删除键值对, 有返回值  ***
# 设置第二个参数则无论字典中有无此键都不会报错
# dic.pop('age')
# ret = dic.pop('age')
# ret = dic.pop('hobby','没有此键')
# print(ret)
# print(dic)

# clear  清空  **
# dic.clear()
# print(dic)

# del  **
# # del dic['age']
# del dic['age1']
# print(dic)


# 改
# dic['name'] = 'alex'
# print(dic)

# 查
# print(dic['hobby_list'])
# print(dic['hobby_list1'])

# get  ***
# l1 = dic.get('hobby_list')
# l1 = dic.get('hobby_list1','没有此键sb')  # 可以设置返回值
# print(l1)

# 三个特殊的
# keys() values() items()
# print(dic.keys(),type(dic.keys()))
# 可以转化成列表
# print(list(dic.keys()))
# for key in dic.keys():
#     print(key)
# for key in dic:
#     print(key)


# values()
# print(dic.values())
# print(list(dic.values()))
# for value in dic.values():
#     print(value)


# items()
# print(dic.items())
# for key,value in dic.items():
#     print(key,value)
# a,b = ('name', '太白')
# print(a,b)
# 面试题
# a = 18
# b = 12
# a,b = b,a
# # a,b = 12,18
# print(a,b)
# 练习题
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# 请在k3对应的值中追加一个元素 44，输出修改后的字典
# print(dic['k3'])
# l1 = dic.get('k3')
# print(l1)
# dic.get('k3').append(44)
# print(dic)
# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典