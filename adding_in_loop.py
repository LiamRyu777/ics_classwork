print("I will add up the numbers you give me.")


result = 0
number = int(input())
result += number




while number != 0:
    print(f"The total so far is {result}")
    number = int(input())
    result += number
if number == 0:
    print(f"The total is {result}")
