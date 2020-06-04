import struct

num1 = 129469649
num2 = 123
num3 = 8

ret1 = struct.pack('i',num1)
print(len(ret1))
ret2 = struct.pack('i',num2)
print(len(ret2))
ret3 = struct.pack('i',num3)
print(len(ret3))

print(struct.unpack('i',ret1))
print(struct.unpack('i', ret2))
print(struct.unpack('i', ret3))