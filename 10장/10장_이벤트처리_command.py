from tkinter import *

def b_click():
    ent.insert(0, "버튼을 클릭하셨습니다.")

win = Tk()

lab = Label(win, text="이벤트 알아보기", height=2, width=30)
lab.grid(row=0, columnspan=2)

ent = Entry(win)
ent.grid(row=1, column=0)

but = Button(win, text="클릭", width=6, height=2,
    command=b_click)
but.grid(row=1, column=1)

win.mainloop()