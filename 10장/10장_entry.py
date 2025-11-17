from tkinter import *

window = Tk()
window.geometry("300x200")

entry = Entry(window)
entry.insert(0, "입력창입니다")
entry.pack()

window.mainloop()