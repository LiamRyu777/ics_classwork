print("Enter the following information about an item you wish to purchase..")
print()

name = input("The name of the item: ")

price = float(input("The price: $"))    

quantity = int(input("How many do you want?: "))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")

"""
1.As I used above, the difference between user input of name 
and user input of price is the difference of the value, as                                                  
name is represented as string, while price is represented as a float.
This is because apples, which I wanted to put in "name" is a string type value(however I didnt put str() cuz 
string is like the default value of input so unless it is instructed to change into different value type it will in 
default,convert user input into string value.), while 
0.5, which I was going to put in price is float value. 

3. The prompt is something we tell users what they are expected to enter. Therefore, it is basically an instruction
for user. However, if the prompt line comes later, users have no idea what to enter, because there is no instruction 
given explaining what to enter.                     

4.As I mentioned in the middle of #1, the default value that user input is converted into is string value. Therefore,
if you, for example, put 0.05 for price, that 0.05 is converted into not a float value, but a string value. And the
reason why we are using float() and int() is because we want to perform some mathematical calculations with user input,
but with string value it is impossible to do it.
"""