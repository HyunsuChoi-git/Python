class Tv:
    #//클래스 변수
    power = False
    color = "white"
    channel = 1

    def onOff(self):
        #//power = not self.power ---> 지역변수
        #//인스턴스변수(객체가 가진 변수)
        self.power = not self.power

    def channelUp(self):
        self.channel += 1

    def channelDown(self):
        self.channel -= 1

    def remote(self, num):
        self.channel = num

    def showInfo(self):
        print("power : ", self.power)
        print("channel : ", self.channel)
        print("color : ", self.color)

###########################################

my = Tv()
my.onOff()
my.color = "red"
my.remote(10)
my.showInfo()
print()

mom = Tv()
mom.showInfo()
mom.onOff()
