# sum() : 요소값 모두 더하기
t1 = 1,2,3,4,5
print(sum(t1))

# len()  :  길이

print(len(t1))


# max(), min() : 최대 최소

print(max(t1))
print(min(t1))

#index() : 요소의 인덱스 번호 구하기

print(t1.index(3))

#count() : 요소의 갯수 구하기
t1 = 1,1,1,2,2
print(t1.count(1))


#1.
def my_sum(*args):
    tot = 0
    for i in args:
        tot += i
    return tot

print(my_sum(1,2,3,4,5,6,7,8,9,10))

#2.
def my_max(*args):
    tot = 1
    for i in args:
        tot *= i
    return tot

print(my_max(10,5,2))

#3.
def my_min(*args):
    tot = args[0]*2
    for i in args:
        tot -= i
    return tot

print(my_min(10,5,4))

#4.
def my_index(args, num):
    index = 0
    for i in range(len(args)):
        if args[i] == num:
            index = i
    return index
tup=1,2,3,4,5
print("index: ",my_index(tup, 1))

#5.
def my_count(*args):
    count = 0
    for i in args:
        count +=1
    return count

print(my_count(1,2,3,4,5))


#6.

str = "Apple Tree"
# str = str.replace("Apple", "Lemon")
print(str)

def my_replace(str,ori,new):
    fistIdx = str.find(ori)
    lastIdx = str.find(ori)+len(ori)
    newStr = str[0:fistIdx]+new+str[lastIdx:]

    return newStr
str = "abcdefghijk"
print("repl : ",my_replace(str,"cdef", "cccc"))








# def my_replace(args,num1,num2):
#     idx1 = 0
#     idx2 = 0
#     for i in range(len(args)):
#         if args[i] == num1:
#             idx1 = i
#         elif args[i] == num2:
#             idx2 = i
#
#     args[idx1], args[idx2] = num2, num1
#
#     return args
#
# tup=[1,2,3,4,5]
# my_replace(tup,1,3)
# print(tup)


