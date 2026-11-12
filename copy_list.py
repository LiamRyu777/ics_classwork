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

#Q1.The reason why list_2 = list_1 work is because though it copies the list, when we change the value of list_1 it also changes list_2 and
# we only want to change the element of list_1 only so we are separating two lists.
