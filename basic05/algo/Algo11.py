# 병합정렬 : 두그룹으로 나눠서 정렬시키고, 다시 서로 비교하여 앞에있는 아이끼리 비교 작은아이만 정렬시키고 한줄끝나면 나머지는 쭈욱 붙힌다.
#easy
def merge_sort(l):
    length = len(l)
    if length <= 1: # 리스트 개수가 1개이하면 정렬할 필요없이 그냥 돌려주기.(재귀함수 종료조건!!)
        return l

    # 그룹 인덱스 양분
    mid = length // 2
    g1 = merge_sort(l[:mid])    # 재귀로 정렬
    g2 = merge_sort(l[mid:])    # 재귀로 정렬

    result = []
    #두 그룹에 모두 자료가 남아있는 동안반복, 하나라도 끝나면 조건성립안됨. 둘중 하나라도 자료가 없으면 while중지
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    # 한쪽이라도 자료가 남으면 아래 조건 성립하여 순서대로 끝에 이어붙히기.
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

lst = [6,8,3,9,10,1,2,4,7,5]
# print(merge_sort(lst))

#ordinary
def m_sort(l):
    length = len(l)
    if length <= 1: #재귀함수 종료조건: 리스트 자료 개수가 한개이하면 정렬 불필요
        return
    #그룹 두개로 나누고
    mid = length // 2
    #나눠서 복사해놓기 : 함수들이 매달려있기때문에 나눌수 있을때까지 나눠서 이 변수를 통해 자료 저장됨.
    g1 = l[:mid]
    print("g1", g1)
    g2 = l[mid:]
    print("g2", g2)
    #재귀호출로 정렬
    merge_sort(g1)
    merge_sort(g2)
    # 정렬하기
    idx1 = 0
    idx2 = 0
    idxL = 0

    # 두그룹의 요소가 있고 그 수 만큼 반복하기
    while idx1 < len(g1) and idx2 < len(g2):
        if g1[idx1] < g2[idx2]:
            l[idxL] = g1[idx1]
            idx1 += 1
            idxL += 1
            print("if: lst", l)
        else:
            l[idxL] = g2[idx2]
            idx2 += 1
            idxL += 1
            print("else: lst", l)

    # 둘중하나 그룹에 요소가 끝났을경우 나머지 자료들 결과에 추가하기
    while idx1 < len(g1):
        l[idxL] = g1[idx1]
        idx1 += 1
        idxL += 1
    while idx2 < len(g2):
        l[idxL] = g2[idx2]
        idx2 += 1
        idxL += 1



