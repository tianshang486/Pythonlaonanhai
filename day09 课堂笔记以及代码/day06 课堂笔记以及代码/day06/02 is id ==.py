# id 身份证号
# i = 100
# s = 'alex'
# print(id(i))
# print(id(s))
# == 比较的是两边的值是否相等
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# print(l1 == l2)
# s1 = 'alex'
# s2 = 'alex '
# print(s1 == s2)

# is 判断的是内存地址是否相同
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# print(id(l1))
# print(id(l2))
# print(l1 is l2)

s1 = 'alex'
s2 = 'alex'
print(id(s1))
print(id(s2))
print(s1 is s2)

# id 相同，值一定相同
# 值相同，id不一定相同


