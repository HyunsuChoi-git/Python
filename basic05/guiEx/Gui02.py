from tkinter import *

window = Tk()

def test():
    print("확인 버튼을 눌렀습니다.")

b1 = Button(window, text="확인", fg="blue", command=test)
                                          #//생성한 함수명 적어주면 됨
b2 = Button(window, text="종료", fg="blue", command=window.quit)
                                          #//기존의 함수를 쓸 수 있음

b1.pack()
b2.pack()

window.mainloop()
