# python3x str为例，模拟将一句话通过网络发送给对方。
# content就是那句话。
# content = input(">>>")
# print(content,type(content))
# # bytes  #
# b = b'hello'
# # print(b.upper())
# print(b,type(b))

# s1 = '中国'
# b = b'\xe4\xb8\xad\xe5\x9b\xbd'
# print(b)

# str ---> bytes\
# s1 = '中国'
# b1 = s1.encode('utf-8')  # 编码
# print(b1,type(b1))  # b'\xe4\xb8\xad\xe5\x9b\xbd'
# # b1 = s1.encode('gbk')  # 编码  # b'\xd6\xd0\xb9\xfa' <class 'bytes'>
# # bytes---->str
# b1 = b'\xe4\xb8\xad\xe5\x9b\xbd'
# s2 = b1.decode('utf-8')  # 解码
# print(s2)


# gbk ---> utf-8
b1 = b'\xd6\xd0\xb9\xfa'
s = b1.decode('gbk')
# print(s)
b2 = s.encode('utf-8')
print(b2)  # b'\xe4\xb8\xad\xe5\x9b\xbd'
