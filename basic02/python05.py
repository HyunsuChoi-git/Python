# 문자열 관련함수
# 문자열 바꾸기 : replace('수정원하는 문자열' , '바뀔 문자열')
str = "apple tree"
print(str)
str = str.replace("apple","lemon")
print(str)

# 문자열 나누기 : split()
a,b,c,d,e = "1 2 3 4 5".split() # 구분자 지정을 안하면 공백을 기준으로 분할
print(a)
str1 = "Grobal:Institute"
str1,str2 = str1.split(":")
print(str1)
print(str2)

# 문자 길이 : len()
str = "akhtbjkwhtkjwehtjkhawenlkdsagfnkl"
print(len(str))

# 문자 개수 구하기 : count('문자')
print(str.count("a"))

name = "Global IT"
print("="*15)
# 문자의 위치 알려주는 방법 1
print(name.find('o'))  # 인덱스번호 리턴
print(name.find('z'))  # 찾는 값이 없으면 -1 return
print("="*15)
# 문자의 위치 알려주는 방법 2
print(name.index('o')) # 인덱스번호 리턴
# print(name.index('z')) # 찾는 값이 없으면 에러 발생!

str = "Apple Tree"
# 소문자를 대문자로 바꿔주는 : upper()
str = str.upper()
print(str)
# 대문자를 소문자로 바꿔주는 : lower()
str = str.lower()
print(str)

# 공백 지우기 : strip(), lstrip, rstrip()
t = "        python          "
print(t.strip())
print(t.lstrip())
print(t.rstrip())