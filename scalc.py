num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))
operator = input("Enter the Operator (+, -, *, /) : ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid Operator")

print("Result :", result)