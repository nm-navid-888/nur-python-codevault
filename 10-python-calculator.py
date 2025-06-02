# Python Calculator with Conditions

# Take inputs
try:
    input1 = float(input("Enter the first number: "))
    input2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /, %): ")

    # Perform calculation
    if operator == "+":
        result = input1 + input2
        print("The result is", result)
    elif operator == "-":
        result = input1 - input2
        print("The result is", result)
    elif operator == "*":
        result = input1 * input2
        print("The result is", result)
    elif operator == "/":
        if input2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = input1 / input2
            print("The result is", result)
    elif operator == "%":
        if input2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = input1 % input2
            print("The result is", result)
    else:
        print("Invalid operator. Please use one of +, -, *, /, %.")

except ValueError:
    print("Error: Please enter valid numbers.")
    