# read 全部读出来  **
# f = open('文件的读', encoding='utf-8')
# content = f.read()
# print(content,type(content))
# f.close()

# read(n) 按照字符读取
# f = open('文件的读', encoding='utf-8')
# content = f.read(5)
# print(content)
# f.close()

# readline()
# f = open('文件的读', encoding='utf-8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# readlines() 返回一个列表，列表中的每个元素是源文件的每一行。
# f = open('文件的读', encoding='utf-8')
# l1 = f.readlines()
# for line in l1:
#     print(line)
# # print(l1)
# f.close()

# for 读取
# f = open('文件的读', encoding='utf-8')
# # ['abc太白金星最帅\n', '老男孩最好的老师\n', '老男孩教育是最好的学校\n', 'fhsjdkfha\n', 'fhdsfads\n']
# for line in f:
#     print(line)
# f.close()

# f = open('美女.jpg',mode='rb')
# content = f.read()
# print(content)
# f.close()