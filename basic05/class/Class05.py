class Cashier:
    #//클래스변수
    count = 0
    discount = 0.3
    total = 0

    #생성자
    def __init__(self, price, number):
        self.price = price #//제품가격
        self.number = number #//제품수량
        Cashier.count += 1

    def calculator(self):
        #//정가로 지불해야하는 금액
        self.pay = self.price * self.number
        #//할인받아 지불해야하는 총 금액
        self.dc_pay = self.pay - (self.pay * Cashier.discount)

    def display(self):
        print(Cashier.count, "번째 제품입니다.")
        print("정가 : ", self.price)
        print("수량 : ", self.number)
        print("가격 : ", self.pay)
        print("할인가격 : ", self.dc_pay)

    @staticmethod
    def message():
        print("어서오세요~")
        print("할인중입니다!!")

    @classmethod
    def update(cls, value):
        while value >= 1 or value <= 0:
            value = float(input("할인율을 다시 입력하세요."))
        cls.discount = value  #//cls. --> Cashier. 과 같음

#///////////////////////////////////////////

product1 = Cashier(1000,5)
product1.calculator()
product1.display()
print()
product2 = Cashier(5000,10)
product2.calculator()
product2.display()
