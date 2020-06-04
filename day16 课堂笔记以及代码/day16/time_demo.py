"""
time 模块
三大对象：
时间戳
结构化时间对象（9大字段）
字符串！！！！
"""

import time
# 获取时间戳
# 时间戳：从时间元年（1970 1 1 00:00:00）到现在经过的秒数。
# print(time.time())  # 1558314075.7787385   1558314397.275036

# 获取格式化时间对象:是九个字段组成的。
# 默认参数是当前系统时间的时间戳。
# print(time.gmtime())  # GMT:
# print(time.localtime())
# print(time.gmtime(1))       # 时间元年过一秒后，对应的时间对象

# 时间对象 -> 时间戳
# t1 = time.localtime()   # 时间对象
# t2 = time.mktime(t1)    # 获取对应的时间戳
# print(t2)
# print(time.time())


# 格式化时间对象和字符串之间的转换
# s = time.strftime("year:%Y %m %d %H:%M:%S")
# print(s)

# 把时间字符串转换成时间对象
# time_obj = time.strptime('2010 10 10','%Y %m %d')
# print(time_obj)

# 暂停当前程序,睡眠xxx秒
# time.sleep(xxx)
for x in range(5):
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    # 休眠一秒钟
    time.sleep(1)


