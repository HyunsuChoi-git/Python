#빈 튜플
t1 = ()
print(t1)
print(type(t1))

#한개의 요소만 대입할 경우
t2 = (10,)
print(t2)
print(type(t2))

#요소가 두개 이상일 경우
t3 = (1,2,3)
print(t3)
print(type(t3))
t4 = 1,2,3
print(t4)
print(type(t4))

t4 = (1,2,"a",True)
print(t4)
print(t4[0])

t5 = (1,2,(3,4,5),[6,7])
print(t5)
print(type(t5))

t5[3][0] = "리스트수정!"
print(t5)

