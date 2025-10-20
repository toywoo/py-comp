sum = 0
number = 1
while number <= 100:
    if number % 3 == 0:
        sum += number
    number += 1
print("1부터 100사이의 모든 3의 배수의 합은 %d 입니다." %sum)

