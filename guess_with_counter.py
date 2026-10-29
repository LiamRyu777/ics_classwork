number = 5
tries = 0


print("I have chosen a number between 1 and 10. Try to guess it.")
guess = int(input("Your guess: "))
tries += 1


while guess != number:
    print("That is incorrect. Try it again.")
    guess = int(input("Your guess: "))
    tries += 1


if guess == number:
    print("That's right! You are a good guesser.")
    print(f"It only took you {tries} times.")

