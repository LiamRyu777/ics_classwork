input("Are you ready for quiz? ")
print("Ok, here it comes!")

print("Q1) What is the capital of Alaska?")
print("   1) Melbourne")
print("   2) Anchorage")
print("   3) Juneau")
user_answer = int(input())

if user_answer == 3:
    print("That's right!")
elif user_answer == 1 or user_answer == 2:
    print("Sorry, that's wrong.")
else:
    print("Please enter a valid number.")
print()

print("Q2) In Python,the way you get keyboard input is the keyboard_input function.")
print("   1) True")
print("   2) False")
user_answer = int(input())

if user_answer == 2:
    print("That's right!")
elif user_answer == 1:
    print("Sorry, in Python, you would use the \"input\" function to get keyboard input.")
else:
    print("Please enter a valid number.")
print()

print("Q3) What is the result of 9+6/3?")
print("   1) 5")
print("   2) 11")
print("   3) 15/3")
user_answer = int(input())

if user_answer == 2:
    print("That's correct!")
elif user_answer == 1 or user_answer == 3:
    print("Sorry, that's wrong.")
else:
    print("Please enter a valid number.")
