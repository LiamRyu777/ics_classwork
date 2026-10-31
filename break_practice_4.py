# Create an infinite loop using while True:. In that loop ask the user for a word. 
# For each word they enter, output the following "Your word: {word}". 
# If ever they enter the word "stop" the program will break out of the loop. 
# Finally the program will output "Goodbye!".


while True:
    word = input("Your word: ")
    if word != "stop":
        print(f"Your word: {word}")
    else:
        break
print("Goodbye!")