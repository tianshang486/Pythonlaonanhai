import os
import json
import socket
# 发送
sk = socket.socket()
# sk.connect(('192.168.14.109',9012))
sk.connect(('127.0.0.1',9001))

# 文件名\文件大小
abs_path = r'D:\python22期\day28 课上视频\3.网络基础概念.mp4'
filename = os.path.basename(abs_path)
filesize = os.path.getsize(abs_path)
dic = {'filename':filename,'filesize':filesize}
str_dic = json.dumps(dic)
sk.send(str_dic.encode('utf-8'))

with open(abs_path,mode = 'rb') as f:
    while filesize>0:
        content = f.read(1024)
        filesize -= len(content)
        sk.send(content)
sk.close()