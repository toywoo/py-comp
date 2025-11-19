from tkinter import *

win = Tk()

lab = Label(win, text="pack 알아보기")
lab.pack(side=TOP, padx=10, pady=10)

lab = Label(win, text="side 인수")
lab.pack(side=BOTTOM, padx=10, pady=10)

lab = Entry(win)
lab.pack(side=LEFT, padx=10, pady=10)

lab = Button(win, text="클릭")
lab.pack(side=RIGHT, padx=10, pady=10)

win.mainloop()