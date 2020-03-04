
#기본함수
def showInfo():
    print("함수야!!")

showInfo()

#리턴값이 있는 함수
def getNum():
    print("리턴있음")
    return 10

print(getNum())

#매개변수가 있는 함수
def showName(name):
    print("당신의 이름은 %s입니다." % name)

showName("피카츄")

#연산
def my_sum(num1,num2):
    result = num1 + num2
    return result
result = my_sum(10,20)
print(result)

def my_min(num1,num2):
    result = num1 - num2
    return result
result = my_min(10,20)
print(result)

def my_mul(num1,num2):
    result = num1 * num2
    return result
result = my_mul(10,20)
print(result)

def my_div(num1,num2):
    result = num1 / num2
    return result
result = my_div(10,20)
print(result)