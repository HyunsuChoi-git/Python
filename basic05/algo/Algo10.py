# 리스트에서 요소가 들어가야할 자리 알려주는 함수
def find_idx(l, val):
    for i in range(0, len(l)):
        if val < l[i]:
            return i    # i자리 값보다 작으면 i번 돌려주기.
    return len(l)   # 못차으면 마지막 자리

# 리스트에서 자리 정렬시키는 함수
def insert_sort(l):
    res = []
    while l:
        value = l.pop(0)
        indx = find_idx(res, value) # 새로 정렬된 리스트에서 순서찾아 idx값 알아내기
        res.insert(indx, value)

    return res

lst = [3,7,1,8,6]
# print(insert_sort(lst))


def ins_sort(l):
    length = len(l)
    for i in range(1, length):
        key = l[i]  #1번부터 시작해서 key에 값 복사
        j = i - 1   #i 왼쪽부터 (0부터) 검사
        while j >= 0 and l[j] > key:    # i 전에 인덱스가 0이상이고, 키값보다 크면
            l[j+1] = l[j]               # 오른쪽으로 자리 땡기고 확인하면서 반복하고
            j -= 1                      # j를 가감하여 알맞은 위치 찾기
        l[j+1] = key                    # 마지막에 j가감한거 다시 올려서 찾은 위치에 복사한 키값 대입.
    return l

# print(ins_sort(lst))

#내림 차순
def ins_sort2(l):
    length = len(l)
    for i in range(1, length):
        key = l[i]
        j = i - 1
        while j >= 0  and l[j] < key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l
print(ins_sort2(lst))
