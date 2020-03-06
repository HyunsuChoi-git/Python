class A:
    pass

print(A.mro())

class B(A):
    pass
print(B.mro())

class C(A):
    pass
print(C.mro())

class D(B, C):
    pass
print(D.mro())


class E(C,B):
    pass
print(E.mro())

class F(D,E):
    pass
print(F.mro())