number = 67
tries = 0
max_tries = 7
print(f"I'm thinking of a number between 1 and 100. You have {max_tries} guesses.")


guess = int(input("First guess: "))
tries += 1


while guess != number and tries < max_tries:
   
    if guess < number:
        print("Sorry. You are too low.")
        guess = int(input(f"Guess #{tries + 1}: "))
        tries += 1
       
    elif guess > number:
        print("Sorry, you are too high.")
        guess = int(input(f"Guess #{tries + 1}: "))
        tries += 1


if guess == number:
    print("You guessed it! What are the odds???")


elif tries >= max_tries:
    print("Sorry, You didn't guess it in 7 tries. YOU LOSE.")
