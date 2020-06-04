# 分组命名
# import re
# ret = re.search('\d(\d)\d(\w+?)(\d)(\w)\d(\d)\d(?P<name1>\w+?)(\d)(\w)\d(\d)\d(?P<name2>\w+?)(\d)(\w)',
#           '123abc45678agsf_123abc45678agsf123abc45678agsf')
#
# print(ret.group('name1'))
# print(ret.group('name2'))

# (?P<名字>正则表达式)
# ret.group('名字')

# 分组命名的引用
# import re
# exp= '<abc>akd7008&(&*)hgdwuih</abb>008&(&*)hgdwuih</abd>'
# ret= re.search('<(?P<tag>\w+)>.*?</(?P=tag)>',exp)
# print(ret)

import re
# exp= '<abc>akd7008&(&*)hgdwuih</abc>008&(&*)hgdwuih</abd>'
# ret= re.search(r'<(\w+)>.*?</\1>',exp)
# ret= re.search('<(\w+)>.*?</\\1>',exp)
# print(ret)

import re
# ret=re.findall(r"\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
# ret = ['1', '2', '60', '', '5', '4', '3','','']
# ret.remove('')
# print(ret)
# ret = filter(lambda n:n,ret)
# print(list(ret))

# 分组命名(?P<组名>正则) (?P=组名)
# 有的时候我们要匹配的内容是包含在不想要的内容之中的,
    # 只能先把不想要的内容匹配出来,然后再想办法从结果中去掉