print("Enter three integers: ")

side_1 = int(input("Side 1: "))
side_2 = int(input("Side 2: "))
side_3 = int(input("Side 3:"))

while True:
    if side_2 < side_1:
        print(f"{side_2} is smaller than {side_1}. Try again.")
    elif side_3 < side_2:
        print(f"{side_3} is smaller than {side_2}. Try again.")

    print(f"your three sides are {side_1} {side_2} {side_3}.")

    if side_3 ** 2 == side_1 ** 2 + side_2 ** 2:
        print("These sides *do* make a right triangle.  Yippy-skippy!")
        break
    else:
        print("NO!  These sides do not make a right triangle!")
        break