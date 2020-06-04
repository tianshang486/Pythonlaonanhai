l1 = [1, 2, 3, {'name': 'alex'}]

# dumps loads 只能用于网络传输
# import pickle
# st = pickle.dumps(l1)
# print(st)  # bytes
#
# l2 = pickle.loads(st)
# print(l2,type(l2))

# dump load 直接写入文件
# import pickle
# dic1 = {'name':'oldboy1'}
# dic2 = {'name':'oldboy2'}
# dic3 = {'name':'oldboy3'}
#
# f = open('pick多数据',mode='wb')
# pickle.dump(dic1,f)
# pickle.dump(dic2,f)
# pickle.dump(dic3,f)
# f.close()
# import pickle
# f = open('pick多数据',mode='rb')
# print(pickle.load(f))
# print(pickle.load(f))
# print(pickle.load(f))
# f.close()

import pickle
def func():
    print('in func')

# f = open('pick对象',mode='wb')
# pickle.dump(func,f)
# f.close()

# f = open('pick对象', mode='rb')
# ret = pickle.load(f)
# print(ret)
# ret()