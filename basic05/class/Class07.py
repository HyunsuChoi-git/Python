class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print("부모!!")
        print("이름:", self.name)
        print("나이:", self.age)

 #//////////////////////////////////

class Student(Person):
     #//메소드 오버라이딩
     def __init__(self, name, age, sdCode):
        #// self.name = name
        #// self.age = age
        #//부모의 생성자에 매개변수를 던져 호출한다
        super().__init__(name,age)
        self.sdCode = sdCode

     #//메소드 오버라이딩
     def showInfo(self):
         print("자식!!")
         #// print("이름 :", self.name)
         #// print("나이 :", self.age)
         super().showInfo()
         print("학번 :", self.sdCode)

pika = Student("학생", 10, 20200306)
pika.showInfo()