# 문제1. Book 클래스를 활용하여 2개짜리 Book 객체 리스트 만들고, 
# 사용자로부터 책의 제목과 저자를 입력받아 리스트를 완성하고 출력해보세요.

# class Book:
#     book = []
#
#     def __init__(self, subject, writer):
#         self.book = [subject, writer]
#     def showInfo(self):
#         print("제목 : %s" % self.book[0])
#         print("저자 : %s" % self.book[1])
#
# subject = input("책 제목을 입력하세요.")
# writer = input("저자를 입력하세요.")
# book = Book(subject,writer)
# book.showInfo()



# 문제2. 직사각형을 표현하는 Rectangle 클래스를 작성하세요.
# 	- int 타입의 x, y, width, heigth 필드 : 사각형을 구성하는 점과 크기 정보
# 	- x, y, width, height 값을 매개변수로 받아 필드를 초기화하는 생성자
# 	- int squareArea() : 사각형 넓이 리턴
# 	- void show() : 사각형의 좌표와 넓이 출력
# 	- contains(r) : 매개변수로 받은 r이 현 사각형 안에 있으면 true 리턴
#   - 실행 코드(변경불가)
#       a = Rectangle(2, 2, 8, 7)
# 		b = Rectangle(5, 5, 6, 6)
# 		c = Rectangle(1, 1, 10, 10)
# 		a.show()
# 		print("b의 면적은 ", b.square())
# 		if c.contains(a) :
# 	    	print("c는 a를 포함합니다.")
# 		if c.contains(b):
# 	    	print("c는 b를 포함합니다.")
# 	- 콘솔출력결과:
# 		(2,2)에서 크기가 8x7인 사각형
# 		b의 면적은 36
# 		c는 a을 포함합니다.
class Rectangle:
    x, y, width, height = 0,0,0,0

    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def square(self):
        area = self.width * self.height
        return area
    def show(self):
        print("(%d,%d)에서 크기가 %dx%d인 사각형" %(self.x,self.y,self.width,self.height))
    def contains(self,r):
        if self.x <= r.x and self.y <= r.y and self.width >= r.width and self.height >= r.height:
            return True
        else: return False

# a = Rectangle(2, 2, 8, 7)
# b = Rectangle(5, 5, 6, 6)
# c = Rectangle(1, 1, 10, 10)
# a.show()
# print("b의 면적은 ", b.square())
# if c.contains(a) :
#     print("c는 a를 포함합니다.")
# if c.contains(b):
#     print("c는 b를 포함합니다.")


# 문제3. n명이 참가하는 끝말잇기 게임을 만들어보자.
#   처음단어는 "자동차"이다. n명의 참가자들은 순서대로 자신의 단어를 입력하면된다.
#   끝말잇기에서 틀리면 게임오버 -> 진사람이름 출력, 끝.
#   WordGameApp 클래스와 각 선수를 나타내는 Player 클래스 작성.
#   WordGameApp : main(),게임을 전체적으로 진행하는 run(), run()에서 플레이어수 만큼 Player객체 배열 생성
#   Player : 플레이어 이름, 단어입력받는 getWordFromUser()메서드, 끝말잇기 성공여부와 게임계속할지 판별하는 checkSuccess() 메소드


# 문제4. 영한 사전 만들기 : dict를 이용하여 10개의 단어를
# 영어,한글의 쌍으로 저장하고 영어로 한글을 검색하는 프로그램을 만들어보세요.
# 단, exit가 입력되면 프로그램 종료!

# voca = {"apple":"사과", "orange":"오렌지", "mango":"망고", "melon":"메론","strawberry":"딸기","banana":"바나나",
#         "cherry":"체리","grape":"포도","grapefruit":"자몽","pineapple":"파인애플"}
#
# while True:
#     word = input("영어 입력 >>")
#     if word in voca:
#         print("%s : %s" % (word, voca[word]))
#     else:
#         if word == "exit":
#             print("종료합니다")
#             break
#         else:
#             print("없는 단어입니다.")



class Day:
    work = None
    def setWork(self, work):
        self.work = work
    def getWork(self):
        return self.work
    def show(self):
        if self.work == None:
            print("없습니다.")
        else:
            print(self.work,"입니다.")
# 문제5. 하루할일을 표현하는 클래스 Day는 다음과 같다.
# 	한달의 할일을 표현하는 MonthSchedule 클래스를 작성하세요.
# 	MonthSchedule 클래스에는 Day 객체를 담는 리스트와 적절한 변수,메서드를 작성하고
# 	실행 예시처럼 입력, 보기, 끝내기 등의 3개의 기능을 작성하라.
# 	 -> 생성자, input(), view(), finish(), run() 메소드 만들기.
# 	#실행예시#
# 	이번달 스케쥴 관리 프로그램.
# 	할일(입력:1, 보기:2, 끝내기:3) >> 1
# 	날짜(1~30)? 1
# 	할일? 자바공부
#
# 	할일(입력:1, 보기:2, 끝내기:3) >> 2
# 	날짜(1~30)? 1
# 	1일의 할 일은 자바공부입니다.
#
# 	할일(입력:1, 보기:2, 끝내기:3) >> 3
# 	프로그램 종료.

# 실행코드
# march = MonthSchedule(31); // 3월달의 할 일
# march.run();

# 문제6. 나라와 수도 맞추기 게임을 만들어 보세요.
# 	1) 나라이름(country)과 수도(capital)로 구성된 Nation클래스를 작성하고,
# 		Nation객체가 저장되는 리스트를 이용하여
# 		아래 실행 예시와 같이 작동되도록 프로그램을 작성하세요.
# 	실행예시:
# 		** 수도 맞추기 게임을 시작합니다 **
# 		입력:1, 퀴즈:2, 종료:3 >> 1 (사용자가 입력)
# 		현재 8개의 나라와 수도가 입력되어 있습니다.
# 		나라와 수도 입력9>> 한국 서울
# 		나라와 수도 입력10>> 그리스 아테네
# 		그리스는 이미 있습니다!!
# 		나라와 수도 입력10>> 호주 시드니
# 		나라와 수도 입력11>> 이탈리아 로마
# 		나라와 수도 입력10>> 그만
# 		입력:1, 퀴즈:2, 종료:3 >> 2
# 		호수의 수도는? 시드니
# 		정답!!
# 		독일의 수도는? 하얼빈
# 		아닙니다!!
# 		멕시코의 수도는? 하얼빈
# 		아닙니다!!
# 		이탈리아의 수도는? 로마
# 		정답!!
# 		한국의 수도는? 서울
# 		정답!!
# 		영국의 수도는? 그만
# 		입력:1, 퀴즈:2, 종료:3 >> 3
# 		게임을 종료합니다.

# 문제7. 이름과 학점(4.5만점)을 5개 입력받아 dict에 저장하고,
#       장학생 선발 기준을 입력받아 장학생 명단을 출력하세요.
# 	실해예시:
# 		자바장학금관리시스템입니다.
# 		이름과 학점 >> 호크아이 3.1
# 		이름과 학점 >> 블랙위도우 3.6
# 		이름과 학점 >> 토르 2.9
# 		이름과 학점 >> 데드풀 3.7
# 		이름과 학점 >> 아이언맨 4.3
# 		장학생 선발 학점 기준 입력 >> 3.2
# 		장학생 명단 : 블랙위도우 데드풀 아이언맨