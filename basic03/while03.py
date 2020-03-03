# ATM 기계
menu = ""
'''
 ***** 글로벌 은행 ATM *****
 1. 입금
 2. 출금
 3. 잔액 조회
 4. 계좌 이체
 5. 종료
'''
my_money = 100000
db_id = "java"
db_pw = "1234"
# 1단계 : 메뉴 번호 선택하면, 메뉴 이름 출력
# 2단계 : 메뉴별 기능 구현하기
while True:
    count = 0
    if count == 3:
        print("비밀번호를 3번 틀려 프로그램을 종료합니다.")
        break
    id = input("id를 입력해주세요.")
    pw = input("pw를 입력해주세요.")
    if db_id == id or db_pw == pw:
        while True:
            menu_list = ["1. 입금", "2. 출금", "3. 잔액조회", "4. 계좌 이체", "5. 종료"]
            print(" ***** 글로벌 은행 ATM *****")
            print(menu_list[0])
            print(menu_list[1])
            print(menu_list[2])
            print(menu_list[3])
            print(menu_list[4])
            print("이용할 서비스 번호를 입력해주세요.")
            num = int(input())
            if num == 5:
                print("서비스를 종료합니다.")
                break
            if num == 1:
                print("입금서비스를 선택하였습니다.")
                print("입금하실 금액을 입력주세요.")
                money = int(input())
                my_money += money
                print("%d원을 입금하여 총 금액은 %d원입니다." %(money,my_money))
                print("입금서비스가 완료되었습니다.")
            elif num == 2:
                print("출금서비스를 선택하였습니다.")
                print("출금하실 금액을 입력해주세요.")
                money = int(input())
                my_money -= money
                print("%d원을 출금하여 총 잔액은 %d원입니다." % (money, my_money))
                print("출금서비스가 완료되었습니다.")
            elif num == 3:
                print("잔액조회 서비스입니다.")
                print("고객님꼐서 가지고 계신 금액은 %d원입니다." %(my_money))
            elif num == 4:
                print("계좌이체 서비스를 선택하였습니다.")
                print("보내실 계좌번호를 입력해주세요.")
                number = int(input())
                print("보내실 금액을 입력해주세요.")
                money = int(input())
                my_money -= money
                print("%d로 계좌이체를 하였습니다." %number)
                print("%d원을 이체하여 총 잔액은 %d원입니다." % (money, my_money))
                print("이체서비스가 완료되었습니다.")
    elif not(db_id == id or db_pw == pw):
        count += 1


# 3단계 : 아이디와 패스워드 입력받아서 로그인하면 서비스 이용 가능하게 만들기
# 4단계 : 아이디와 패스워드 3회 오류시 프로그램 강제 종료

# Up, Down 게임
'''
컴퓨터로부터 1~100사이의 임의의 숫자를 입력받고,
우리는 그 숫자를 맞춰보자.
총 기회는 10번, 기회를 모두 소진하면 종료.
숫자를 맞췄을 경우 "축하합니다" 종료
기회가 끝날을 경우 "실패...." 종료
'''