# WEIGHT CONVERTER

weight = float(input("Enter your weight : "))
unit = input("Enter unit (kg->K/lbs->L): ")

if unit == "K":
    weight *= 2.2
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight /= 2.2
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is invalid!!")

