def safe_divide(numerator, denominator):
    try:
        num1 = float(numerator)
        num2 = float(denominator)
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        elif num2 > 0:
            result = num1 / num2
            print(f"The result of the division is {result}.")
    except ValueError:
        print("Error: Please enter numeric values only.")
