def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
    """
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def main():
    """Main function to get user input and calculate factorial"""
    print("Factorial Calculator")
    print("=" * 20)
    
    try:
        # Get input from user
        user_input = input("Enter a number: ")
        
        # Convert input to integer
        number = int(user_input)
        
        # Calculate factorial
        result = factorial(number)
        
        if result is None:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {number} is: {result}")
            
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
