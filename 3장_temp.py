sec = int(input("초를 입력하세요: "))

hour = sec // 3600
min = sec % 3600 // 60
second = sec % 3600 % 60

print("입력한 시간은", hour, "시간", min, "분", second, "초 입니다.")


x =	int(input("금액 :	"))

x500 = x // 500
t =	x %	500												

x100 = t // 100
t =	t %	100

x50 = t // 50
t =	t %	50

x10 = t // 10
print("500원:",	x500, "100원:", x100, "50원:", x50, "10원:", x10)