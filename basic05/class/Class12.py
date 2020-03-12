# 객체의 구조화

class Person:
    #생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        pass
    def eat(self):
        pass
#////////////////////////////////////

p1 = Person("피카츄",2)
print(p1.name)
print(p1.age)

class Postman(Person):
    def __init__(self, name, age, *args, **kwargs):
        super().__init__(name, age)
        # **kwargs가 키=밸류 형태의 인자들을 한번에 받아서
        #items() 함수를 이용하여 값을 꺼내고
        #반복문을 통해 i,j 에 키, 밸류 형태로 데이터 담는다.
        # setattr() 함수로 ---> 인스턴스변수로 만든다.
        # self는 생성자를 호출하는 객체가 된다.
        for i, j in kwargs.items():
            setattr(self, i, j)
        self.data= []
        for i in args:
            self.data.append(i)


#////////////////////////////////////
post1 = Postman("우체부1", 30, gender="F", section="A")
print(post1.name)
print(post1.gender)

post2 = Postman("우체부2", 32, 1,2,3,4,5, gender="M", section="B")
print(post2.data)

#/////////////////////////////////////

dic = dict()
for i in range(3):

    lst = list()
    for j in range(50):
        lst.append(Postman(f"postman{j+1}", 20+j, section="B", worktime="8Hours"))
    dic.update({f"postOffice{i+1}":lst})

print(dic["postOffice1"][40].name)
print(dic["postOffice1"][40].age)
print(dic["postOffice1"][40].section)
print(dic["postOffice1"][40].worktime)
