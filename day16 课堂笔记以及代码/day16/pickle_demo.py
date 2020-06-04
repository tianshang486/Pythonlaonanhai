"""
pickle:
将Python中所有的数据类型.转换成字节串.序列化过程
将字节串转换成python中数据类型,反序列化过程.

"""

import pickle
#
# bys = pickle.dumps([1,2,3])
# print(type(bys))    # <class 'bytes'>
# print(bys)          # b'\x80\x03]q\x00(K\x01K\x02K\x03e.'

# 保存了元组的数据类型
# bys = pickle.dumps((1,2,3))
# # print(bys)
# #
# res = pickle.loads(bys)
# print(type(res))

# 所有的数据类型都可以进行序列化
# bys = pickle.dumps(set('abc'))
# res = pickle.loads(bys)
# print(type(res))

# 把pickle序列化内容写入文件中
# with open('c.txt',mode='wb') as f:
#     pickle.dump([1,2,3],f)

# 从文件中反序列化pickle数据
# with open('c.txt',mode='rb') as f:
#     res = pickle.load(f)
#     print(type(res))
#     print(res)


# 多次pickle数据到同一个文件中
# with open('c.txt',mode='ab') as f:
#     pickle.dump([1,2,3],f)
#     pickle.dump([1,2,3],f)
#     pickle.dump([1,2,3],f)

# 从文件中反序列化pickle数据
# with open('c.txt',mode='rb') as f:
#     for x in range(4):
#         res = pickle.load(f)
#         print(res)

# pickle常用场景:和json一样,一次性写入,一次性读取.

# json,pickle的比较:
"""
json:
1.不是所有的数据类型都可以序列化.结果是字符串.
2.不能多次对同一个文件序列化.
3.json数据可以跨语言

pickle:
1.所有python类型都能序列化,结果是字节串.
2.可以多次对同一个文件序列化
3.不能跨语言.

"""