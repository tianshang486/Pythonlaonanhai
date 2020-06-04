from django import template

register = template.Library()  #register固定的名字,注册器

# @register.filter
# def oo(v1,v2):  #不带参数的过滤器
#     s = v1 + 'xxoo'

#     return s

@register.filter
def oo(v1,v2):  #带参数的过滤器
    s = v1 + v2
    return s

@register.simple_tag
def mytag(v1,v2,v3):
    s = v1 + '和B哥' + v2 + v3
    return s


@register.inclusion_tag('inclusiontag.html')
def func(v1):

    return {'oo':v1}















