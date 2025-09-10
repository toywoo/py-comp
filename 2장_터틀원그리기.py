import webbrowser

s = input("번역할 영어 문장을 입력하시오 : ")
url = "https://translate.google.co.kr/#en/ko/"+s
webbrowser.open(url)

import turtle
radius = int(input("반지름 : "))
length = int(input("진행 : "))

turtle.shape("turtle")

turtle.circle(radius)
turtle.forward(length)

turtle.circle(radius)
turtle.forward(length)

turtle.circle(radius)
turtle.forward(length)