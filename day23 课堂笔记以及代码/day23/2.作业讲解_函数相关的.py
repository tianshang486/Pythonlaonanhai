# sys.argv练习
# 写一个python脚本,在cmd里执行
# python xxx.py 用户名 密码 cp 文件路径 目的地址
# python xxx.py alex sb cp D:\python_22\day22\1.内容回顾.py D:\python_22\day21
# python D:\python_22\day23\2.作业讲解_函数相关的.py alex sb rm D:\python_22\day23\6.作业.py
# python D:\python_22\day23\2.作业讲解_函数相关的.py alex sb rename D:\python_22\day23  D:\python_22\day24
# python D:\python_22\day23\2.作业讲解_函数相关的.py alex sb move D:\python_22\day23\文件  D:\python_22\day24
# python D:\python_22\day23\2.作业讲解_函数相关的.py alex sb mkdir D:\python_22\新的文件夹名
# 在这个基础上实现一个move移动 把一个文件或者文件夹移动到另一个位置
# 创建文件夹
# import os
# import sys
# import shutil
# if len(sys.argv) >= 5:
#     if sys.argv[1] =='alex' and sys.argv[2] == 'sb':
#         if sys.argv[3] == 'cp' and len(sys.argv) == 6:
#             if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
#                 filename = os.path.basename(sys.argv[4])
#                 path = os.path.join(sys.argv[5],filename)
#                 shutil.copy2(sys.argv[4],path)
#         elif sys.argv[3] == 'rm' and len(sys.argv) == 5:
#             if os.path.exists(sys.argv[4]):
#                 if os.path.isfile(sys.argv[4]):os.remove(sys.argv[4])
#                 else:shutil.rmtree(sys.argv[4])
#         elif sys.argv[3] == 'rename'and len(sys.argv) == 6:
#             if os.path.exists(sys.argv[4]):
#                     os.rename(sys.argv[4],sys.argv[5])
# else:
#     print('您输入的命令无效')


# 使用walk来计算文件夹的总大小
# import os
# g = os.walk('D:\python_22')
# size = 0
# for i in g :
#     path,dir_lst,name_lst = i
#     for name in name_lst:
#         abs_path = os.path.join(path,name)
#         size += os.path.getsize(abs_path)
# print(size)
