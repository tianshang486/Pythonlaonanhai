import socket

sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9001))
while True:
    msg,addr= sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    msg = input('>>>')
    sk.sendto(msg.encode('utf-8'),addr)


