from tkinter import	*

root = Tk()

canvas = Canvas(root, height=400, width=400)
canvas.pack()

c1=canvas.create_line(150, 150, 250, 250, width=5, fill="red")
c2=canvas.create_oval(50, 50, 150, 150, outline="green")
c3=canvas.create_rectangle(300,	300, 350, 350, width=10,	
    outline="blue",	fill="yellow")

canvas.delete(c1,c2)

root.mainloop()