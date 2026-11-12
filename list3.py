import random

list = []

for i in range(10):
    list.append(random.randint(1, 101))

for s in range(len(list)):
    print(f"slot {s} contains a {list[s]}")