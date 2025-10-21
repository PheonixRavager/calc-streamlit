import math  # For sqrt

def calculate(num1, num2, operation):
    """
    Perform basic arithmetic or sqrt on num1/num2.
    Raises ValueError for invalid ops, div-by-zero, or negative sqrt.
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "^":  # New: Exponents (num1 ** num2)
        return num1 ** num2
    elif operation == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    elif operation == "sqrt":
        if num1 < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(num1)  # Ignores num2
    else:
        raise ValueError("Invalid operation")