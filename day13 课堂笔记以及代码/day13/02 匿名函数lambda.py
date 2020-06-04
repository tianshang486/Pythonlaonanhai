# 匿名函数：一句话函数，比较简单的函数。

def func(a,b):
    return a + b
# 构建匿名函数
func1 = lambda a,b: a + b
print(func1(1,2))

# 接收一个可切片的数据，返回索引为0与2的对应的元素（元组形式）。
func2 = lambda a: (a[0],a[2])
print(func2([22,33,44,55]))
# 写匿名函数：接收两个int参数，将较大的数据返回。
# def func(a,b): return a if a > b else b
lambda a,b: a if a > b else b