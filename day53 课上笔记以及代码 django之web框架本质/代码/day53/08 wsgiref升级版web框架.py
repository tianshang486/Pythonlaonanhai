import time
from threading import Thread
from wsgiref.simple_server import make_server
from showdata import showdata
from jinja2 import Template

def html():
    # time_tag = str(time.time())
    userinfo_data = showdata()

    with open('08 jinja2搞基版动态web框架.html', 'r',encoding='utf-8') as f:
        data = f.read()
    # print(data)
    tem = Template(data)
    print(userinfo_data)
    # {'userinfo': {'id':1,'name':'dazhuang','age':18}}
    data = tem.render({'userinfo':userinfo_data})
    # data = data.replace('$xxoo$',userinfo_data['name'])
    data = data.encode('utf-8')
    return data

def css():
    with open('test.css', 'rb') as f:
        data = f.read()
    return data

def js():
    with open('test.js', 'rb') as f:
        data = f.read()
    return data

def jpg():
    with open('1.jpg', 'rb') as f:
        data = f.read()
    return data

def ico():
    with open('22.ico', 'rb') as f:
        data = f.read()
    return data

urlpatterns = [
    ('/',html),
    ('/test.css',css),
    ('/1.jpg',jpg),
    ('/test.js',js),
    ('/22.ico',ico),
]

def application(environ, start_response):
    # print(environ)
    # conn.send(b'HTTP/1.1 200 ok\r\n\r\nxxxx')
    start_response('200 OK', [('k1','v1'),('k2','v2')])
    # print(environ['PATH_INFO'])
    path = environ['PATH_INFO']

    for i in urlpatterns:
        if path == i[0]:
            ret = i[1]()
            break
    else:
        ret = b'404 not found!!!!'
    return [ret]

httpd = make_server('127.0.0.1', 8080, application)

print('Serving HTTP on port 8080...')
httpd.serve_forever()









