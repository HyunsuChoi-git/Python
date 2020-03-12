'''
***모듈과 패키지***





***GUI***
1. 컨테이너
2. 컴포넌트
3. 배치관리자
4. 이벤트


tkinter 모듈 사용하여 gui 만들어보기

# 배치관리자
1. pack : 상하좌우로 컴포턴트(위젯)를 배치
    1) side : 위젯을 배치하는 시작점 설정
        TOP (기본값, 위), LEFT, RIGHT, BOTTOM
    2) fill : 위젯을 화면에 꽉차게 표지
        x(가로), y(세로), both(둘다)
    3) expand : 창 크기가 변하면, 위젯의 배치도 비율대로 변환
    4) padx : 좌우 여백 지정
    5) pady : 상하 여백 지정
    6) anchor : 위젯을 방위에 따라 배치
        E, W, S, N, SW, NW, NE
2. grid : 행과 열로 구획을 지어서 컴포넌트 배치
    1) row : 행번호
    2) column : 열번호
    3) rowspan : 행 갯수
    4) columnspan : 열 갯수
3. palce : 좌표를 지정하여 컴포넌트 배치

'''


#//tkinter import
from tkinter import *

#//1. 컨테이너
window = Tk()

#//2. 컴포넌트
b1 = Button(window, text="one")
b2 = Button(window, text="two")
b3 = Button(window, text="three")
b4 = Button(window, text="병합을수행했다")

#//3. 배치관리자
#// pack
#// b1.pack(side=LEFT, fill=BOTH, padx=10, pady=5, expand=YES)
#// b2.pack(side=LEFT, fill=BOTH, padx=10, pady=5, expand=YES)

#// gird
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0, columnspan=3)

#//4. 루프돌리기 : thread  :  신호를 기다리면서 무한적으로 반복해서 화면 띄우기
window.mainloop()