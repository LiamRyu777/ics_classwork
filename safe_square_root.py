import math

print("SQUARE ROOT!")

number = int(input("Enter a number: "))

while True:

    if number < 0:
        print("You can't take the square root of a negative number, silly.")
        number = int(input("Try again: "))
        continue #Jumps back to the loop(While)

    print(f"The square root of {number} is {math.sqrt(number)}")
    break