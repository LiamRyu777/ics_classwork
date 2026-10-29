number = 5
print("I have chosen a number between 1 and 10. Try to guess it.")


guess = int(input("Your guess: "))


while guess != number:
    print("That is incorrect. Try again.")
    guess = int(input("Your guess: "))


if guess == number:
    print("That's right! You are a good guesser.")
