def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """
    Divides two numbers and returns the result.

    Args:
        a (float or int): The numerator.
        b (float or int): The denominator.

    Returns:
        float: The result of dividing a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
if __name__ == "__main__":
    x, y = 10, 5
    print("Add:", add(x, y))
    print("Subtract:", subtract(x, y))
    print("Multiply:", multiply(x, y))
    print("Divide:", divide(x, y))

# manual documentation
# declare functions to perform arithmetic operations.
# It includes addition, subtraction, multiplication, and division.
# Each function takes two arguments and returns the result of the operation.
# Division function raises an error if attempting to divide by zero.