#ATM 기계

# 1 단계: 메뉴 번호 선택하면, 메뉴 이름 출력
# 2 단계: 메뉴별 기능 구현하기
# 3 단계: 아이디와 패스워드 입력받아서 로그인하면 서비스 이용가능하게 만들기
# 4 단계: 아이디와 패스워드 3회 오류시 프로그램 강제 종료

db_id = "java"
db_pw = "1111"

menu = ["1.입금","2.출금","3.잔액 조회","4.계좌 이체","5.종료"]
my_money = 100000

print("*** 글로벌 은행 ATM ***")
i = 0
while True:
    if i == 3:
        print("아이디와 패스워드 3회 오류. 프로그램이 종료됩니다.")
        break
    if i == 5:
        print("이용해주셔서 감사합니다.")
        break

    id = input("아이디를 입력하세요")
    pw = input("비밀번호를 입력하세요")

    if db_id != id or db_pw != pw:
        print("아이디와 비밀번호를 확인하세요")
        i += 1
    elif db_id == id and db_pw == pw:
        while True:
            print(menu[0])
            print(menu[1])
            print(menu[2])
            print(menu[3])
            print(menu[4])
            print()
            menuNum = input("번호를 선택하세요.")
            if menuNum == "1": #입금
                print(menu[0])

                put = int(input("입금하실 금액을 입력하세요."))
                my_money += put
                print("총 잔액 :", my_money)
                print()
            elif menuNum == "2": #출금
                print(menu[1])
                put = int(input("출금하실 금액을 입력하세요."))
                if put > my_money:
                    print("잔액이 부족합니다.")
                    print()
                else:
                    my_money -= put
                    print("총 잔액 :", my_money)
                    print()
            elif menuNum == "3":  # 잔액조회
                print(menu[2])
                print("총 잔액 :", my_money)
                print()
            elif menuNum == "4":  # 계좌이체
                print(menu[3])
                print(input("이체할 계좌번호를 입력하세요."))
                send = int(input("이체할 금액을 입력하세요"))
                if send > my_money:
                    print("잔액이 부족합니다.")
                    print()
                else:
                    my_money -= send
                    print("총 잔액 :", my_money)
                    print()
            elif menuNum == "5":  # 종료
                print(menu[4])
                print("프로그램이 종료됩니다.")
                print()
                i = 5
                break

#UP,Down 게임
'''
컴퓨터로부터 1~100 사이의 임의의 숫자를 입력받고,
우리는 그 숫자를 맞춰보자.
총 기회는 10번, 기회를 모두 소진하면 종료!!
숫자를 맞췄을 경우 "축하합니다" 종료
기회가 끝났을 경우 "실패.." 종료
'''
import random

num = random.randint(1,100)
i = 0
while True:
    if i == 10:
        print("기회를 모두 소진하였습니다.")
        break
    else:
        user = int(input("1~100 사이의 정수를 입력하세요 >>"))
        if num == user:
            print("축하합니다!")
            break
        elif num != user:
            print("실패..")
            print("숫자:", num)
            i += 1