import os
import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()

    def run(self):
        time.sleep(3)
        print(os.getppid(),os.getpid(),self.a,self.b,self.c)

if __name__ == '__main__':
    p = MyProcess(1,2,3)
    p.start()
    print(p.pid,p.ident)
    print(p.name)
    print(p.is_alive())
    p.terminate()   # 强制结束一个子进程   同步  异步非阻塞
    print(p.is_alive())
    time.sleep(0.01)
    print(p.is_alive())
