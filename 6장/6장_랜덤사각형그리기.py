import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
for i in range(30):
    t.fillcolor(random.random(), random.random(), random.random())
    t.up()
    t.goto(random.randint(-100, 100), random.randint(-100, 100))
    t.down()
    length = random.randint(10, 100)
    height = random.randint(10, 100)
    t.begin_fill()
    for _ in range(2):
        t.forward(length)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
turtle.done()