#튜플의 언패킹

tup = ("피카추", 20, "Seoul")
name, age, city = tup
print(name)
print(age)
print(city)

a, b = 10, 20

a, b = b, a
print(a)
print(b)

#튜플 결합하기
t1 = (1,2,3)
t2 = ('a','b','c')
t3 = t1 + t2
print(t3)

#튜플 요소 할당하기 : *
t2 = t1 * 3
print(t2)

#in 연산자
tup = (1,2,'a','b')
print('a' in tup)


tupList = [("피카츄", 100),("꼬북이",70),("파이리",45)]
for i,j in tupList:
    print("%s님의 점수는 %d점 입니다." %(i, j))


#인덱싱, 슬라이싱
tup = ("global", [1,2,3], (4,5,6))
print(tup[1:])
print(tup[1][1:])
print(tup[2][:])