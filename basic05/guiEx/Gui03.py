from tkinter import *

win = Tk()

beach = PhotoImage(file="beach.gif")

lab1 = Label(win, image=beach).pack(side="right")

memo = """
    이미지는 gif와 ppm/ppm/pgm 포맷만 사용할 수 있다.
    특정 모듈을 import하면, 다른 포맷의 이미지도 사용 가능하다.
"""
lab2 = Label(win, text=memo, padx=10).pack(side="left")

win.mainloop()