class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
#/////////////////////////////////

pika = Person("pika", 10)
print(pika.name)
print(pika.age)

class Character:
    count = 0 # 캐릭터 객체의 갯수를 카운트할 변수

    def __init__(self, name):
        self.name = name
        print("%s가 만들어지는 중 .." % self.name)
        Character.count += 1
    def die(self):
        print("%s가 죽었습니다." % self.name)
        Character.count -= 1
    def showInfo(self):
        print("캐릭터의 갯수는 %d이다." % Character.count)
#//////////////////////////////////////////////////

elf1 = Character("엘프1")
elf2 = Character("엘프2")
elf3 = Character("엘프3")
elf1.showInfo()
elf2.die()
elf1.showInfo()