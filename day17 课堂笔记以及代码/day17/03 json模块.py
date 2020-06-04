l1 = [i for i in range(10000)]
# l1 --->bytes
# b1 = l1.encode('utf-8')  # 不能直接转换
# l1转化成字符串在转化成bytes
s1 = str(l1)
b1 = s1.encode('utf-8')
# print(b1)

# 岑哥接收了b1
s2 = b1.decode('utf-8')
# print(s2,type(s2))

# str 我们学过的str

# dic = {'username': '太白', 'password': 123,'status': True}
import json
#dumps loads 主要用于网络传输,但是也可以读写文件
# 特殊的字符串
# st = json.dumps(dic,ensure_ascii=False)
# print(st,type(st))
# # 反转回去
# dic1 = json.loads(st)
# print(dic1,type(dic1))

# 写入文件
# l1 = [1, 2, 3, {'name': 'alex'}]
# 转化成特殊的字符串写入文件
# with open('json文件',encoding='utf-8',mode='w') as f1:
#     st = json.dumps(l1)
#     f1.write(st)

# 读取出来还原回去
# with open('json文件',encoding='utf-8') as f2:
#     st = f2.read()
#     l1 = json.loads(st)
#     print(l1,type(l1))
# 特殊的参数
l1 = [1, 2, 3, {'name': 'alex'}]

# dump load 只能写入文件,只能写入一个数据结构
# with open('json文件1',encoding='utf-8',mode='w') as f1:
#     json.dump(l1,f1)

# 读取数据
# with open('json文件1',encoding='utf-8') as f2:
#     l1 = json.load(f2)
#     print(l1,type(l1))


# 一次写入文件多个数据怎么做?

# 错误示例:
# dic1 = {'username': 'alex'}
# dic2 = {'username': '太白'}
# dic3 = {'username': '大壮'}
# with open('json文件1',encoding='utf-8',mode='w') as f1:
#     json.dump(dic1,f1)
#     json.dump(dic2,f1)
#     json.dump(dic3,f1)


# 读取数据
# with open('json文件1',encoding='utf-8') as f1:
#     print(json.load(f1))
    # print(json.load(f1))
    # print(json.load(f1))


# 正确写法:
dic1 = {'username': 'alex'}
dic2 = {'username': '太白'}
dic3 = {'username': '大壮'}
# with open('json文件1',encoding='utf-8',mode='w') as f1:
#     f1.write(json.dumps(dic1) + '\n')
#     f1.write(json.dumps(dic2) + '\n')
#     f1.write(json.dumps(dic3) + '\n')

# with open('json文件1',encoding='utf-8') as f1:
#     for i in f1:
#         print(json.loads(i))


