def safe_divide(numerator, denominator):
    try:
        num1 = float(numerator)
        num2 = float(denominator)
        divide = num1 / num2
        # print(num1)
        # print(num2)
        return f"The result of the division is {divide}"
    except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError:
            return "Error: Please enter numeric values only."

