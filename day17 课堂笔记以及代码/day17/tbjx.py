# print('from the tbjx.py')
__all__ = ['name', 'read1']  # 配合*使用

name = '太白金星'

def read1():
    print('tbjx模块：', name)

def read2():
    print('tbjx模块')
    read1()

def change():
    global name
    name = 'barry'
    print(name)



# print(__name__)
# 当tbjx.py做脚本: __name__ == __main__  返回True
# 当tbjx.py做模块被别人引用时: __name__ == tbjx

# __name__ 根据文件的扮演的角色(脚本,模块)不同而得到不同的结果
#1, 模块需要调试时,加上 if __name__ == '__main__':
# import time

# change()  # 测试代码
# if __name__ == '__main__':
#     change()

# 2, 作为项目的启动文件需要用.

