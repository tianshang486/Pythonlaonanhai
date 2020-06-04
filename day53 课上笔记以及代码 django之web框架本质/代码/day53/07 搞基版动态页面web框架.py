
import socket
from threading import Thread
import time
server = socket.socket()
ip_port = ('127.0.0.1',8001)
server.bind(ip_port)
server.listen()

def html(conn):
    time_tag = str(time.time())
    with open('07 搞基版动态web框架.html', 'r',encoding='utf-8') as f:
        data = f.read()
    print(data)
    data = data.replace('$xxoo$',time_tag)
    data = data.encode('utf-8')
    conn.send(data)
    conn.close()

def css(conn):
    with open('test.css', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()

def js(conn):

    with open('test.js', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()

def jpg(conn):
    with open('1.jpg', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()

def ico(conn):
    with open('22.ico', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()

urlpatterns = [
    ('/',html),
    ('/test.css',css),
    ('/1.jpg',jpg),
    ('/test.js',js),
    ('/22.ico',ico),
]

while 1:
    conn,addr = server.accept()
    from_client_msg = conn.recv(1024)
    # print(from_client_msg.decode('utf-8'))
    request_str = from_client_msg.decode('utf-8')
    path = request_str.split('\r\n')[0].split(' ')[1]


    print(path)
    conn.send(b'HTTP/1.1 200 ok\r\nk1:v1\r\n\r\n')
    # conn.send(b'hello girl')
    for i in urlpatterns:
        if path == i[0]:
            # i[1](conn)
            t = Thread(target=i[1],args=(conn,))
            t.start()




































