# # def func():
# #     count = 1
# #     while 1:
# #         count += 1
# #         print(count)
# #         return
# # func()
#
# # def func(x,y):
# #     return x + y
# # func(1,6)
#
# 1.整理函数相关知识点,写博客。
#
# 2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
#
# 3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def func(x):
#     if len(x) > 5:
#         return True
#     else:
#         return False

# def func(x):
#     return True if len(x) > 5 else False

# def func(x):
#     return len(x) > 5
# print(func('f'))

# 4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#
# 5.写函数，计算传入函数的字符串中,[数字]、[字母] 以及 [其他]的个数，并返回结果。
#
# 6.写函数，接收两个数字参数，返回比较大的那个数字。
#
# 7.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}    {"k1": "v1", "k2": [11,22]}
# PS:字典中的value只能是字符串或列表
# def func(dic):
#     dict1 = {}
#     for key,value in dic.items():
#         dict1[key] = value[:2]
#     return dict1


#
# 8.写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
# 此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
#
# 9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。
# 用户通过输入这四个内容，然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
#
# 10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
# 用户持续输入： while input
# # 函数：接收四个参数。将四个参数追加到文件中。
# def register(n,s,a,e):
#     with open('student_msg',encoding='utf-8', mode='a') as f1:
#         f1.write('{}|{}|{}|{}\n'.format(n,s,a,e))
#
# while 1:
#     name = input('请输入姓名(Q或者q退出)：')
#     if name.upper() == 'Q': break
#     sex = input('请输入性别：')
#     age = input('请输入年龄：')
#     edu = input('请输入学历：')
#     register(name,sex,age,edu)


# 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（选做题）。
# import os
# def file(path,old_content,new_content):
#     with open(path,encoding='utf-8') as f1,\
#         open(path+'.bak',encoding='utf-8',mode='w') as f2:
#         for line in f1:
#             new_line = line.replace(old_content, new_content)
#             f2.write(new_line)
#     os.remove(path)
#     os.rename(path+'.bak',path)
# file('alex自述','alex', 'SB')
# file('t1','太白','barry')


