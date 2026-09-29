print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
print("there are " + str(33 - 11) + " boys.") # does 33 minus 11 which is 22 and converts into a string value to make sentence
print()
print(f"That means {11 / 33} % are girls...") # divides 11 by 33 and prints the result(0.33333....)
print("and {} % are boys.".format((33 - 11) / 33)) # the mathematical operations is done in the .format() and the result is printed inside {}.
print()
print("If we made groups of six...")
print(f"There would be {33 // 6} groups of six.") #prints the quotient of 33 divided by 6 (=5)
print(f"And then a smaller group of {33 % 6} people.") #prints the remainder of 33 divided by 6 (=3)
print("-" * 30) # there would be 30 of these "-" printed in a line.
print("If we had 17 apples and 3 people...")
print(f"Each person would get {17 // 3} whole apples.") #prints the quotient of 17 divided by 3 (=5)
print("There would be " + str(17 % 3) + " apples remaining.") #prints the remainder of 17 divided by 3, then string-ifies it. (=2)
print()
print("If we charged each person $2 each for their 5 apples..") 
print("they would each pay ${}.".format(2 * 5)) #the result of 2*5(=10) is printed inside {}.

#f strings, dot format, concatenation 

# -> f strings
print(f"The result of 2+5 is {2 + 5}.") #output = the result of 2+5 is 7.")

# -> dot format
print("The result of 2+5 is {}".format( 2 + 5 )) #output = the result of 2+5 is 7.

# -> concatenation
print("The " + "result " + "of " + "2+5 " + "is " + "7 " + ".") #output = the result of 2+5 is 7.

