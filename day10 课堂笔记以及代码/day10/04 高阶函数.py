# 例1：
def func1():
    print('in func1')
    print(3)

def func2():
    print('in func2')
    print(4)

func1()
print(1)
func2()
print(2)
# in func1 3 1 in func2 4 2



# 例2：
def func1():
    print('in func1')
    print(3)

def func2():
    print('in func2')
    func1()
    print(4)

print(1)
func2()
print(2)


# 例3：
def fun2():
    print(2)

    def fun3():
        print(6)

    print(4)
    fun3()
    print(8)

print(3)
fun2()
print(5)


# glbals() locals()


