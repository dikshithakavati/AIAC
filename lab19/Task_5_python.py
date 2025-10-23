class Car:
    """
    A class representing a car with basic attributes.
    
    Attributes:
        brand (str): The brand/manufacturer of the car
        model (str): The model name of the car
        year (int): The manufacturing year of the car
    """
    
    def __init__(self, brand, model, year):
        """Initialize a new Car instance."""
        self.brand = brand
        self.model = model
        self.year = year
    
    def get_info(self):
        """Return a string containing all car information."""
        return f"{self.year} {self.brand} {self.model}"
    
    def __str__(self):
        """String representation of the Car object."""
        return self.get_info()
    
    def display_details(self):
        """Display detailed information about the car."""
        print("Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print("-" * 20)

# Test cases
if __name__ == "__main__":
    # Create some car instances
    car1 = Car("Toyota", "Camry", 2022)
    car2 = Car("Honda", "Civic", 2023)
    car3 = Car("Tesla", "Model 3", 2024)
    
    # Test the car objects using display_details()
    car1.display_details()
    car2.display_details()
    car3.display_details()
    
    # Test string representation
    print("String representation:")
    print(car1)  # This will use __str__ method
