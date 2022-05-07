weight_string = input("Weight? ")   # ask user for input (string)
weight = float(weight_string)     # convert input to float
height = float(input("Height? "))  # combines both in 1 statement

bmi = weight / (height * height) # bmi = 18.9...
print(bmi)

if bmi < 18:   # 18.9 < 18 is False
    print("Underweight")   # this will not execute
elif 18 <= bmi <= 25:    # normal weight
    print("Normal weight")
elif 25 < bmi <= 30:
    print("Overweight")
else:
    print("Obese")

# it does not belong to else
print("End of program.")