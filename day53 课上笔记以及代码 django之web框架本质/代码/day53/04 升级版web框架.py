
import socket
server = socket.socket()
ip_port = ('127.0.0.1',8001)
server.bind(ip_port)
server.listen()

while 1:
    conn,addr = server.accept()
    from_client_msg = conn.recv(1024)
    # print(from_client_msg.decode('utf-8'))
    request_str = from_client_msg.decode('utf-8')
    path = request_str.split('\r\n')[0].split(' ')[1]
    print(path)
    conn.send(b'HTTP/1.1 200 ok\r\nk1:v1\r\n\r\n')
    # conn.send(b'hello girl')
    if path == '/':
        with open('04 升级版web框架.html','rb') as f:
            data = f.read()
        conn.send(data)
        conn.close()
    elif path == '/test.css':
        with open('test.css','rb') as f:
            data = f.read()
        conn.send(data)
        conn.close()
    elif path == '/1.jpg':
        with open('1.jpg','rb') as f:
            data = f.read()
        conn.send(data)
        conn.close()

    elif path == '/test.js':
        with open('test.js','rb') as f:
            data = f.read()
        conn.send(data)
        conn.close()
    elif path == '/22.ico':
        with open('22.ico','rb') as f:
            data = f.read()
        conn.send(data)
        conn.close()

































