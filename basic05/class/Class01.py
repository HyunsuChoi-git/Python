class Person:
    # //변수
    name = ""
    age = 0
    gender = ""
    blood = ""
    jumin = ""

    # //메소드
    def speak(self):
        print("말한다~~")

    def eat(self):
        print("냠냠쩝쩝")

    def showInfo(self):
        print("이름 : %s" % self.name)
        print("나이 : %s" % self.age)
        print("성별 : %s" % self.gender)

pika = Person()
pika.name = "피카츄"
pika.age = 10
pika.gender = "남자"
print(pika.name)
pika.showInfo()




