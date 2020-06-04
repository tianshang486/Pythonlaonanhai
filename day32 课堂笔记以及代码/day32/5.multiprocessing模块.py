# multiple  多元化的
# processing 进程
# multiprocessing 多元的处理进程的模块

# import os
# from multiprocessing import Process
#
# def func():
#     print(os.getpid(),os.getppid())
#     # pid process id           进程id
#     # ppid parent process id   父进程id
#
# if __name__ == '__main__':
#     # 只会在主进程中执行的所有的代码你写在name = main下
#     print('main :',os.getpid(),os.getppid())
#     p = Process(target=func)
#     p.start()

# 为什么要用 if __name__ == '__main__':
# 能不能给子进程传递参数
# import os
# from multiprocessing import Process
#
# def func(name,age):
#     print(os.getpid(),os.getppid(),name,age)
#
# if __name__ == '__main__':
#     # 只会在主进程中执行的所有的代码你写在name = main下
#     print('main :',os.getpid(),os.getppid())
#     p = Process(target=func,args=('alex',84))
#     p.start()

# 能不能获取子进程的返回值   # 不能

# 能不能同时开启多个子进程
# import os
# import time
# from multiprocessing import Process
#
# def func(name,age):
#     print('%s start'%name)
#     time.sleep(1)
#     print(os.getpid(),os.getppid(),name,age)
#
# if __name__ == '__main__':
#     # 只会在主进程中执行的所有的代码你写在name = main下
#     print('main :',os.getpid(),os.getppid())
#     arg_lst = [('alex',84),('太白', 40),('wusir', 48)]
#     for arg in arg_lst:
#         p = Process(target=func,args=arg)
#         p.start()  # 异步非阻塞

# join的用法
# import os
# import time
# import random
# from multiprocessing import Process
#
# def func(name,age):
#     print('发送一封邮件给%s岁的%s'%(age,name))
#     time.sleep(random.random())
#     print('发送完毕')
#
# if __name__ == '__main__':
#     arg_lst = [('大壮',40),('alex', 84), ('太白', 40), ('wusir', 48)]
#     p_lst = []
#     for arg in arg_lst:
#         p = Process(target=func,args=arg)
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:p.join()
#     # p_l = []
#     # p = Process(target=func, args=('大壮',40))
#     # p.start()
#     # p_l.append(p)
#     # p = Process(target=func, args=('alex', 84))
#     # p.start()
#     # p_l.append(p)
#     # p = Process(target=func, args=('太白', 40))
#     # p.start()
#     # p_l.append(p)
#     # p = Process(target=func, args=('wusir', 48))
#     # p.start()
#     # p_l.append(p)
#     # for p in p_l:p.join()
#     print('所有的邮件已发送完毕')

# 同步阻塞 异步非阻塞
    # 同步阻塞 join
    # 异步非阻塞 start

# 多进程之间的数据是否隔离
# from multiprocessing import Process
# n = 0
# def func():
#     global n
#     n += 1
#
# if __name__ == '__main__':
#     p_l = []
#     for i in range(100):
#         p = Process(target=func)
#         p.start()
#         p_l.append(p)
#     for p in p_l:p.join()
#     print(n)


# 使用多进程实现一个并发的sokcet的server




