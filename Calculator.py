# CALCULATOR PROGRAM

num1 = float(input("Enter the first value: "))
num2 = float(input("Enter the second value: "))
operator = input("Enter the operator (+, -, *, /, ^): ")

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
elif operator == "^":
    result = pow(num1,num2)
    print(round(result, 2))
else:
    print("INVALID OPERATOR!!🤬")


