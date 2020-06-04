"""
os:和操作系统相关的操作被封装到这个模块中.

"""
import os
# 和文件操作相关,重命名,删除
# os.remove('a.txt')
# os.rename('a.txt','b.txt')

# 删除目录,必须是空目录
# os.removedirs('aa')

# 使用shutil模块可以删除带内容的目录
# import shutil
# shutil.rmtree('aa')

# 和路径相关的操作,被封装到另一个子模块中:os.path
# res = os.path.dirname(r'd:/aaa/bbb/ccc/a.txt') # 不判断路径是否存在.
# print(res)
#
# # 获取文件名
# res = os.path.basename(r'd:/aaa/bbb/ccc/a.txt')
# print(res)

# 把路径中的路径名和文件名切分开,结果是元组.
# res = os.path.split(r'd:/aaa/bbb/ccc/a.txt')
# print(res)

# 拼接路径
# path = os.path.join('d:\\','aaa','bbb','ccc','a.txt')
# print(path)

# 如果是/开头的路径,默认是在当前盘符下.
# res = os.path.abspath(r'/a/b/c')
# 如果不是以/开头,默认当前路径
# res = os.path.abspath(r'a/b/c')
# print(res)


# 判断
# print(os.path.isabs('a.txt'))
# print(os.path.isdir('d:/aaaa.txt')) # 文件不存在.False
# print(os.path.exists('d:/a.txt'))
# print(os.path.isfile('d:/asssss.txt'))      # 文件不存在.False


