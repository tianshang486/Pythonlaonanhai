
import socket
server = socket.socket()
server.bind(('127.0.0.1',8001))
server.listen(2)
while 1:
    conn, addr = server.accept()

    from_browser_msg = conn.recv(1024).decode('utf-8')
    print(from_browser_msg)

    # conn.send(b'hello')
    conn.send(b'HTTP/1.1  200 ok\r\n\r\n')
    # conn.send(b'<h1>s22 welcome to hongkong</h1>')
    with open('111.html','rb') as f:
        data = f.read()

    conn.send(data)

    conn.close()

# server.close()
























