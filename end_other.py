word_1 =input("Enter a word: ")
word_2 =input("Enter a word: ")

if word_2.lower() in word_1.lower() or word_1.lower() in word_2.lower():
    print("True")
else:
    print("False")