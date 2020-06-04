# 机试题
# 1.lis = [['哇',['how',{'good':['am',100,'99']},'太白金星'],'I']] （2分）
# # o列表lis中的'am'变成大写。(1分)
# # o列表中的100通过数字相加在转换成字符串的方式变成'10010'。(1分)
# # 2.dic = {'k1':'v1','k2':['alex','sb'],(1,2,3,):{'k3':['2',100,'wer']}} （3分）
# # o将'k3'对应的值的最后面添加一个元素'23'。(1分)
# # o将'k2'对应的值的第0个位置插入元素'a'。(1分)
# o将(1,2,3,)对应的值添加一个键值对'k4','v4'。(1分)
# 3.实现一个整数加法计算器（多个数相加）：（5分）
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。


# 4.请写一个电影投票程序。现在上映的电影列表如下：(10分)
lst = ['复仇者联盟4', '驯龙高手3', '金瓶梅', '老男孩', '大话西游']
# 由用户给每⼀个电影投票.最终将该⽤户投票信息公布出来。
# 要求：
# o用户可以持续投票，用户输入序号，进行投票。比如输入序号 1，给金瓶梅投票1。
# o每次投票成功，显示给哪部电影投票成功。
# o退出投票程序后，要显示最终每个电影的投票数。
# 建议最终投票的结果为这种形式：
# {'⾦瓶梅': 0, '复仇者联盟4': 0, '驯龙高手3': , '老男孩': 0,'大话西游':0}
# dic = dict.fromkeys(lst,0)
# print(dic)
# lst = ['复仇者联盟4', '驯龙高手3', '金瓶梅', '老男孩', '大话西游']
# dic = {}
# while 1:
#     for index,moive_name in enumerate(lst):
#         print(f'序号：{index+1} 电影名称：{moive_name}')
#     num = input('请输入您要投票的电影序号：').strip()
#     if num.isdecimal():
#         num = int(num)
#         if 0 < num <= len(lst):
#             if lst[num-1] not in dic:
#                 dic[lst[num-1]] = 1
#                 print(dic)
#             else:
#                 dic[lst[num-1]] += 1
#                 print(dic)
#         else:
#             print('超出范围，重新输入')
#     elif num.upper() == 'Q': break
#     else:
#         print('输入有误，重新输入')
# print(dic)
# for movie_name,count in dic.items():
#     print(f'电影{movie_name} 最终得票数为{count}')


# 5.有文件t1.txt里面的内容为:（10分）
# id,name,age,phone,job
# 1,alex,22,13651054608,IT 2,wusir,23,13304320533,Tearcher 3,taibai,18,1333235322,IT
# 利用文件操作，将其构造成如下数据类型。
# [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},......]
# 6.按要求完成下列转化。(10分)
list3 = [
{"name": "alex", "hobby": "抽烟"},
{"name": "alex", "hobby": "喝酒"},
{"name": "alex", "hobby": "烫头"},
{"name": "alex", "hobby": "Massage"},
{"name": "wusir", "hobby": "喊麦"},
{"name": "wusir", "hobby": "街舞"},
{"name": "wusir", "hobby": "出差"},
]
list4 = [
    {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
    {"name": "wusir", "hobby_list": ["喊麦", "街舞","出差"]},
]
# 将list3 这种数据类型转化成list4类型,你写的代码必须支持可拓展.
# 比如list3 数据在加一个这样的字典{"name": "wusir", "hobby": "溜达"},
# list4 {"name": "wusir", "hobby_list": ["喊麦", "街舞", "溜达"]
# 或者list3增加一个字典{"name": "太白", "hobby": "开车"},
# list4{"name": "太白", "hobby_list": ["开车"],
# 无论按照要求加多少数据,你的代码都可以转化.如果不支持拓展,则4分,支持拓展则10分.
# 两种方式：
# l1 = []
# 1.直接构建。
# for i in list3:
#     for j in l1:
#         if i['name'] == j['name']:
#             j['hobby_list'].append(i['hobby'])
#             break
#     else:
#         l1.append({'name': i['name'], 'hobby_list':[i['hobby'],]})
# print(l1)

# 2,构建特殊的数据结构。
# dic = {'alex':{"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
# "wusir": {"name": "wusir", "hobby_list": ["喊麦", "街舞","出差"]}
#  }
# print(list(dic.values()))
# dic = {}
# for i in list3:
#     if i['name'] not in dic:
#         dic[i['name']] = {'name': i['name'],'hobby_list':[i['hobby'],]}
#     else:
#         dic[i['name']]['hobby_list'].append(i['hobby'])
# print(list(dic.values()))
