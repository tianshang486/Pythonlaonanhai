class A:
    role = '法师'
    def func1(self):pass
    def func2(self):pass
class B:pass
class C(B,A):pass
print(A.__base__)
print(C.__base__)
print(C.__bases__)
print(A.__dict__)
print(A.__name__)
print(A.__class__)
print(B.__class__)
print(C.__class__)
print(C.__module__)