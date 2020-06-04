"""
random模块的演示
"""

import random
# 获取[0.0,1.0)范围内的浮点数
# print(random.random())
#
# # 获取[a,b)范围内的浮点数
# print(random.uniform(3,5))
#
# # 获取[a,b]范围内的一个整数
# print(random.randint(3,10))

# lst = list(range(10))
# random.shuffle(lst)
# print(lst)


t = (1,2,3)
# random.shuffle(t)
# 通过sample变相实现打乱
lst = random.sample(t,len(t))
print(lst)



