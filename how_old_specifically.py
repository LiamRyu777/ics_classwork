name = input("Hey, what is your name? (Sorry I keep forgetting): ")
age = int(input(f"Ok, {name}, how old are you?: "))

if age < 16:
    print("You can't drive.")
elif age == 16 or age == 17:
    print("You can drive but not vote.")
elif age > 17 and age < 21:
    print("You can vote but not rent a car.")
else:
    print("You can do pretty much anything.")

