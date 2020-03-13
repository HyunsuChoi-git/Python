# 같은숫자
lst = [1,1,2,3,5,4,7,7,2]

def find_same_val(l):
    n = len(l)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if l[i] == l[j]:
                result.add(l[i])
    return  result

res = find_same_val(lst)
print(res)


# n명 중 두명을 뽑아 짝을 짓는다, 짝지을 수 있는 모든 조합을 출력

lst0 = ["tom", "jerry", "mike"]

def matchF(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            print(a[i], a[j])

matchF(lst0)