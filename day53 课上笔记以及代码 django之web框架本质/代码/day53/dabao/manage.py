from urls import urlpatterns
from wsgiref.simple_server import make_server
def application(environ, start_response):
    # print(environ)
    # conn.send(b'HTTP/1.1 200 ok\r\n\r\nxxxx')
    start_response('200 OK', [('k1','v1'),('k2','v2')])
    # print(environ['PATH_INFO'])
    path = environ['PATH_INFO']
    for i in urlpatterns:
        if path == i[0]:
            ret = i[1](environ)
            break
    else:
        ret = b'404 not found!!!!'
    return [ret]
httpd = make_server('127.0.0.1', 8080, application)
print('Serving HTTP on port 8080...')
httpd.serve_forever()









