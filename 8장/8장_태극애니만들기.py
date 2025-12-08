import turtle

turtle.title('태극모양')
turtle.shape('turtle')

turtle.color('red')
turtle.begin_fill()
turtle.penup()
turtle.goto(-200,0)
turtle.right(90)
turtle.pendown()

turtle.circle(100,180)
turtle.circle(-100,180)
turtle.left(180)
turtle.circle(200,180)
turtle.end_fill()

turtle.color('blue')
turtle.begin_fill()
turtle.circle(100,180)
turtle.circle(-100,180)
turtle.circle(-200,180)
turtle.end_fill()

turtle.penup()
turtle.goto(0,-300)
turtle.color('black')
turtle.write('태극모양', False, 'center', font=('Gungsuh', 50))
turtle.hideturtle()