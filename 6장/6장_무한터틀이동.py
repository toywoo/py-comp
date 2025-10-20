
import turtle

tShape = input("거북이 모양 ==>")
turtle.shape(tShape)
tPensize = int(input("거북이 선 두께 ==> "))
turtle.pensize(tPensize)
tColor = input("거북이 색상 ==> ")
turtle.color(tColor)

while True:
    angle = int(input("거북이의 회전 각도: "))
    distance = int(input("거북이의 이동 거리: "))
    turtle.right(angle)
    turtle.fd(distance)
