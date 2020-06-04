# 用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# name = ['oldboy','alex','wusir']
# print([n+'_sb' for n in name])
# print(list(map(lambda x:x+'_sb',name)))
#
# 用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
# l = [{'name':'alex'},{'name':'y'}]
# print(list(map(lambda x:x['name']+'sb',l)))
# 用filter来处理,得到股票价格大于20的股票名字
#
#  shares={
# 	'IBM':36.6,
# 	'Lenovo':23.2,
# 	'oldboy':21.2,
# 	'ocean':10.2,
# }
# 有下面字典，得到购买每只股票的总价格，并放在一个迭代器中结果：list一下[9110.0, 27161.0,......]
#
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 21.09},
# {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# 还是上面的字典，用filter过滤出单价大于100的股票。

# 有下列三种数据类型，
#
l1 = [1,2,3,4,5,6]
l2 = ['oldboy','alex','wusir','太白','日天']
tu = ('**','***','****','*******')
# ​写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）
# [(3, 'wusir', '****'), (4, '太白', '*******')]这样的数据。
# print(list(filter(lambda x: x[0] > 2 and len(x[-1])>=4,zip(l1,l2,tu))))

# ​	7. 有如下数据类型(实战题)：

l1 = [ {'sales_volumn': 0},

	{'sales_volumn': 108},

	{'sales_volumn': 337},

	{'sales_volumn': 475},

	{'sales_volumn': 396},

	{'sales_volumn': 172},

	{'sales_volumn': 9},

	{'sales_volumn': 58},

	{'sales_volumn': 272},

	{'sales_volumn': 456},

	{'sales_volumn': 440},

	{'sales_volumn': 239}]
#
# ​	将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
# print(sorted(l1,key=lambda x: x['sales_volumn']))
# print(sorted(l1,key=lambda x: x['sales_volumn'],reverse=True))
# 求结果(面试题)
# def func():
#     return 6

# v = [lambda :x for x in range(10)]
# # [function 432423, function 65654, function 756767,.......]
# print(v)
# print(v[0])
# print(v[0]()) # lambda : x 9
# 求结果(面试题)
v = (lambda :x for x in range(10))
# print(v)
# print(v[0])
# print(v[0]())
# print(next(v))  # lambda :x
# print(next(v)()) #  lambda :0  lambda :1
# print(str(100))
# list(map(str,[1,2,3,4,5,6,7,8,9]))  输出是什么? # (面试题)
# ['1', '2', '3'......'9']

# 写一个函数完成三次登陆功能：
# 用户的用户名密码从一个文件register中取出。
# register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
# 完成三次验证，三次验证不成功则登录失败，登录失败返回False。
# 登陆成功返回True。

# def get_user_pwd():
# 	user_dict = {}
# 	with open('register', encoding='utf-8') as f:
# 		for line in f:
# 			line_list = line.strip().split('|')
# 			user_dict[line_list[0].strip()] = line_list[1].strip()
# 	return user_dict
#
# def login():
# 	u_dict = get_user_pwd()
# 	count = 1
# 	while count < 4:
# 		username = input('请输入用户名：').strip()
# 		password = input('请输入密码：').strip()
# 		if username in u_dict and password == u_dict[username]:
# 			print('登录成功')
# 			return True
# 		else:
# 			print('用户名密码错误....重新登录')
# 		count += 1



# v = (lambda :x for x in range(10))