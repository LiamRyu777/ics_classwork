# Ask the user for a starting number and an ending number. The program will get the sum of all the numbers from the 
# start to the end (using a loop). However, our program is a bit of a diva: 
# the program will stop summing the numbers 
# if it encounters a 13 or a 31. It will still output the sum up to that point.

start = int(input("Enter your first number: "))
end = int(input("Enter your ending number: "))
sum = 0
while start <= end:
    if start == 13 or start == 31:
        break
    sum += start
    start += 1
print(sum)
