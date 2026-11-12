import random

list_1 = []
list_2 = []

for i in range(10):
    list_1.append(random.randint(1, 101))

for s in range(len(list_1)):
    list_2.append(list_1[s])

list_1[-1] = -7

print(f"list_1: {list_1}")
print(f"list_2: {list_2}")