from turtle import *
shape("turtle")
color("orange")

def move():
    fd(50)
    lt(60) 

onkeypress(move, "w")
listen()
mainloop()