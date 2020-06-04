# 生成一个随机字符串
# import os
# ret = os.urandom(16)
# print(ret)

# import hashlib
# sha = hashlib.sha1(密钥)
# sha.update(随机字符串)
# 结果 = sha.hexdigest()

# import os
# import hmac   # 替代hashlib模块的
#
# h = hmac.new(b'alex_sb',os.urandom(32))
# ret = h.digest()
# print(ret)