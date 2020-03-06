class Starbucks:
    #//클래스 변수
    logo = ""

    def say(self):
        #//메소드안 -> 인스턴스변수 or 지역변수
        #//self. 이 붙으면 인스턴스 변수
        self.msg = "안녕하세요, 스타벅스입니다."
        print(self.msg)

#////////////////////////////////////////

s1 = Starbucks()
s2 = Starbucks()
print("1호점 로고 : ",s1.logo)
print("2호점 로고 : ",s2.logo)

print("================")
#//클래스변수 : 클래스명.변수명
#//인스턴스변수에 영향을 미친다.
Starbucks.logo = "Star"
print("본사 로고 : ",Starbucks.logo)
print("1호점 로고 : ",s1.logo)
print("2호점 로고 : ",s2.logo)

print("================")
#//인스턴스변수 : 인스턴스변수명.변수명
s1.logo = "Square"
print("본사 로고 : ",Starbucks.logo)
print("1호점 로고 : ",s1.logo)
print("2호점 로고 : ",s2.logo)
print()
s2.logo = "Diamond"
print("본사 로고 : ",Starbucks.logo)
print("1호점 로고 : ",s1.logo)
print("2호점 로고 : ",s2.logo)

print("================")
s3 = Starbucks()
print("3호점 로고 : ",s3.logo)