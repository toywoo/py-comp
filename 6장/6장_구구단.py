dan = int(input("원하는 단은: "))
i = 1

while i <= 9:
    print("%s*%s=%s" %(dan, i, dan*i))
    i += 1

for i in range(1, 10, 1):
    print(f"{dan} * {i} = {dan*i}")