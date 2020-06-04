# callable(对象)
# 对象() 能不能运行就是callable判断的事儿

class A:
    def __call__(self, *args, **kwargs):
        print('-------')

# obj = A()
# print(callable(obj))
# obj()
# A()()
# Flask框架的源码