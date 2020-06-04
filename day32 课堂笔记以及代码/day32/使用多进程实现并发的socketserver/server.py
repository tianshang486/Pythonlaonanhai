import socket
from multiprocessing import Process

# def talk(sk):
#     conn,addr = sk.accept()
#     while True:
#         msg = conn.recv(1024).decode('utf-8')
#         ret = msg.upper().encode('utf-8')
#         conn.send(ret)
#     conn.close()
#
# if __name__ == '__main__':
#     sk = socket.socket()
#     sk.bind(('127.0.0.1',9001))
#     sk.listen()
#     Process(target = talk,args=(sk,)).start()
#     Process(target = talk,args=(sk,)).start()
#     sk.close()

def talk(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        ret = msg.upper().encode('utf-8')
        conn.send(ret)
    conn.close()

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1',9001))
    sk.listen()
    while True:
        conn, addr = sk.accept()
        Process(target = talk,args=(conn,)).start()
    sk.close()