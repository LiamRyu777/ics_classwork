print("Type in a message, and I'll display it 5 times.")


message = input("Message: ")
print()


n = int(input("How many times? "))
count = 0
end_point = n * 10
while count < end_point:
    print(f"{count + 10}. {message}")
    count += 10


# Q1. If we exclude n += 1, the message is printed out infinitely unless pressing ctrl + c.
