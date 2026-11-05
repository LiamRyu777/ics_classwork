word_1 = input("Enter a word: ")
word_2 = input("Enter a word: ")

i = 0
result = ""

while i <len(word_1) and i < len(word_2):
    result += word_1[i] + word_2[i]
    i += 1

print(result)