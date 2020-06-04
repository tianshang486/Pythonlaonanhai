
from showdata import showdata
from jinja2 import Template
# 逻辑函数就这么写
# def ico():
#     with open('static/img/22.ico', 'rb') as f:
#         data = f.read()
#     return data

def f1(environ):
    print(environ['PATH_INFO'])
    with open('templates/test.html','rb') as f:
        data =f.read()
    return data


