word = input("Enter a word: ")
n = int(input("Enter a index of first character where you want to slice before and repeat the string: "))

#REMEMBER!!!
# • To get the last 3 characters: word[-3:]
# • To get the last 4 characters: word[-4:]
# • To get the last n characters: word[-n:]
print(word[-n:] * n)
