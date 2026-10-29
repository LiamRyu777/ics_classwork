import random


again = "y"

while True:
    flip = random.randrange(2)  # 0-1

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print("You flip a coin and it is... " + coin)

    again = input("Would you like to flip again (y/n)? ")

    if again != "y":
        break

# Q3.Deleting again = "y" still works with the while True loop
# because the loop does not check the value of again before starting.
# The input statement gives again a value before it is checked.