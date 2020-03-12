'''

파일읽기

r : 읽기모드 : open()에서 파일모드를 지정하지 않으면 default 값 > r 로 처리됨

'''


f = open("data.txt")


#1. read(byte) : 바이트수 만큼 읽기

r1 = f.read(2)
print(r1)

#2. read() : 전체 읽기
r2 = f.read()
print(r2)

#3. seek(byte)
f.seek(5)  #0 == 처음
r3 = f.read(5)
print(r3)

#4. readLines()
f.seek(0)
lines = f.readlines()
print(len(lines))
print(lines)

for line in lines:
    print(line[::-1])

f.close()