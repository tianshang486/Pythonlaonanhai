
from collections import OrderedDict

d = OrderedDict()

d['k1'] = 'v1'
d['k2'] = 'v2'

# print(d['k1'])
d1 = {}
for i in range(1000):
    d1['k%s'%i] = i

print(d1)

# print(d)
print(d.keys())



