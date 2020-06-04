import requests
from multiprocessing import Process,Queue
url_dic = {
    'cnblogs':'https://www.cnblogs.com/Eva-J/articles/8253549.html',
    'douban':'https://www.douban.com/doulist/1596699/',
    'baidu':'https://www.baidu.com',
    'gitee':'https://gitee.com/old_boy_python_stack__22/teaching_plan/issues/IXSRZ',
}

def producer(name,url,q):
    ret = requests.get(url)
    q.put((name,ret.text))

def consumer(q):
    while True:
        tup = q.get()
        if tup is None:break
        with open('%s.html'%tup[0],encoding='utf-8',mode='w') as f:
            f.write(tup[1])

if __name__ == '__main__':
    q = Queue()
    pl = []
    for key in url_dic:
        p = Process(target=producer,args=(key,url_dic[key],q))
        p.start()
        pl.append(p)
    Process(target=consumer,args=(q,)).start()
    for p in pl:p.join()
    q.put(None)

    # join n 个进程   n个进程必须都执行完才继续
    # for i in range(4):
    #     print(q.get())


# 同步阻塞
    # 调用函数必须等待结果\cpu没工作 input sleep recv accept connect get
# 同步非阻塞
    # 调用函数必须等待结果\cpu工作 - 调用了一个高计算的函数 strip eval('1+2+3') sum max min sorted
# 异步阻塞
    # 调用函数不需要立即获取结果,而是继续做其他的事情,在获取结果的时候不知道先获取谁的,但是总之需要等(阻塞)
# 异步非阻塞
    #  调用函数不需要立即获取结果,也不需要等 start() terminate()











