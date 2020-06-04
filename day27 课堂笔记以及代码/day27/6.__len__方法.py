class Cls:
    def __init__(self,name):
        self.name = name
        self.students = []
    def len(self):
        return len(self.students)
    def __len__(self):
        return len(self.students)
py22 = Cls('py22')
py22.students.append('杜相玺')
py22.students.append('庄博')
py22.students.append('大壮')
print(py22.len())
print(len(py22))

# class Pow:
#     def __init__(self,n):
#         self.n = n
#     # def __pow2__(self):
#     #     return self.n ** 2
#
# def pow2(obj):
#     return obj.__pow2__()
# obj = Pow(10)
# print(pow2(obj))
