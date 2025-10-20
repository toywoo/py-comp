number = int(input("정수를 입력하세요: "))
sum = 0
while number > 0:
    digit = number % 10
    sum += digit
    number //= 10
print("자리수의 합은 %d 입니다." %sum)

