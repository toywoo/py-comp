import turtle
t = turtle.Turtle()

t.shape("turtle")
t.speed(10)

t.fillcolor("blue")
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(100)

t.fillcolor("orange")
t.begin_fill()
t.circle(120)
t.end_fill()

t.up()
t.goto(-300, -200)
t.down()

t.fillcolor("green")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

t.up()
t.right(90)
t.forward(200)
t.down()

t.fillcolor("red")
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()

turtle.done()
