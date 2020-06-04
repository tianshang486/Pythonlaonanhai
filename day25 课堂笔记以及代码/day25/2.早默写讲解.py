# Queue队列 : 先进先出 FIFO(FIRST IN FIRST OUT)
# put
# get
# class Queue:
#     def __init__(self):
#         self.l = []
#     def put(self,item):
#         self.l.append(item)
#     def get(self):
#         return self.l.pop(0)
# q = Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())

# 假设你希望一个类的多个对象之间 的某个属性 是各自的属性,而不是共同的属性
# 这个时候我们要把变量存储在对象的命名空间中,不能建立静态变量,
# 建立静态变量是所有的对象共同使用一个变量

# class Stack:
#     def __init__(self):
#         self.l = []
#     def put(self,item):
#         self.l.append(item)
#     def get(self):
#         return self.l.pop()
#
# s1 = Stack()
# s2 = Stack()
# s1.put(1)
# s2.put('a')
# s2.put('b')
# s2.put('c')
# s1.put(2)
# s1.put(3)
# print(s2.get())
# print(s1.get())
# print(s2.get())
# print(s2.get())
# print(s1.get())
# s1.put(4)
# print(s1.get())
# print(s1.get())

# 方法一
# class Foo:
#     def __init__(self):
#         self.l = []
#
#     def put(self, item):
#         self.l.append(item)
#
#
# class Queue(Foo):
#     def get(self):
#         return self.l.pop(0)
#
#
# class Stack(Foo):
#     def get(self):
#         return self.l.pop()

# 方法二:
# class Foo:
#     def __init__(self):
#         self.l = []
#
#     def put(self,item):
#         self.l.append(item)
#
#     def get(self):
#         return self.l.pop() if self.index else self.l.pop(0)
#
# class Queue(Foo):
#     def __init__(self):
#         self.index = 0
#         Foo.__init__(self)
#
# class Stack(Foo):
#     def __init__(self):
#         self.index = 1
#         Foo.__init__(self)

# 方法三
class Foo:
    def __init__(self):
        self.l = []

    def put(self, item):
        self.l.append(item)

    def get(self):
        return self.l.pop()


class Queue(Foo):
    def get(self):
        return self.l.pop(0)

class Stack(Foo):pass

class Mypickle:
    pass

import pickle
class Mypickle:
    def __init__(self,path):
        self.file = path
    def dump(self,obj):
        with open(self.file, 'ab') as f:
            pickle.dump(obj, f)
    def load(self):
        with open(self.file,'rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
    # def load(self):
    #     l = []
    #     with open(self.file,'rb') as f:
    #         while True:
    #             try:
    #                 l.append(pickle.load(f))
    #             except EOFError:
    #                 break
    #     return l

# pic = Mypickle('pickle_file')
# s1 = Stack()
# s1.put('aaa')
# s1.put(123)
# s1.put(456)
# pic.dump(s1)
# s2 = Stack()
# s2.put('aaa')
# s2.put(123)
# s2.put(456)
# pic.dump(s2)
# for i in pic.load():
#     print(i.l)


