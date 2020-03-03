#0 ~ 10 까지 출력
for i in range(10): #매개변수 이전 숫자까지 인식한다.
    print(i)

print()

#1 ~ 11 까지 출력
for i in range(1, 11):
    print(i)

print()

#건너뛰면서 출력 : range(start, end-1, step)
# start와 step은 생략가능하나 end-1 은 반드시 있어야한다.

for i in range(1, 11, 2):
    print(i)



