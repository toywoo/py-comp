import tkinter
import tkinter.messagebox

def myFunc():
    tkinter.messagebox.showinfo("버튼 클릭", "버튼을 눌렀군요 ^^")

root = tkinter.Tk()
root.geometry("300x100-300+200")

button1 = tkinter.Button(root, text="클릭하세요", bg="yellow", fg="red"
                         , command=myFunc)

button1.pack()

root.mainloop()