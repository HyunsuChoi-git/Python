
#1
for i in range(1,6):
    print("%d행 : %s" % (i,"*"*3))

#2
for i in range(1,6):
    print("*"*i)

#3
for i in range(5,0,-1):
    print("*"*i)
#4
for i in range(1,6):
    for j in range(0,5):
        print(i+j, end="")
    print()

#5
for i in range(5,0,-1):
    for j in range(0,5):
        print(i+j, end="")
    print()

#6
for i in range(1,6):
    print("*"*i)
for i in range(4,0,-1):
    print("*"*i)

#7
for i in range(5):
    for j in range(1,5-i):
        print(" ", end="")
    for k in range(0,i+1):
        print("*", end="")
    print()
print()

#8
for i in range(5,0,-1):
    for k in range(0, 5-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
print()

#9
for i in range(5):
    for j in range(1,5-i):
        print(" ", end="")
    for k in range(0,i+1):
        print("*", end="")
    print()
for i in range(5,0,-1):
    for k in range(0, 6-i):
        print(" ", end="")
    for j in range(i-1):
        print("*", end="")
    print()

#10
for i in range(5):
    for j in range(i,4):
        print(" ", end="")
    for k in range(1,(i+1)*2):
        print("*", end="")
    print()
print()
#11
for i in range(0,5):
    for k in range(i):
        print(" ", end="")
    for j in range(9-(i*2)):
        print("*", end="")
    print()

print()
#12
for i in range(5,0,-1):
    print("*"*i)
for i in range(2,6):
    print("*"*i)

print()
#13
for i in range(1,6):
    for j in range(i-1):
        print(" ", end="")
    for k in range(5,i-1,-1):
        print("*", end="")
    print()
for i in range(4):
    for j in range(3-i):
        print(" ", end="")
    for k in range(2+i):
        print("*", end="")
    print()

print()
#14
for i in range(5):
    for j in range(4-i):
        print(" ", end="")
    for k in range((i*2)+1):
        print("*", end="")
    print()
for i in range(4):
    for j in range(i+1):
        print(" ", end="")
    for k in range(7-(i*2)):
        print("*", end="")
    print()

print()
#15
for i in range(4):
    for j in range(4-i):
        print("*", end="")
    for k in range((i*2)+1):
        print(" ", end="")
    for j in range(4 - i):
        print("*", end="")
    print()
print()
for i in range(4):
    for j in range(i+1):
        print("*", end="")
    for k in range(7-(i*2)):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()

print()
#16
for i in range(4):
    for j in range(i+1):
        print("*", end="")
    for k in range(7-(i*2)):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()
print("*********")
for i in range(4):
    for j in range(4-i):
        print("*", end="")
    for k in range(0,1+(i*2)):
        print(" ", end="")
    for j in range(4 - i):
        print("*", end="")
    print()

print()
#17
for i in range(5):
    for j in range(i):
        print(" ", end="")
    for k in range(9-(i*2)):
        print("*", end="")
    print()
for i in range(4):
    for j in range(3-i):
        print(" ", end="")
    for k in range(3+(i*2)):
        print("*", end="")
    print()

print()
#18
print("\t\t\t\t\t\t구구단")
print()
print()
for i in range(1,10):
    for j in range(2,6):
        print("%d X %d = %d\t\t" %(j,i,j*i), end="")
    print()
print()
for i in range(1,10):
    for j in range(6,10):
        print("%d X %d = %d\t\t" %(j,i,j*i), end="")
    print()