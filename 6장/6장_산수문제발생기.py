import random

while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print (x, "+", y, "=", end = "")

    answer = int(input())
    if anser == x + y:
        print("잘했어요!!")
    else:
        print("다음번에는 잘 할 수 있죠?")