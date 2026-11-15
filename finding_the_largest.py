import random

array = []
for i in range(10):
    array.append(random.randint(1, 101))

print(f"Array: {array}")

for i in range(len(array)):
    if array[i] == max(array):
        print(f"The largest value in the array is {array[i]} ")