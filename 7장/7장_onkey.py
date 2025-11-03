import	turtle
t=turtle.Turtle()
s=turtle.Screen()
t.shape('turtle')

def	up():
    t.setheading(90)
    t.forward(100)
def	down():
    t.setheading(-90)
    t.forward(100)
def	right():
    t.setheading(0)
    t.forward(100)
def	left():
    t.setheading(180)
    t.forward(100)
def	star():
	for	i in range(5):
        t.forward(50)
        t.left(144)

s.onkey(up,	"Up")
s.onkey(down,	"Down")
s.onkey(right,	"Right")
s.onkey(left,	"Left")
s.onkey(star,	"s")
s.listen()	
s.mainloop()