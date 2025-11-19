from tkinter import *

win = Tk()

lab = Label(win, text="pack 알아보기", height=2, width=30, bg="gray")
lab.grid(row=0, columnspan=2)

end = Label(win, text="위치지정", height=2, bg="gray")
end.grid(row=2, columnspan=2)

ent = Entry(win)
ent.grid(row=1, column=0)

but = Button(win, text="클릭", width=6, height=2, bg="green",
             activebackground="red")
but.grid(row=1, column=1)

win.mainloop() 
