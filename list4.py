import random

list = []

for i in range(1000):
    list.append(random.randint(10, 100))

for num in list:
    print(num, end=" ")