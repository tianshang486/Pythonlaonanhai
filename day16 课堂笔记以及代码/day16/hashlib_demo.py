"""
md5加密算法:

给一个数据加密的三大步骤:
1.获取一个加密对象
2.使用加密对象的update,进行加密,update方法可以调用多次
3.通常通过hexdigest获取加密结果,或digest()方法.

"""
import hashlib
# 获取一个加密对象
# m = hashlib.md5()
# # 使用加密对象的update,进行加密
# m.update('abc中文'.encode('utf-8'))
# m.update('def'.encode('utf-8'))

# 通过hexdigest获取加密结果
# res = m.hexdigest()
# res = m.digest()
# print(res)      # 1af98e0571f7a24468a85f91b908d335

# 给一个数据加密,
# 验证:用另一个数据加密的结果和第一次加密的结果对比.
# 如果结果相同,说明原文相同.如果不相同,说明原文不同.

# 不同加密算法:实际上就是加密结果的长度不同;
# s = hashlib.sha224()
# s.update(b'abc')
# print(len(s.hexdigest()))
#
# print(len(hashlib.md5().hexdigest()))
# print(len(hashlib.sha256().hexdigest()))

# 在创建加密对象时,可以指定参数,称为salt.
# m = hashlib.md5(b'abc')
# print(m.hexdigest())
#
# m = hashlib.md5()
# m.update(b'abc')
# print(m.hexdigest())

# m = hashlib.md5()
# m.update(b'abc')
# m.update(b'def')
# print(m.hexdigest())
#
#
#
# m = hashlib.md5()
# m.update(b'abcdef')
# print(m.hexdigest())

# 注册,登录程序:


def get_md5(username,passwd):
    m = hashlib.md5(username[::-1].encode('utf-8'))
    m.update(username.encode('utf-8'))
    m.update(passwd.encode('utf-8'))
    return m.hexdigest()


def register(username,passwd):
    # 加密
    res = get_md5(username,passwd)
    # 写入文件
    with open('login',mode='at',encoding='utf-8') as f:
        f.write(res)
        f.write('\n')

    # username:xxxxxx

def login(username,passwd):
    # 获取当前登录信息的加密结果
    res = get_md5(username, passwd)
    # 读文件,和其中的数据进行对比
    with open('login',mode='rt',encoding='utf-8') as f:
        for line in f:
            if res == line.strip():
                return True
        else:
            return False

while True:
    op = int(input("1.注册 2.登录 3.退出"))
    if op == 3 :
        break
    elif op == 1:
        username = input("输入用户名:")
        passwd = input("输入密码:")
        register(username,passwd)
    elif op == 2:
        username = input("输入用户名:")
        passwd = input("输入密码:")
        res = login(username,passwd)
        if res:
            print('登录成功')
        else:
            print('登录失败')


