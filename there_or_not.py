import random

list = []

for i in range(10):
    list.append(random.randint(1, 51))

print(f"List: {list}")

value_to_find = int(input("Enter a value to find in the list: "))

count = 0
for i in range(len(list)):
    if list[i] == value_to_find:
        count += 1
if count > 0:
    print(f"{value_to_find} isin the list.")
else:
    print(f"{value_to_find} is not in the list.")