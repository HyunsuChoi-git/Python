# 예외처리
'''
IOError : 파일을 오픈할 수 없을 때 발생
IndexError
ImportError
ValueError
ZerodivisionError
FileNotFoundError
SynteaxError  :  문법에러
EOFError  :  End of File  더이상 읽어올 내용이 없을 때 발생


구조 :
    try :
        코드들...
    except [에러 [as 변수명]] :
        예외 발생 시 처리할 코드..
'''

# print("프로그램 시작!!")
#
# while True:
#     try:
#         num = input("정수 : ")
#         int(num)
#         print(num)
#         break
#     except ValueError:
#         print("ValueError 발생!")
#
# print("프로그램 종료!!")


# lst = [1,2,3]
#
# try:
#     idx = int(input("인텍스 번호 입력 : "))
#     print(3/idx)        #ZerodivisionError
#     print(lst[idx])     #IndexError
# except Exception:
#     print("모든예외처리!")
# finally:
#     print("예외 발생 여부와 관계없이 무조건 실행되는 finally")

# def func():
#     num = int(input("1~5 사이의 정수를 입력 : "))
#
#     if num > 5 or num < 1:
#         raise  # 강제 예외 발생 키워드 ( 함수를 호출한 곳에서 예외처리를 한다 )
#     else:
#         print(num)
# #///////////////////////////////////
#
# try:
#     func()
# except:
#     print("1~5사이의 정수가 아닙니다.")

try:
    age = int(input("나이 입력: "))
    if age < 0 :
        raise ValueError("음수를 입력받음")
except ValueError as e:
    print(e)
else:
    print(f"당신의 나이는 {age}살 입니다")