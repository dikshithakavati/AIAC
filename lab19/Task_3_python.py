def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    Args:
        n: A non-negative integer
    Returns:
        The factorial of n
    """
    # Base cases
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Test cases
print(f"Factorial of 5: {factorial(5)}")    # Should print 120
print(f"Factorial of 0: {factorial(0)}")    # Should print 1
print(f"Factorial of 3: {factorial(3)}")    # Should print 6
print(f"Factorial of -1: {factorial(-1)}")  # Should print error message
