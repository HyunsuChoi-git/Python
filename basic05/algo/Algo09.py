#선택정렬 : 최소값 찾아 위치옮기기

def sel_sort(li):
    l_len = len(li)
    for i in range(0, l_len-1):
        max_idx = i
        for j in range(i+1 , l_len):
            if li[j] > li[max_idx]:
                max_idx = j
                print(j)
        li[i], li[max_idx] = li[max_idx], li[i]
    return li

lst = [3,9,12,6,1]
print(sel_sort(lst))