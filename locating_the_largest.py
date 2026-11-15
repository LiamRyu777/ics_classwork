import random

list = []
for i in range(10):
    list.append(random.randint(1, 101))

print(f"List: {list}")

for i in range(len(list)):
    if list[i] == max(list):
        print(f"The largest value is {list[i]}")
        print(f"it is at index {i}")