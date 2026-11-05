word = input("Enter a word: ")
xyz = "xyz"
i = 0
result = False  # Start by assuming we haven't found a valid "xyz" yet

# 1. Stop the loop 2 characters early so we don't slice past the end of the word
# number to subtract = length of the target word - 1
# • Looking for a 3-letter word ("xyz")? Subtract 2
# • Looking for a 2-letter word ("hi")? Subtract 1
# • Looking for a 4-letter word ("code")? Subtract 3
while i < len(word) - 2:
    if word[i : i + 3] == xyz: 
    # i+3 is not included so if i = 0, we are checking index 0,1,and 2.
        # 2. If we find "xyz", check if it's at the start OR doesn't have a period before it
        if i == 0 or word[i - 1] != ".":
            #if we dont put i == 0, if the word start with xyz, python will check index 0-1
            # which is -1, and it represents the last character of the string, and if that
            # last character is a period, it will return false, which is not what we want.
            result = True  # We found a valid one!
            break  # Stop searching immediately, we have our answer

    i += 1

# 3. Print the final answer just ONCE at the very end
print(result)