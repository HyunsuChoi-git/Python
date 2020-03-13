def f_max(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max

lst0 = [39, 48, 4,69,3,1]
res = f_max(lst0)
print(res)

def f_M_idx(lst):
    n = len(lst)
    m_idx = 0
    for i in range(1, n):
        if lst[i] > lst[m_idx]:
            m_idx = i
    return m_idx