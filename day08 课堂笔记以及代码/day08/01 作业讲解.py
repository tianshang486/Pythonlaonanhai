# '''
# l1 = [5,] l1+= [3] 结果：
#     1.报错
#     2. [5]
#     3 [5,3]
#     4, [5,3,3]
#
# 0000 0100
# '''
# day07 作业
#
# 看代码写结果
#
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
#
# v1.append(6)
# print(v1)
# print(v2)
# 看代码写结果
#
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
#
# v2[1][0] = 111
# v2[2][0] = 222
# print(v1)
# print(v2)
# 看代码写结果，并解释每一步的流程。
#
# v1 = [1,2,3,4,5,6,7,8,9]
# v2 = {}
# for item in v1:
#     if item < 6:
#         continue
#     if 'k1' in v2:
#         v2['k1'].append(item)
#     else:
#         v2['k1'] = [item ]  # v2 = {'k1': [6,7]}
# print(v2)
# 简述深浅拷贝？
#
# 看代码写结果
#
# import copy
#
# v1 = "alex"
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1 is v2)
# print(v1 is v3)
# 看代码写结果
#
# import copy
#
# v1 = [1,2,3,4,5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1 is v2)
# print(v1 is v3)
# 看代码写结果
#
import copy
#
# v1 = [1,2,3,4,5]
#
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[0] is v2[0])
# print(v1[0] is v3[0])
# print(v2[0] is v3[0])
#
# 看代码写结果
#
# import copy
#
# v1 = [1,2,3,4,[11,22]]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[-1] is v2[-1])
# print(v1[-1] is v3[-1])
# print(v2[-1] is v3[-1])
# 看代码写结果
#
# import copy
#
# v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
# v2 = copy.copy(v1)
#
# print(v1 is v2)
#
# print(v1[0] is v2[0])
# print(v1[3] is v2[3])
#
# print(v1[3]['name'] is v2[3]['name'])
# print(v1[3]['numbers'] is v2[3]['numbers'])
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])
# 看代码写结果
#
import copy
#
v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
v2 = copy.deepcopy(v1) # [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]

# print(v1 is v2)  # False

# print(v1[0] is v2[0])  # True
# print(v1[3] is v2[3])  # False

# print(v1[3]['name'] is v2[3]['name'])  # True
# print(v1[3]['numbers'] is v2[3]['numbers'])  # False
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])  # True
# 请说出下面a,b,c三个变量的数据类型。
#
# ```python
# a = ('太白金星')
# b = (1,)
# c = ({'name': 'barry'})
# ```
# 按照需求为列表排序：
#
# l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
# # 从大到小排序
# # 从小到大排序
# # 反转l1列表
# 利用python代码构建一个这样的列表(升级题)：
# [['_','_','_'],['_','_','_'],['_','_','_']]
# 看代码写结果：
#
# l1 = [1,2,]
# l1 += [3,4]
# print(l1)
# 看代码写结果：
#
# ```python
# dic = dict.fromkeys('abc',[])
# dic['a'].append(666)
# dic['b'].append(111)
# print(dic)
# ```
# l1 = [11, 22, 33, 44, 55]，请把索引为奇数对应的元素删除（不能一个一个删除，此l1只是举个例子，里面的元素不定）
#
# dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18} 请将字典中所有键带k元素的键值对删除.
#
# bytes数据类型是python的基础数据类型，bytes类型存在的意义是什么？
#
# 列举bytes类型与str类型的三个不同点？
#
# 完成下列需求：
#
# s1 = '太白金星'
# # 将s1转换成utf-8的bytes类型。
# # 将s1转化成gbk的bytes类型。
# b = b'\xe5\xa4\xaa\xe7\x99\xbd\xe6\x9c\x80\xe5\xb8\x85'
# # b为utf-8的bytes类型，请转换成gbk的bytes类型。
#
# 用户输入一个数字，判断一个数是否是水仙花数。
#
# 水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数. 那这个数就是一个水仙花数,
#
# 例如: 153 =1**3 + 5**3 + 3**3
# 把列表中所有姓周的⼈的信息删掉(此题有坑, 请慎重):
#
# lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
#
# 结果: lst = ['麻花藤']
#
# 车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (选做题)
#
# cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
#
# locals = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南','京': '北京'}
#
# 结果: {'⿊⻰江':2, '⼭东': 1, '北京': 1}