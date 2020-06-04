import socket
friend_lst = {'alex':'32','太白':'33'}
sk =socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9001))
while True:
    msg,addr = sk.recvfrom(1500)
    msg = msg.decode('utf-8')
    name,message  = msg.split('|',1)
    print('\033[1;%sm %s:%s\033[0m'%(friend_lst.get(name,'30'),name,message))
    content = input('>>>')
    sk.sendto(content.encode('utf-8'),addr)













