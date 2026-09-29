#1 foot =  0.30 m
#1 inch = 0.03 m 
#1 pound = 0.45 kg

Height_foot = float(input("Height (feet only): "))
Height_inch = float(input("Height (inches): "))
Weight_pound = float(input("Weight in pounds: "))

Height_meter = (Height_foot * 0.30) + (Height_inch * 0.03)
Weight_kilogram = (Weight_pound * 0.45)
bmi = (Weight_kilogram) / (Height_meter ** 2)
print()

print(f"The BMI is {round(bmi , 2)} ") # I rounded cuz I don't like a long line of numbers after a decimal point :)