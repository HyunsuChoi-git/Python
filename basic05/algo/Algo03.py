#factorial

def facto(n):
    if n <= 1:
        return 1
    return n * facto(n-1)

# 1 ~ n 까지의 합 재귀
def sum_facto(n):
    if n <= 1:
        return 1
    return n + sum_facto(n-1)

def fmax(l):
    n = len(l)
    max = l[0]
    for i in range(1, n-1):
        if l[i] >= max:
            max = l[i]
    return max

lst0 = [32,55,37,89,3,22,5,23,9]
def max_facto(lst, n):
    #인덱스 내꺼랑 내 뒤에꺼 비교해서 큰애 돌려주기. 무한반복
    if n == 1:
        return lst[0]
    max = max_facto(lst, n-1)
    if max > lst[n-1]:
        return max
    else:
        return lst[n-1]
  


res = max_facto(lst0, len(lst0))
print(res)

