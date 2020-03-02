# #문제 1. 정수 1개를 입력받아, 그 수가 '양수'인지 '음수'인지 출력해보세요.
#
# num = int(input("정수입력 >>"))
# if num > 0:
#     print("양수")
# elif num < 0:
#     print("음수")
# else:
#     print(0)
#
#
#
# #문제 2. 정수 1개를 입력받아, 그 수가 "짝수"인지 "홀수"인지 출력해보세요.
#
#
# num2 = int(input("정수입력 >>"))
# result = num2%2
# print(result)
# if result == 0:
#     print("짝")
# elif result == 1:
#     print("홀")
#
#
#
# #문제 3. id와 pw 입력받아 모두 일치하면 "(id)님이 로그인되었습니다."출력
# #       불일치하면 "아이디와 비밀번호를 확인해주세요" 출력
#
# db_id= "python"
# db_pw= "1234"
#
# id = input("id >>")
# pw = input("pw >>")
#
# if id == db_id and pw == db_pw:
#     print("(%s)님이 로그인되었습니다." %id)
# else:
#     print("아이디와 비밀번호를 확인해주세요")

#문제 4. 주민번호를 입력받아, "여성 / "남성" 을 출력해보세요.

# per = input("주민번호입력>>")
# print(per[6])
# if per[6] == 2:
#     print("여")
# else:
#     print("남")

#문제 5. 사용자로부터 키를 입력받아, 키가 150 이상이면 "놀이기구 이용가능해요"출력
#       140 미만이면, 질문:부모님 모시고 오셨니? 물어보고 답변(yes:1, no:0)받아
#       1 --> "이용가능해~ 재밌게 놀아~"
#       2 --> "부모님 모시고 다시오렴" 출력

# hight = int(input("키 >>"))
# if hight >= 150:
#     print("놀이기구 이용가능해요")
# elif hight < 150:
#     an = int(input("부모님 모시고 오셨니? (yes:1, no:0)"))
#     if an == 1:
#         print("이용가능해~ 재밌게 놀아~")
#     elif an == 0:
#         print("부모님 모시고 다시오렴")


#출력 6. 학점 처리 프로그램

'''
이름과 국어, 영어, 수학 3과목에 대한 점수를 입력받아
총점, 평균, 학점을 구해보세요.
단, 평균은 소수점 이하 한자리까지 표현
학점기분 : 90점 이상 A
          80점 이상 B
          70점 이상 C
          60점 이상 D
          그 이하 F
'''


name = input("이름입력 >>")
kor = int(input("국어>>"))
eng = int(input("영어>>"))
math = int(input("수학>>"))

tot = kor+eng+math
avg = tot/3
sco = ""

if avg >= 90:
    sco = "A"
elif avg >= 80:
    sco = "B"
elif avg >= 70:
    sco = "C"
elif avg >= 60:
    sco = "D"
else:
    sco = "F"

print("%s 님의 총점은 %d 이고, 평균은 %.1f, 학점은 %s 입니다." %(name, tot, avg, sco))