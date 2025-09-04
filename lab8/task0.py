def calculator(a, b,operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unknown operation"
if __name__ == "__main__":
    print(calculator(10, 5, 'add'))        # Output: 15
    print(calculator(10, 5, 'subtract'))   # Output: 5
    print(calculator(10, 5, 'multiply'))   # Output: 50
    print(calculator(10, 5, 'divide'))     # Output: 2.0
    print(calculator(10, 0, 'divide'))     # Output: Error: Division by zero
    print(calculator(10, 5, 'mod'))        # Output: Error: Unknown operation