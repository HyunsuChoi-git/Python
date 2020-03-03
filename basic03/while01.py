'''
반복문 : while, for

*** while ***
구조
    #1. 반복횟수를 알 때 지정
    while 조건식:
        실행문...
        증감식

    #2. 무한반복
    while True:
        실행문...
        // 종료시점
        if 조건문:
            break

'''

# 10회 반복하기
'''
i = 0
while i <10:
    print("hello")
    i+=1
'''
# 문제1. 0 ~ 3까지 출력
'''
i = 0
while i < 4:
    print(i)
    i+=1
'''
# 문제2. 1 ~ 10사이 홀수 출력
'''
i = 1
while i < 10:
    print(i)
    i+=2
'''
# 문제3. 0 ~ 100사이의 수중 10단위로 출력 (0,10,20,30...)
'''
i = 0
while i < 100:
    print(i)
    i+=10
'''
# 문제4. 1 ~ 10까지의 모든 수를 더한 합을 출력
'''
i = 0
num = 0
while i < 10:
    i += 1
    num += i
print(num)
'''
# 문제5. 1 ~ 20사이의 짝수만 모두 더한 값 출력
'''
i = 0
num = 0
while i < 20:
    i +=2
    num += i
    print(num)
'''
# 문제6. 숫자를 5번 입력받고, 입력받은 수를 모두 더한 값을 출력
'''
i = 0
num = 0
num2 = 0
while i < 5:
    num = int(input("숫자를 입력해주세요. "))
    num2 += num
    i += 1
    print(num2)
'''

# 무한적으로 숫자를 입력받아 출력하는 while문을 만들어보자.
# 단, 숫자 9를 입력하면 while문 종료
'''
while True:
    num = int(input("숫자를 입력해주세요"))
    print("num는 %d" %num)
    if num == 9:

        print("while문 종료")
        break
'''

import time
while True:
    print("시작은 원하시면 enter를 눌러주세요.")
    input()
    print("게임 시작!!")
    time.sleep(3)
    print("게임종료!!")
    break

