# 为什么要写log?
    # log是为了排错
    # log用来做数据分析的

# 购物商城 - 数据库里
    # 什么时间购买了什么商品
    # 把哪些商品加入购物车了

# 做数据分析的内容 - 记录到日志
# 1.一个用户什么时间在什么地点 登录了购物程序
# 2.搜索了哪些信息,所长时间被展示出来了
# 3.什么时候关闭了软件
# 4.对哪些商品点进去看了

# 计算器
    # (1+2)*3/4
    # 计算乘法(表达式):
       # 记录日志:计算乘法表达式是什么,结果是什么
       # return
    # 计算除法
        # 记录日志:表达式是什么,结果是什么
       # return
    # 计算小括号内的
    # 计算加法
    # 计算减法

# 1.用来记录用户的行为 - 数据分析
# 2.用来记录用户的行为 - 操作审计
# 3.排查代码中的错误

import logging
# 输出内容是有等级的 : 默认处理warning级别以上的所有信息
# logging.debug('debug message')          # 调试
# logging.info('info message')            # 信息
# logging.warning('warning message')      # 警告
# logging.error('error message')          # 错误
# logging.critical('critical message')    # 批判性的

# def cal_mul(exp):
#     exp = 4*6
#     logging.debug('4*6 = 24')
#     return 24
# def cal_div():
#     pass
# def cal_add():
#     pass
# def cal_sub(exp):
#     exp = 3-24
#     logging.debug('cal_sub :3-24 = 21')
#     return 21

# def cal_inner_bracket(exp2):
#     exp2 = 3-4*6
#     ret = cal_mul(4*6)
#     exp2 = 3-24
#     ret = cal_sub(3-24)
#     logging.debug('3-4*6 = -21')
#     return -21
#
# def main(exp):
#     exp =(1+2*(3-4*6))/5
#     ret = cal_inner_bracket(3-4*6)
#     return ret
#
# logging.basicConfig(level=logging.DEBUG)
# ret = main('(1+2*(3-4))/5')
# print(ret)

# 1.无论你希望日志里打印哪些内容,都得你自己写,没有自动生成日志这种事儿
# logging.basicconfig
# 输出到屏幕
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )
# logging.warning('warning message test2')
# logging.error('error message test2')
# logging.critical('critical message test2')

# 输出到文件,并且设置信息的等级
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     filename='tmp.log',
#     level= logging.DEBUG
#
# )
# logging.debug('debug 信息错误 test2')
# logging.info('warning 信息错误 test2')
# logging.warning('warning message test2')
# logging.error('error message test2')
# logging.critical('critical message test2')



# 要记住的
# --------------------------------------------------------------------------------------------------
# 同时向文件和屏幕上输出 和 乱码
# fh = logging.FileHandler('tmp.log',encoding='utf-8')
# # fh2 = logging.FileHandler('tmp2.log',encoding='utf-8')
# sh = logging.StreamHandler()
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level= logging.DEBUG,
#     # handlers=[fh,sh,fh2]
#     handlers=[fh,sh]
# )
# logging.debug('debug 信息错误 test2')
# logging.info('warning 信息错误 test2')
# logging.warning('warning message test2')
# logging.error('error message test2')
# logging.critical('critical message test2')

# 做日志的切分
# import time
# from logging import handlers
# sh = logging.StreamHandler()
# rh = handlers.RotatingFileHandler('myapp.log', maxBytes=1024,backupCount=5)   # 按照大小做切割
# fh = handlers.TimedRotatingFileHandler(filename='x2.log', when='s', interval=5, encoding='utf-8')
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level= logging.DEBUG,
#     # handlers=[fh,sh,fh2]
#     handlers=[fh,rh,sh]
# )
# for i in range(1,100000):
#     time.sleep(1)
#     logging.error('KeyboardInterrupt error %s'%str(i))

