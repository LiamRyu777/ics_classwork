import random


roll_1 = random.randrange(1, 7)
roll_2 = random.randrange(1, 7)


while True:
    print(f"Roll #1: {roll_1}!")
    print(f"Roll #2: {roll_2}!")
    print(f"The total is {roll_1 + roll_2}!")
    roll_1 = random.randrange(1, 7)
    roll_2 = random.randrange(1, 7)


    if roll_1 == roll_2:
        print(f"Roll #1: {roll_1}!")
        print(f"Roll #2: {roll_2}!")
        print(f"The total is {roll_1 + roll_2}!")
        break
