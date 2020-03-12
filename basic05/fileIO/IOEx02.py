'''
쓰기

1. open file
2. write
3. close file

#더 쉬운 방법
with 키워드를 이용해서 context manager만들기
하나의 open 블럭을 만들고, 블럭안의 변수는 일정기간 동안(블럭이 실행될 때)만
존재하게 함.

'''
import codecs

def writeThings(st):
    #f = codecs.open("data.txt", "w", "utf-8")
    #f = codecs.open("data.txt", "a", "utf-8")
    #f.write(st + "\n")
    #f.close()
    with open("data.txt","a") as f:
        f.write(st+"\n")


if __name__ == '__main__':
    writeThings(input("작성하세요."))
