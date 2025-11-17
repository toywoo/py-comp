import tkinter
import tkinter.messagebox

def myFunc():
    tkinter.messagebox.showinfo(" ", "체크버튼 ON 이네요.")

root = tkinter.Tk()
root.geometry("300x100-100+100")

cb1 = tkinter.Checkbutton(root, text="클릭하세요"
                         , command=myFunc)

cb1.pack()

root.mainloop()