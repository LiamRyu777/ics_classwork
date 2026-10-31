print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(0, 5, 2): #range((start), (stop), (increase))
    print(f"{n}. {message}")

#Q1. Nothing really happens, I think it is because n stands for "number".
# Q2. 0 is the number it starts, while 5 is a number it ends(but does not include).
#Q3. If we make third number 2, the number goes up by 2.