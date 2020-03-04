num = 5
def func1():
    global num  # 전역변수 가리키는 것을 선언 한 것이다.
    num = num + 1
    print(num)

func1()

print("전역변수 : ", num)  # 6


# def ques1():
#     num1 = int(input("정수1 입력 : "))
#     num2 = int(input("정수2 입력 : "))
#
#     print("덧셈 : ", num1+num2)
#     print("뺄셈 : ", num1-num2)
#     print("곱셈 : ", num1*num2)
#     print("나눗셈 : ", num1/num2)
#     ans = input("﻿종료하시겠습니다?(y/n)")
#
#     if ans.lower == "y":
#         print("프로그램 종료!")
#         return
#     elif ans.lower == "n":
#         ques1()
#
# ques1()


def ques2(id,pw):
    db_id = "python"
    db_pw = "1234"
    if db_id == id and db_pw == pw :
        print("%s 님 환영합니다!" % id)
    else:
        if db_id != id :
            print("%s 는 존재하지 않는 id입니다." % id)
        elif db_pw != pw :
            print("비밀번호가 일치하지 않습니다.")

print("***로그인***")
id = input("id를 입력하세요 : ")
pw = input("pw를 입력하세요 : ")
ques2(id, pw)
