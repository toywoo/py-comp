import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("사각형그리기", "이름을 입력하시오: ")
t.write("안녕하세요?" + s + "씨, 터틀 인사드립니다.")

for i in range(0, 4) :  
    t.left(90)
    t.fd(100)
