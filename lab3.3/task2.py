def sort_ascending(numbers):
    """Sort numbers in ascending order"""
    return sorted(numbers)

def sort_descending(numbers):
    """Sort numbers in descending order"""
    return sorted(numbers, reverse=True)

def sort_odd_numbers(numbers):
    """Filter and sort only odd numbers in ascending order"""
    odd_nums = [num for num in numbers if num % 2 != 0]
    return sorted(odd_nums)

def sort_even_numbers(numbers):
    """Filter and sort only even numbers in ascending order"""
    even_nums = [num for num in numbers if num % 2 == 0]
    return sorted(even_nums)

def get_numbers_from_user():
    """Get a list of numbers from user input"""
    while True:
        try:
            user_input = input("Enter numbers separated by spaces (e.g., 5 2 8 1): ")
            
            if not user_input.strip():
                print("Please enter some numbers.")
                continue
            
            numbers = []
            for item in user_input.split():
                try:
                    num = float(item)
                    if num.is_integer():
                        numbers.append(int(num))
                    else:
                        numbers.append(num)
                except ValueError:
                    print(f"Warning: '{item}' is not a valid number, skipping...")
            
            if numbers:
                return numbers
            else:
                print("No valid numbers entered. Please try again.")
                
        except Exception as e:
            print(f"An error occurred: {e}")

def display_menu():
    """Display the sorting menu options"""
    print("\n" + "=" * 40)
    print("SORTING MENU")
    print("=" * 40)
    print("1. Sort in ascending order")
    print("2. Sort in descending order")
    print("3. Sort odd numbers only")
    print("4. Sort even numbers only")
    print("5. Exit")
    print("=" * 40)

def main():
    """Main program function"""
    print("Number Sorting Program")
    print("=" * 30)
    
    # Get numbers from user
    numbers = get_numbers_from_user()
    print(f"\nYour list: {numbers}")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                result = sort_ascending(numbers)
                print(f"\nAscending order: {result}")
                
            elif choice == '2':
                result = sort_descending(numbers)
                print(f"\nDescending order: {result}")
                
            elif choice == '3':
                result = sort_odd_numbers(numbers)
                if result:
                    print(f"\nOdd numbers (ascending): {result}")
                else:
                    print("\nNo odd numbers found in the list.")
                    
            elif choice == '4':
                result = sort_even_numbers(numbers)
                if result:
                    print(f"\nEven numbers (ascending): {result}")
                else:
                    print("\nNo even numbers found in the list.")
                    
            elif choice == '5':
                print("\nThank you for using the Number Sorting Program!")
                break
                
            else:
                print("\nInvalid choice! Please enter a number between 1 and 5.")
                
        except ValueError:
            print("\nInvalid input! Please enter a number.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()