#리스트 관련 함수들

#요소 추가하기 : append()
lst = []
lst.append(1)
lst.append(2)
print(lst) # [1, 2]
lst.append("a")
print(lst) # [1, 2, 'a']


#리스트 확장 : extend()
lst1 = [1,2,3]
lst2 = [4,5,6]
lst1.extend(lst2)
print(lst1) # [1, 2, 3, 4, 5, 6]

lst1 = [1,2,3]
lst2 = [4,5,6]
lst1.append(lst2)
print(lst1) # [1, 2, 3, [4, 5, 6]]


# 요소 삽입하기 : insert(index, 데이터)
# 원하는 index 번호와 삽입할 데이터를 넣으면 된다.
lst = [1,2,3]
lst.insert(1, 10)
print(lst) # [1, 10, 2, 3]


# 요소 제거하기 : remove(데이터)
lst.remove(10)
print(lst) # [1, 2, 3]


###############################
l1 = [1,2,3,4,5]

# idx1 = int(input("인덱스번호 입력 1 >>"))
# idx2 = int(input("인덱스번호 입력 2 >>"))
# emt = l1[idx1]

# l1[idx1] = l1[idx2]
# l1[idx2] = emt
# print(l1)

l2 = [1,3,5,4,2]
l2.insert(4,l2[1])
l2.append(1)
l2.remove(1)
l2.remove(3)
print(l2)


l3 = ["Global",["IT",[1,3,5,7,9],["Even", [0,2,4,6,8]]]]
print(l3[0])
print(l3[1][1][1])
print(l3[1][2][1][4])

l4 = ["﻿==================","파이썬",["자료형","제어문","입출력","클래스"],"*"]
print(l4[0])
print("\t ", l4[1])
print(l4[0])
print(l4[2][0], l4[3])
print(l4[2][1], l4[3]*3)
print(l4[2][2], l4[3]*4)
print(l4[2][3], l4[3]*6)