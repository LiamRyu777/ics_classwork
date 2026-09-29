store = "No Frills"
item = "Apples"
price = 0.4
quantity = 10
subtotal = price * quantity
tax = subtotal * 0.13
total = tax + subtotal

print(f"at {store} I bought some {item}.") #f-strings
print("They sold for $" + str(price) + " each.") #concatenation
print("I wanted to purchase {} of them. ".format(quantity)) #dot format
print(f"The tax was included which was 5% of the subtotal, ${subtotal}, was ${round(tax, 2)}")#f-strings
print(f"The total price, with tax included, was ${round(total, 2)}.") #<-- Without f in the front, the output would be "The total price, with tax included, was ${round(total, 2)}." instead of the actual value of total.


