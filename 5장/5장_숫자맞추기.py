from random import *

answer = randint(1, 10)
print("숫자 게임에 오신 것을 환영합니다.")
g = input("숫자를 맞춰 보세요:")
guess = int(g)

if guess == answer:
    print("사용자 (%d) > 컴퓨터 (%d)" %(guess, answer))
elif guess > answer:
    print("사용자 (%d) > 컴퓨터 (%d)" %(guess, answer))

else:
    print("사용자 (%d) < 컴퓨터 (%d)" %(guess, answer))

print("게임 종료")