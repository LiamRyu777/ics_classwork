import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 51))

print(f"List: {numbers}")
value_to_find = int(input("Enter a value to find in the list: "))

found = False
for i in range(len(numbers)):
    if numbers[i] == value_to_find:
        print(f"{value_to_find} is at index {i}.")
        found = True

if not found:
    print(f"{value_to_find} is not in the list.")
