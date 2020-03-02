'''
***Random(난수)***
seed 값이라는 것이 존재한다. seed값 : 임의로 선택하는 것처럼 만들어주는 숫자

'''

import random
num = random.randint(1, 5)

print(num)
#0 ~ 1 사이의 실수 형태인 난수를 리턴
print(random.random())

lst = [10,20,30,40,50]
num2 = random.choice(lst)
print(num2)

#원하는 만큼의 리스트 원소들을 무작위로 추출
num3 = random.sample(lst, 3)
print(num3)

#리스트를 무작위로 섞어준다 shuffle() : 대입할 필요없음
print(lst)
random.shuffle(lst)
print(lst)



#문제 1. 동전던지기. 앞면 0, 뒷면 1 인지 출력

coin = random.randint(0,1)
if coin == 0:
    print("앞면")
else:
    print("뒷면")


#문제 2. 가위(0), 바위(1), 보(2) 게임
'''
컴퓨터와 가위바위보 대결하기
컴퓨터는 임의의 값을 가지고,
플레이어는 입력을 하여 서로 비교한 후,
플레이어가 이겼는지 비겼는지 졌는지 출력하세요.

'''

com = random.randint(0,2)
ply = int(input("가위(0), 바위(1), 보(2)"))

if com == ply:
    print("비겼다!")
elif com == 0:
    if ply == 1:
        print("이겼다!")
    elif ply == 2:
        print("졌다!")
elif com == 1:
    if ply == 0:
        print("졌다!")
    elif ply == 2:
        print("이겼다!")
elif com == 2:
    if ply == 0:
        print("이겼다!")
    elif ply == 1:
        print("졌다!")

