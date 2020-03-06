class Student1:
    def python(self):
        print("재미있는 파이썬!!")

class Student2:
    def c(self):
        print("재미있는 C언어!!")

class Student3:
    def java(self):
        print("재미있는 자바!!")

class Pikachu(Student1,Student2,Student3):
    pass

#////////////////////////////////

pika = Pikachu()
