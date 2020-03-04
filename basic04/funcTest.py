menu = """
1. 입금 
2. 출금 
3. 잔액조회 
4. 계좌이체 
5. 종료
"""

def atm():
    my_money = 100000
    print('*** 글로벌 은행 ATM ***')
    while True:
        check = login()
        if check == 1:
            while True:
                print(menu)
                sel = int(input("이용할 서비스를 선택하세요."))
                if sel == 1:
                    my_money = deposit(my_money)
                elif sel == 2:
                    my_money = withdraw(my_money)
                elif sel == 3:
                    showAccount(my_money)
                elif sel == 4:
                    my_money = transfer(my_money)
                else:
                    print("서비스를 종료합니다.")
                    break
        else:
            return
        print()


def login():
    db_id = 'java'
    db_pw = '1234'
    count = 0

    while True:
        if count == 3:
            print("아이디와 패스워드 3회 오류. 프로그램이 종료됩니다.")
            return 2

        id = input("ID : ")
        pw = input("PW : ")

        if db_id == id :
            if db_pw == pw :
                print("%s 님 환영합니다." % id)
                return 1
            else:
                print("패스워드가 일치하지 않습니다.")
                count += 1
        else:
            print("존재하지 않는 ID입니다.")
            count += 1


def deposit(money):
    amount = int(input("입금 금액을 입력하세요."))
    money += amount
    print("입금이 완료되었습니다.")
    print("잔액 : ", money)
    return money

def withdraw(money):
    amount = int(input("출금 금액을 입력하세요."))
    if money >= amount:
        money -= amount
        print("출금이 완료되었습니다.")
        print("잔액 : ", money)
        return money
    else:
        print("잔액이 부족합니다.")
        return money

def showAccount(money):
    print("잔액 : ", money)
def transfer(money):
    whom = input("입금할 계좌를 입력하세요.")
    amount = int(input("이체할 금액을 입력하세요."))
    if money >= amount:
        money -= amount
        print("%s님에게 %d원 이체가 완료되었습니다." % (whom,amount))
        print("잔액 : ", money)
        return money
    else:
        print("잔액이 부족합니다.")
        return money

def serv(cont):
    global my_money
    if cont == 1: #입금
        save = int(input("입금 금액을 입력하세요."))
        my_money += save
        print("입금이 완료되었습니다.")
        print("잔액 : ", my_money)
    if cont == 2: #출금
        out = int(input("출금 금액을 입력하세요."))
        if my_money >= out:
            my_money -= out
            print("출금이 완료되었습니다.")
            print("잔액 : ", my_money)
        else:
            print("잔액이 부족합니다.")
    if cont == 3: #계좌조회
        print("잔액 : ", my_money)
    if cont == 4: #계좌이체
        whom = input("입금할 계좌를 입력하세요.")
        amount = int(input("이체할 금액을 입력하세요."))
        if my_money >= amount:
            my_money -= amount
            print("%s님에게 %d원 이체가 완료되었습니다." % (whom,amount))
            print("잔액 : ", my_money)
        else:
            print("잔액이 부족합니다.")


atm()