# import time
# for i in range(0,101,2):   # 0,2,4,6,8
#      time.sleep(0.1)
#      char_num = i//2      #打印多少个'*'  2//2
#      if i == 100:
#           per_str = '\r%s%% : %s\n' % (i, '*' * char_num)
#      else:
#           per_str = '\r%s%% : %s'%(i,'*'*char_num)
#      print(per_str,end='', flush=True)

def processBar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    if rate_num == 100:
        r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
    else:
        r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
    print(r,flush=True,end='')
# processBar(204800,101028199)
# import time
# time.sleep(0.5)
# processBar(2048000,101028199)
# client端
# 下载  101028199
# 1024/101028199 百分比
# 2048/101028199 百分比
# 20480/101028199 百分比
# 204800/101028199 百分比
