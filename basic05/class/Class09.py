class A:
    def hello(self):
        print("helloAAAA")

class B(A):
    #//오버라이딩
    def hello(self):
        print("helloBBBB")

class C(A):
    #//오버라이딩
    def hello(self):
        print("helloCCCC")

class D(B,C):
    pass

#////////////////////////////////////
x = D()
x.hello()  #//helloBBBB


class F(B,C):
    def hello(self):
        super(F, self).hello()   #//helloBBBB
        super(C, self).hello()   #//helloAAAA
        super(B, self).hello()   #//helloCCCC

x = F()
print(F.mro())
x.hello()

