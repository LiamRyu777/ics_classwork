word = input("Enter a word: ")
result = ""

for char in range(len(word)):
    result +=word[char] * 2

print(result)