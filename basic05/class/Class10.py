class Character:
    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print("player가 생성되었습니다.")

    def __call__(self, *args, **kwargs):
        print("hp: %d, attack: %d, defence: %d" % (self.hp, self.attack, self.defence))

    def __getitem__(self, item):
        print(item)
        if item == "hp":
            return self.hp
        elif item == "attack":
            return self.attack
        elif item == "defence":
            return self.defence
        else:
            return "존재하지 않는 변수입니다."

#////////////////////////////////////////////

a = Character(10,20,30)
b = Character(100,200,300)

#call
a()
b()

#getitem
print(a["hp"])
print(a["attack"])
print(a["defence"])





print("=========end=========")