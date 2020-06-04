import re
from functools import reduce

def mul_div(exp): # 计算两个数的乘法或者除法
    if '*' in exp:
        a, b = exp.split('*')
        return float(a)*float(b)
    if '/' in exp:
        a, b = exp.split('/')
        return float(a) / float(b)

def exp_fmt(exp):
    while re.search('[+-]{2,}',exp):
        exp = exp.replace('--','+')
        exp = exp.replace('+-','-')
        exp = exp.replace('-+','-')
        exp = exp.replace('++','+')
    return exp

def remove_addsub(exp):
    ret = re.findall('[-+]?\d+(?:\.\d+)?',exp)
    res = reduce(lambda a,b:float(a)+float(b),ret)
    return res

def remove_muldiv(exp):   # 计算表达式中的所有的乘除法
    while True:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?',exp)
        if ret:
            son_exp = ret.group()   # 3*4  12*5
            res = mul_div(son_exp)
            exp = exp.replace(son_exp,str(res))
        else:return exp

def cal(exp):
    res = remove_muldiv(exp)   # 计算乘除
    res = exp_fmt(res)                  # 符号整理
    ret = remove_addsub(res)            # 计算加减
    return ret

def main(exp):
    exp = exp.replace(' ','')
    while True:
        ret = re.search('\([^()]+\)', exp)
        if ret:
            res = cal(ret.group())
            exp = exp.replace(ret.group(), str(res))
        else: return cal(exp)

exp = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
ret = main(exp)
print(ret)