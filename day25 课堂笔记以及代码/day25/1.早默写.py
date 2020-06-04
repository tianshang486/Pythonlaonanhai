# 内置的数据结构
    # {}  key-value 通过key找v非常快
    # []  序列 通过index取值非常快
    # ()  元组
    # {1,}集合
    # 'sx'字符串
# 不是python内置的
    # Queue队列 : 先进先出 FIFO(FIRST IN FIRST OUT)
        # put
        # get
    # Stack栈   : 后进先出 LIFO(Last In First Out)
        # put
        # get
    # 继承关系
        # 完成代码的简化

# 队列
# 栈
# 自定义Pickle,借助pickle模块来完成简化的dump和load
    # pickle dump
        # 打开文件
        # 把数据dump到文件里
    # pickle load
        # 打开文件
        # 读数据

# 对象 = Mypickle('文件路径')
# 对象.load()  能拿到这个文件中所有的对象
# 对象.dump(要写入文件的对象)