length = int(input("길이 : "))
distance = int(input("간격 : "))

import turtle
t = turtle.Turtle()
t.shape("turtle")

t.fd(length)

t.up()
t.goto(0, -(distance*1))
t.down()
t.fd(length)

t.up()
t.goto(0, -(distance*2))
t.down()
t.fd(length)
