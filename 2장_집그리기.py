import turtle
t = turtle.Turtle()

t.shape("turtle")
# 사용자로부터 집의 크기를 받아서 size라는 변수에 저장한다. 
size = int(input("집의 크기는 얼마로 할까요? "))

t.left(60)
t.forward(size) 
t.right(120)
t.forward(size) 

t.right(30)
t.forward(size) 
t.right(90)
t.forward(size) 
t.right(90)
t.forward(size) 
t.right(90)
t.forward(size) 

turtle.done()