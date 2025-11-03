import turtle
t=turtle.Turtle()
t.shape("turtle")

xpoint=0
ypoint=0

for i in range(1, 6):
    for j in range(0, i):
        t.circle(20)
        t.up()
        xpoint += 50
        t.goto(xpoint, ypoint)
        t.down()
        
    xpoint = 0
    ypoint -= 50
    
    t.up()
    t.goto(xpoint, ypoint)
    t.down()
