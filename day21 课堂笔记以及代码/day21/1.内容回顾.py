# re模块的常用方法
    # findall(正则,待匹配字符串,flag) :  返回所有匹配项的列表
    # search : 返回一个变量,通过group取到的是第一个匹配的项
    # finditer :返回一个迭代器,通过迭代取到的是一个变量,通过group取值
    # match : 从头开始找第一个,其他和search一样

    # compile(正则):同一个正则表达式需要多次使用的时候提前编译来节省时间

    # split 通过正则表达式匹配的内容进行分割
    # sub 替换,通过正则表达式匹配的内容来进行替换
    # subn 替换,在sub的基础上,返回一个元组,第一个内容是替换结果,第二个是替换次数

# 标签匹配
# <h1>aksfgi031oq3h</h1><h2>sdhyqo-120v b,</h2>
# re.findall('<\w+>(.*?)</\w+>',exp)
# ret = re.search(r'<(\w+)>(.*?)</\1>',exp)
# ret.group(2)

# 用户输入身份证号匹配
# re.match('^[1-9]\d{14}(\d{2}[\dx])?$',ident_num)
# ^([1-9]\d{16}[\dx]|[1-9]\d{14})$

# 分组命名 取消分组优先
# (?P<组名>正则)  (?P=组名)  (?:正则)


# 2、匹配年月日日期 格式2018.12.16
# [1-9]\d{3}-(1[0-2]|0?[1-9])-([12]\d|3[01]|0?[1-9])
# [1-9]\d{3}-(1[0-2]|0?[1-9])-([12]\d|3[01]|0?[1-9])
# [1-9]\d{3}(?P<sub>[^\d])(1[0-2]|0?[1-9])(?P=sub)([12]\d|3[01]|0?[1-9])

# 7、匹配邮箱地址
# 邮箱规则
# @之前必须有内容且只能是字母（大小写）、数字、下划线(_)、减号（-）、点（.）
# @和最后一个点（.）之间必须有内容且只能是字母（大小写）、数字、点（.）、减号（-），且两个点不能挨着
# 最后一个点（.）之后必须有内容且内容只能是字母（大小写）、数字且长度为大于等于2个字节，小于等于6个字节
# taibai@oldboy..cn
# [-\w.]+@([-\da-zA-Z]+\.)+[a-zA-Z\d]{2,6}

# 8、从类似

# exp ='''<a>wahaha</a><b>banana</b><h1>qqxing</h1>'''

# 这样的字符串中，
# 1）匹配出wahaha，banana，qqxing内容。
# import re
# re.findall('<\w+>(.+?)</\w+>',exp)
# 2）匹配出a,b,h1这样的内容
# import re
# ret = re.finditer(r'<(\w+)>.+?</\1>',exp)
# print([i.group(1) for i in ret])

# 9、1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-3*2))
# 1）从上面算式中匹配出最内层小括号以及小括号内的表达式
# \([^()]+\)

# 10、从类似9-25/3+7/399/42998+10568/14的表达式中匹配出从左到右第一个乘法或除法
# \d+(\.\d+)?[*/]-?\d+(\.\d+)?


# 11
# 从lianjia.html（html文件在群文件中）中匹配出标题，户型和面积，结果如下：
# [('金台路交通部部委楼南北大三居带客厅 单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', '2室1厅', '94.14平米')]
# par = '<div class="title">.*?<a class=.*?>(?P<name>.*?)</a>.*?<span class="divide">/</span>(?P<room>.*?)<span class="divide">/</span>(?P<area>.*?)<span'
# import re
# with open('lianjia.html',encoding='utf-8') as f:
#     content = f.read()
# ret = re.findall(par,content,flags=re.S)
# print(ret)
# ret = re.finditer(par,content,flags=re.S)
# for i in ret:
#     print(i.group('name'),i.group('room'),i.group('area'))

