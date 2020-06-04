# 文件操作
class File:
    lst = [('读文件','read'), ('写文件','write'),
           ('删除文件','remove'),( '文件重命名','rename'),
           ('复制','copy'),('移动文件','move')]
    def __init__(self,filepath):
        self.filepath = filepath
    def write(self):
        print('in write func')
    def read(self):
        print('in read func')
    def remove(self):
        print('in remove func')
    def rename(self):
        print('in rename func')
    def copy(self):
        print('in copy func')
    def move(self):
        print('in 移动文件 func')

f = File('ashkgkfj')
while True:
    for index,opt in enumerate(File.lst,1):
        print(index,opt[0])
    num = int(input('请输入您要做的操作序号>>'))
    if hasattr(f,File.lst[num-1][1]):
        getattr(f,File.lst[num-1][1])()


