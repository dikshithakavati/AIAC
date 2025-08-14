def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
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
    
    while True:
        try:
            # Get input from user
            user_input = input("Enter a non-negative integer (or 'quit' to exit): ")
            
            # Check if user wants to quit
            if user_input.lower() in ['quit', 'q', 'exit']:
                print("Goodbye!")
                break
            
            # Convert input to integer
            number = int(user_input)
            
            # Calculate factorial
            if number < 0:
                print("Error: Please enter a non-negative integer.")
                continue
                
            result = factorial(number)
            print(f"The factorial of {number} is: {result}")
            
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Error: Please enter a valid integer.")
            else:
                print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        print()  # Empty line for better readability

if __name__ == "__main__":
    main()
