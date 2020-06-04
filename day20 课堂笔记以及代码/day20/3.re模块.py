# findall
# search
import re
# split
# ret = re.split('\d+','alex222wusir')
# ret = re.split('\d(\d)\d','alex123wusir')
# print(ret)

# sub  替换
# ret = re.sub('\d+','H','alex123wusir456',1)
# print(ret)

# subn
# ret = re.subn('\d+','H','alex123wusir456')
# print(ret)

# match  用户输入的内容匹配的时候,要求用户输入11位手机号码,^手机号正则$
# match('手机号正则$','123eva456taibai')  规定这个字符号必须是什么样的
# search('^手机号正则$','123eva456taibai') 用来寻找这个字符串中是不是含有满足条件的子内容

# ret = re.match('\d+','123eva456taibai')
# print(ret.group())

# ret = re.search('^\d+','123eva456taibai')
# print(ret.group())

# compile -- 节省代码时间的工具
    # 假如同一个正则表达式要被使用多次
    # 节省了多次解析同一个正则表达式的时间
# ret = re.compile('\d+')
# res1 = ret.search('alex37176')
# res2 = ret.findall('alex37176')
# print(res1)
# print(res2)

# finditer -- 节省空间
# ret = re.finditer('\d+','agks1ak018093')
# for i in ret:
#     print(i.group())

# 先compile(如果没有重复使用同一个正则,也不能节省时间)
# 再finditer
# ret= re.compile('\d+')
# res = ret.finditer('agks1ak018as093')
# for r in res:
#     print(r.group())

# 列表不能用insert
# 列表不能用pop(n)

# 功能
# 性能
    # 时间 :
        # 你要完成一个代码所需要执行的代码行数
        # 你在执行代码的过程中,底层程序是如何工作的
    # 空间
        # 是占用了宝贵的内存条资源
        # 影响程序的执行效率
# 用户体验






