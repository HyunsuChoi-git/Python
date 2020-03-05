#국어, 수학, 영어 점수를 입력받아
# 총점과 평균을 출력하세요. % 포맷팅 사용하기


# kor = int(input("국어 점수를 입력하세요"))
# math = int(input("수학 점수를 입력하세요"))
# eng = int(input("영어 점수를 입력하세요"))

# print("총점은 %s, 평균은 %s 입니다." % ((kor+math+eng), ((kor+math+eng)/3)))

print("hello python")
print('hello python')
print('''hello 
python''')

memo = """안녕하세요
저는 피카츄입니다
나이는 100살입니다"""
print(memo)


first = "python"
second = " is easy"
third = first+second
print(third)

word1 = "Global IT"
print(word1[0], word1[4], word1[7])


# hello 문자열을 변수에 저장하고 olleh라고 출력해보세요.

hello = "hello"
print(hello[4]+hello[3]+hello[2]+hello[1]+hello[0])
print(hello[-1]+hello[-2]+hello[-3]+hello[-4]+hello[-5])
print(hello[::-1])

print(hello[4::-1])

print(''.join(reversed(hello)))
