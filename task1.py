def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    Leap year rules:
    1. Year must be divisible by 4
    2. If year is divisible by 100, it must also be divisible by 400
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if it's a leap year, False otherwise
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


# Get input from console and check if it's a leap year
if __name__ == "__main__":
    try:
        year = int(input("Enter a year: "))
        result = is_leap_year(year)
        print(result)
    except ValueError:
        print("Please enter a valid integer year.")

