"""
次模块作为对外引用的入口
"""

# 相对导入同项目下的模块
# from ..z import zz            # 容易向外界暴露zz模块
# from . import abc             # 导入同路径下的abc模块
from ..z.zz import *

# 不使用相对导入的方式，导入本项目中的模块
# 通过当前文件的路径找到z的路径
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.dirname(__file__)) + '/z')
# from zz import *

# 定义自己的成员
age2 = 888
def f2():
    print('f2')


