def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def display_menu():
    """Display the temperature conversion menu"""
    print("\n" + "=" * 50)
    print("TEMPERATURE CONVERSION CALCULATOR")
    print("=" * 50)
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    print("=" * 50)

def get_temperature_input(unit_name):
    """Get temperature input from user with validation"""
    while True:
        try:
            temp = float(input(f"Enter temperature in {unit_name}: "))
            return temp
        except ValueError:
            print(f"Invalid input! Please enter a valid number for {unit_name}.")

def perform_conversion(choice):
    """Perform the selected temperature conversion"""
    if choice == '1':
        celsius = get_temperature_input("Celsius")
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"\n{celsius}°C = {fahrenheit:.2f}°F")
        
    elif choice == '2':
        fahrenheit = get_temperature_input("Fahrenheit")
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"\n{fahrenheit}°F = {celsius:.2f}°C")
        
    elif choice == '3':
        celsius = get_temperature_input("Celsius")
        kelvin = celsius_to_kelvin(celsius)
        print(f"\n{celsius}°C = {kelvin:.2f}K")
        
    elif choice == '4':
        kelvin = get_temperature_input("Kelvin")
        celsius = kelvin_to_celsius(kelvin)
        print(f"\n{kelvin}K = {celsius:.2f}°C")
        
    elif choice == '5':
        fahrenheit = get_temperature_input("Fahrenheit")
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"\n{fahrenheit}°F = {kelvin:.2f}K")
        
    elif choice == '6':
        kelvin = get_temperature_input("Kelvin")
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"\n{kelvin}K = {fahrenheit:.2f}°F")
        
    else:
        print("Invalid choice!")

def main():
    """Main program function with looping menu"""
    print("Welcome to Temperature Conversion Calculator!")
    
    while True:
        display_menu()
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '7':
            print("\nThank you for using Temperature Conversion Calculator!")
            print("Goodbye!")
            break
            
        elif choice in ['1', '2', '3', '4', '5', '6']:
            perform_conversion(choice)
            
        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()