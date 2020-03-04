def sum(*num):
    tot = 0
    print(num)
    for i in num:
        tot += i
    return tot

print(sum(10,20,30,40,50))
print(sum(10,20,30))


#op:연산자 기호, *num 연산위한 숫자
def calc(op, *num):
    if op == '+':
        tot = 0
        for i in num:
            tot += i
    elif op == '-':
        tot = num[0]
        for i in num:
            tot -= i
    elif op == '*':
        tot = 1
        for i in num:
            tot *= i
    elif op == '/':
        tot = num[0]*num[0]
        for i in num:
            tot /= i
    return tot

print(calc("*", 1,2,3,4,5))
print(calc("/", 10,2))
