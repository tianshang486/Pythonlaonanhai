# %s format
# name = '太白'
# age = 18
# msg = '我叫%s,今年%s' %(name,age)
# msg1 = '我叫{},今年{}'.format(name,age)

# 新特性：格式化输出
# name = '太白'
# age = 18
# msg = f'我叫{name},今年{age}'
# print(msg)

# 可以加表达式
# dic = {'name':'alex','age': 73}
# msg = f'我叫{dic["name"]},今年{dic["age"]}'
# print(msg)

# count = 7
# print(f'最终结果：{count**2}')
# name = 'barry'
# msg = f'我的名字是{name.upper()}'
# print(msg)

# 结合函数写：
def _sum(a,b):
    return a + b

msg = f'最终的结果是：{_sum(10,20)}'
print(msg)
# ! , : { } ;这些标点不能出现在{} 这里面。
# 优点：
#  1. 结构更加简化。
#  2. 可以结合表达式，函数进行使用。
# 3. 效率提升很多。