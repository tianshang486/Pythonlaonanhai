import json
import struct
import socket
# 接收
sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

conn,_ =sk.accept()
msg_len = conn.recv(4)
dic_len = struct.unpack('i',msg_len)[0]
msg = conn.recv(dic_len).decode('utf-8')
msg = json.loads(msg)

with open(msg['filename'],'wb') as f:
    while msg['filesize'] > 0:
        content = conn.recv(1024)
        msg['filesize'] -= len(content)
        f.write(content)
conn.close()
sk.close()

# dir
    # - file1