for i in "hello" :
    print(i)

lst = [1,2,3,4,5]
for i in lst:
    print(i)


score = [40,78,34,97,68]
#시험 점수가 60점 이상이면 합격, 그렇지 않으면 불합격 출력
#for문으로 만들어보세요.
num = 1
for i in score:
    if i >= 60:
        print("%d번 학생의 점수는 %d점으로 합격입니다." %(num, i))
    elif i < 60:
        print("%d번 학생의 점수는 %d점으로 불합격입니다." %(num, i))
    num += 1

