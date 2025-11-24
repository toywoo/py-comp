from tkinter import	*

def	f_open():
    f_name="d:/python_exam/"+ent.get()
    fhand=open(f_name,	"r")
    t_memo.insert(END,fhand.read())
    fhand.close()  

def	f_save():
    f_name="d:/python_exam/"+ent.get()
    fhand=open(f_name,	"w")
    memo_txt=t_memo.get("1.0",END)
    fhand.close()

win	= Tk()

ent	= Entry(win)
ent.grid(row=0,	column=0)

b_open = Button(win, text="열기", width=10,	command=f_open)
b_open.grid(row=0,	column=1)

b_open = Button(win, text="저장", width=10,	command=f_save)
b_open.grid(row=0,	column=2)

t_memo=Text(win)
t_memo.grid(row=1,column=0,columnspan=3)

win.mainloop()