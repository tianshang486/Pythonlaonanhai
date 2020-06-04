"""
序列化:
把内存中的数据,转换成字节或字符串的形式,以便于进行存储或者
网络传输.

内存中数据 -> 字节串/字符串 : 序列化
字节串/字符串 -> 内存中的数据 : 反序列化
"""

# json :将数据转换成字符串,用于存储或网络传输.
import json
# s = json.dumps([1,2,3]) # 把指定的对象转换成json格式的字符串
# print(type(s))
# print(s)        # '[1,2,3]'   [1,2,3]

#
# s = json.dumps((1,2,3))     # 元组序列化后,变成列表
# print(s)

# res = json.dumps(10)
# print(res)          # '10'

# res = json.dumps({'name':'Andy','age':10})
# print(res)          # {"name": "Andy", "age": 10}

# res = json.dumps(set('abc'))      # Object of type 'set' is not JSON serializable

# 将json结果写到文件中
# with open('a.txt',mode='at',encoding='utf-8') as f:
#     json.dump([1,2,3],f)

# 反序列化
# res = json.dumps([1,2,3])
# lst = json.loads(res)           # 反序列化
# print(type(lst))
# print(lst)

# 元组会变成列表
# res = json.dumps((1,2,3))
# lst = json.loads(res)           # 反序列化
# print(type(lst))
# print(lst)


# 从文件中反序列化
# with open('a.txt',encoding='utf-8')as f:
#     res = json.load(f)
#     print(type(res))
#     print(res)

# json
# json.dumps(obj)
# json.dump(obj,f)
# json.loads(s)
# json.load(f)

# json文件通常是一次性写,一次性读.
# 使用另一种方式,可以实现多次写,多次读.


# 把需要序列化的对象.通过多次序列化的方式, 用文件的write方法,把多次序列化后的json字符串
# 写到文件中.
# with open('json.txt',mode='at',encoding='utf-8') as f:
#     f.write(json.dumps([1,2,3]) + '\n')
#     f.write(json.dumps([4,5,5]) + '\n')


#  把分次序列化的json字符串,反序列化回来
with open('json.txt',mode='rt',encoding='utf-8') as f:
    # res = json.loads(f.readline().strip())
    # print(res)
    # res2 = json.loads(f.readline().strip())
    # print(res2)
    # 使用循环改进:
    for x in f:
        print(json.loads(x.strip()))

