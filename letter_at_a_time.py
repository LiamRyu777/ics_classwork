message = input("What is your message? ")


print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")


for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")


vowels = "aeiou"
vowel_count = 0

for i in range(len(message)):
    char = message[i]
    print(f"{i} - '{char}'")
    
    if char.lower() in vowels:
        vowel_count += 1

print(f"Your message contains {vowel_count} vowels.")

# Q1: If I print range(7), it prints itself, and if I convert in a list it shows the sequence of numbers as list
# Q2: 5, because "Hello" is 5 characters long, and the digits corresponding each are 0,1,2,3,4.
# Q3: 3, and index is 2 because the first digit is 0 not 1.
# Q4: 