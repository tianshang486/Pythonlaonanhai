import time
import struct
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9001))
# length = int(sk.recv(4).decode('utf-8'))
length = sk.recv(4)
length = struct.unpack('i',length)[0]
msg1 = sk.recv(length)
msg2 = sk.recv(1024)
print(msg1.decode('utf-8'))
print(msg2.decode('utf-8'))

sk.close()