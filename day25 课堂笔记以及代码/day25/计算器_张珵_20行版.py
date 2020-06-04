import re
def calculator(s):
    def two_num_cal(s):#给定str格式的两个数字（可能是整数或小数）组成的四则运算表达式（可能包含多余的+或-，如'3.5346*-23.2354'、'-3.5346-23.2354'），返回float型的计算结果
        ret=re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)',s)
        if ret.group(2)=='*': return float(ret.group(1))*float(ret.group(3))
        elif ret.group(2)=='/': return float(ret.group(1))/float(ret.group(3))
        elif ret.group(2)=='+': return float(ret.group(1))+float(ret.group(3))
        elif ret.group(2)=='-': return float(ret.group(1))-float(ret.group(3))
    while not re.search(r'^[+-]?\d+(\.\d+)?$',s):#当s不能转化为float型时，执行此while循环
        while re.search('[+-]{2,}',s): s = s.replace('++', '+').replace('--', '+').replace('+-', '-').replace('-+', '-') # 循环替换表达式中多余的+-号
        ret1 = re.search(r'[(][^()]+[)]', s) # 匹配首个最内层小括号，递归计算其值，将结果替换至原字符串
        if ret1:
            s = s[:ret1.span()[0]] + str(calculator(ret1.group()[1:len(ret1.group())-1])) + s[ret1.span()[1]:]
        ret2 = re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?', s) # 匹配首个乘法或除法，将结果替换至原字符串
        if ret2:
            s = s[:ret2.span()[0]] + str(two_num_cal(ret2.group())) + s[ret2.span()[1]:]
        ret3=re.search(r'[+-]?(\d+(\.\d+)?[+-]\d+(\.\d+)?)', s) # 匹配首个加法或减法，将结果替换至原字符串
        if ret2==None and ret3:
            s = s[:ret3.span()[0]] + str(two_num_cal(ret3.group())) + s[ret3.span()[1]:]
    return float(s)