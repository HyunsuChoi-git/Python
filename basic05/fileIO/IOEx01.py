'''
*** 파일입출력 i/o ***
1. 파일생성하기
    open("파일이름", "파일열기 모드")

2. 파일열기
    r : 읽기모드 (read)
    w : 쓰기모드 (write)
        - 파일이 존재하지 않을 경우, 새로운 파일이 생성됨
        - 같은 이름의 파일이 존재할 경우, 덮어쓰기
    a : 추가모드 (append)
        - 기존 내용에 내용 추가가
3.파일닫기
    객체이름.close  :  열려있는  파일 객체 닫기.

'''
import codecs

f = codecs.open("newFile01.txt", "w")
f.write("피카츄\n")
f.write("피카츄\n")
f.write("피카츄\n")
f.write("피카츄\n")
f.close()