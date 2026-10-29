PIN = "12345"


print("WELCOME TO THE BANK OF LIAM.")
entry = input("ENTER YOUR PIN: ")


while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")




print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")


#1. While loop is similar to if statement because it works only if the value is True
#2. While loop infinitely repeats unless stopped manually unlike if statement
#3. then we should change entry=input() to entry=int(input()).
#4. the string "INCORRECT PIN. TRY AGAIN" infinitely repeats.
