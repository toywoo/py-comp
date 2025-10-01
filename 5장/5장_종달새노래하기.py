import random, datetime
time = random.randint(1, 24)
now = datetime.datetime.now()

print("지금 시각은" + str(time) + "시 입니다.")
# print("현재 시각은" + str(now.hour) + "시 입니다.")

sunny = random.choice([True, False])
if sunny:
    print("현재 날씨가 화창합니다.")
else:
    print("현재 날씨가 화창하지 않습니다.")

if time >= 6 and time < 9 and sunny:
    print("종달새가 노래를 한다.")
else:
    print("종달새가 노래를 하지 않는다.")
