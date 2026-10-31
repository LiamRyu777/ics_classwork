# Create a loop that will add the numbers from 5 to 20 but not any multiples of 3. Use modulus.

num = 5
total = 0
while num < 20:
    num += 1
    if num % 3 == 0:
        continue
    total += num
print(total)
