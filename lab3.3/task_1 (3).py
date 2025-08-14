def factorial_recursive(n):
    """
    Calculate the factorial of a given number using recursion.
    Assumes the input is a non-negative integer.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage and testing
if __name__ == "__main__":
    # Test the recursive factorial function
    test_numbers = [0, 1, 2, 3, 4, 5]
    
    print("Testing Recursive Factorial Function")
    print("=" * 35)
    
    for num in test_numbers:
        result = factorial_recursive(num)
        print(f"{num}! = {result}")
    
    # Interactive testing
    print("\n" + "-" * 35)
    try:
        user_input = input("Enter a number to calculate factorial: ")
        number = int(user_input)
        
        if number < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            result = factorial_recursive(number)
            print(f"{number}! = {result}")
            
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")
