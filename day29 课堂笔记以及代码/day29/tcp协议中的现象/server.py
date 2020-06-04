import struct
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

conn,addr = sk.accept()
msg1 = input('>>>').encode()
msg2 = input('>>>').encode()
# num = str()  # '10001'
# ret = num.zfill(4)    # '0006'
# conn.send(ret.encode('utf-8'))
blen = struct.pack('i',len(msg1))
conn.send(blen)
conn.send(msg1)
conn.send(msg2)
conn.close()
sk.close()

# 粘包现象
# 只出现在tcp协议中,因为tcp协议 多条消息之间没有边界,并且还有一大堆优化算法
# 发送端 : 两条消息都很短,发送的间隔时间也非常短
# 接收端 : 多条消息由于没有及时接收,而在接收方的缓存短堆在一起导致的粘包

# 解决粘包问题的本质 :设置边界












