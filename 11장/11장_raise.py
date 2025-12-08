test_list = [1, 2, 3, 4, 5, 6]
try:
    for num in test_list:
        if num % 3 == 0: raise Exception("3의 배수 발견") 
        print(num)
except Exception as e:
    print("예외 발생:", e)