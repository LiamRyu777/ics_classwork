word = input("Enter a word: ")
i = 0
result = False  # Start by assuming we haven't found a valid "bob" yet

# 1. Stop the loop 2 characters early so we don't slice past the end of the word
# number to subtract = length of the target word - 1
# • Looking for a 3-letter word ("xyz")? Subtract 2
# • Looking for a 2-letter word ("hi")? Subtract 1
# • Looking for a 4-letter word ("code")? Subtract 3
while i < len(word) - 2:
       if word[i] == "b" and word[i + 2] == "b":
            result = True
            break
    i += 1

# 3. Print the final answer just ONCE at the very end
print(result)