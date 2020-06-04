import socket

sk = socket.socket()          # 创建一个server端的对象
sk.bind(('127.0.0.1',9001))  # 给server端绑定一个地址
sk.listen()                   # 开始监听(可以接收)客户端给我的连接了

conn,addr = sk.accept()  # 建立连接 conn是连接
conn.send(b'hello')
msg = conn.recv(1024)
print(msg)
conn.close()     # 关闭连接

sk.close()