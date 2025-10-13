import random

options = ['바위', '보', '가위']
user_choice = input("가위, 바위, 보를 입력하시오: ")
computer_choice = random.choice(options)
print(f"컴퓨터: {computer_choice}.")

if user_choice == computer_choice:
    print("비겼습니다. ")
elif user_choice == '바위' and computer_choice == '가위':
    print("컴퓨터가 졌습니다. ")
elif user_choice == '보' and computer_choice == '바위':
    print("컴퓨터가 졌습니다. ")
elif user_choice == '가위' and computer_choice == '보':
    print("컴퓨터가 졌습니다. ")
else:
    print("컴퓨터가 이겼습니다. ")
