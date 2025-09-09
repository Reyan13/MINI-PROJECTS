unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9 / 5) + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round(5 / 9 * (temp - 32), 1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is invalid!")