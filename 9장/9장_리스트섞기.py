import random

menu = ['apple','banana','pineapple','grape','strawberry' ]

for i in range(5):
    print(random.choice(menu))

random.shuffle(menu)
print(menu)