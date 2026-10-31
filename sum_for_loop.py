integer = int(input("Number: "))

sum = 0

for i in range(1, integer + 1, 1):
    print(i)
    sum += i

print(f"The total is {sum}")
