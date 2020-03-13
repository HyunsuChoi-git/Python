lst = [17,92,18,33,58,7,33,42, 92]

def search(l, num):
    f_lst = []
    length = len(l)
    for i in range(length):
        if l[i] == num:
            f_lst.append(i)

    return f_lst

print(search(lst, 92))


stu_no = [39,14,67,105]
stu_name = ["Justin", "John", "Mike", "Summer"]

# 학생번호입력하면 이름 나오는 함수
def getname(stdNumL, stuNameL, num):
    numL = len(stdNumL)
    for i in range(numL):
        if num == stdNumL[i]:
            return stuNameL[i]
    return '?'

print(getname(stu_no, stu_name, 1))