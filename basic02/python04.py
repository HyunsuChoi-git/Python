"""
***** 문자열 str *****
    '문자열' "문자열" '''여러줄 문자열'''(홑따옴표 가능)

    문자열 indexing
    0 1 2 3 4
    h e l l o

"""
#
# print('hello'
#       ''
#       'python')
# print("""hello
#
# python""")
# memo="""안녕하세요
# 저는 피카츄입니다.
# 나이는 몰라요"""
# print(memo)
#
# first="python"
# second=" is easy"
# third=first+second
# print(third)
#
# a = "python "*10
# print(a)
#
# str1="Grobal IT"
# print(str1[0], str1[1] , str1[8])
#
# # Hello 문자열을 변수에 저장하고 olleh라고 출력해주세요.
#
# str2="Hello"
# print(str2[4]+str2[3]+str2[2]+str2[1]+str2[0])
# print(str2[-1]+str2[-2]+str2[-3]+str2[-4]+str2[-5])
#
# print(str2[4:-1:-1])
#
# print(''.join(reversed(str2)))
#
#
# # 문자열을 수정 불가능 immutable
# # 문자열 슬라이싱 (slicing)
# # 문자열을 나눌 수 있다.
# # 변수명[시작번호:끝번호] * 끝번호는 포함x, 끝번호 전까지
#
# str3 = "Grobal Institute"
# print(str3[0:3])
# print(str3[:6])
# print(str3[7:16])
# print(str3[:])
#
# str4 = "prigraming"
# # programming
# str5 = str4[0:2]+"o"+str4[3:7]+"m"+str4[7:10]
# print(str5)

# 날짜 잘라보기
import datetime
date = (str)(datetime.date.today())
print(date)
print(type(date))
year = date[0:4]
month = date[5:7]
day = date[8:10]

print(year)
print(month)
print(day)
print(year+"년"+month+"월"+day+"일")
print("%s년 %s월 %s일" %(year,month,day))