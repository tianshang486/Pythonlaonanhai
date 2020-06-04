# import hashlib
# hashlib.md5()

# md5
# s1 = 'kfdslfjasdlfgjsdlgkhsdafkshdafjksdfsdkfhjsdafj老fhdskafhsdkjfdsa男孩教育'
# import hashlib
# ret = hashlib.md5()
# ret.update(s1.encode('utf-8'))
# print(ret.hexdigest(),)

# 相关练习
import hashlib
# def MD5(pwd):
#     ret = hashlib.md5()
#     ret.update(pwd.encode('utf-8'))
#     return ret.hexdigest()
#
#
# def register():
#     username = input('请输入用户名:').strip()
#     password = input('请输入密码:').strip()
#     password_md5 = MD5(password)
#     with open('register',encoding='utf-8',mode='a') as f1:
#         f1.write(f'\n{username}|{password_md5}')
#
# register()
#
# def login():
#     username = input('请输入用户名:').strip()
#     password = input('请输入密码:').strip()
#     password_md5 = MD5(password)
#

# 普通加密

import hashlib
# s1 = 'kfdslfjasdlfgjsdlgkhsdafkshdafjksdfsdkfhjsdafj老fhdskafhsdkjfdsa男孩教育'
# s2 = 'kfdslfjasdlfgjsdlgkhsdafkshdafjksdfsdkfhjsdafj老fhdskafhsdkjfdsa男孩教育'
# ret = hashlib.md5()
# ret.update(s2.encode('utf-8'))
# print(ret.hexdigest())  # 18f127c24462dd59287798ea5c0c0c2f  18f127c24462dd59287798ea5c0c0c2f
# 123456:  18f127c24462dd59258898ea5c0c0c2f
# 000000:  18f127c24462dd59258898we5c0c0c2f

# s2 = '19890425'
# ret = hashlib.md5()
# ret.update(s2.encode('utf-8'))
# print(ret.hexdigest())  # 6e942d04cf7ceeeba09e3f2c7c03dc44

# 加盐

# s2 = '19890425'
# ret = hashlib.md5('太白金星'.encode('utf-8'))
# ret.update(s2.encode('utf-8'))
# print(ret.hexdigest())  # 84c31bbb6f6f494fb12beeb7de4777e1


# 动态的盐
# s2 = '19890425'
# ret = hashlib.md5('太白金星'[::2].encode('utf-8'))
# ret.update(s2.encode('utf-8'))
# print(ret.hexdigest())  # 84c31bbb6f6f494fb12beeb7de4777e1


# sha系列  金融类,安全类.用这个级别.
# 随着sha系列数字越高,加密越复杂,越不易破解,但是耗时越长.
# s2 = '198fdsl;fdsklgfjsdlgdsjlfkjsdalfksjdal90425'
# ret = hashlib.sha3_512()
# ret.update(s2.encode('utf-8'))
# print(ret.hexdigest())  # 4d623c6701995c989f400f7e7eef0c4fd4ff15194751f5cb7fb812c7d42a7406ca0349ea3447d245ca29b48a941e2f2f66579fb090babb73eb2b446391a8e102



# 文件的校验

# linux中一切皆文件: 文本文件,非文本文件,音频,视频,图片....
# 无论你下载的视频,还是软件(国外的软件),往往都会有一个md5值


# 6217ce726fc8ccd48ec76e9f92d15feecd20422c30367c6dc8c222ab352a3ec6  *pycharm-professional-2019.1.2.exe

# s1 = '我叫太白金星 今年18岁'
# ret = hashlib.sha256()
# ret.update(s1.encode('utf-8'))
# print(ret.hexdigest())  # 54fab159ad8f0bfc5df726a70332f111c2c54d31849fb1e4dc1fcc176e9e4cdc
#
# ret = hashlib.sha256()
# ret.update('我叫'.encode('utf-8'))
# ret.update('太白金星'.encode('utf-8'))
# ret.update(' 今年'.encode('utf-8'))
# ret.update('18岁'.encode('utf-8'))
# print(ret.hexdigest()) # 54fab159ad8f0bfc5df726a70332f111c2c54d31849fb1e4dc1fcc176e9e4cdc

# low版校验:
def file_md5(path):
    ret = hashlib.sha256()
    with open(path,mode='rb') as f1:
        b1 = f1.read()
        # print(b1)
        ret.update(b1)
    return ret.hexdigest()
result = file_md5('pycharm-professional-2019.1.2.exe')
print(result)  # 6217ce726fc8ccd48ec76e9f92d15feecd20422c30367c6dc8c222ab352a3ec6

# 高大上版
