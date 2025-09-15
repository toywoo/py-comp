radius = int(input("반지름: "))

import turtle
t = turtle.Turtle()

t.shape("turtle")
t.circle(radius)

t.up()
t.goto(0, radius*2)
t.down()

t.circle(radius/2)
