from tkinter import *

window = Tk()

w = Label(window, text="박스 #1", bg="red", fg="white")
w.place(x=0, y=0, width=100, height=30)

w = Label(window, text="박스 #2", bg="green", fg="black")
w.place(x=50, y=50)

w = Label(window, text="박스 #3", bg="blue", fg="white")
w.place(x=100, y=100)

window.mainloop()