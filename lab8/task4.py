class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store item names and their prices

    def add_item(self, name, price):
        """Add an item with the specified name and price to the cart."""
        self.items[name] = price

    def remove_item(self, name):
        """Remove an item by name from the cart if it exists."""
        if name in self.items:
            del self.items[name]

    def total_cost(self):
        """Calculate and return the total cost of all items in the cart."""
        return sum(self.items.values())


if __name__ == "__main__":
    # Your main code here (e.g., instantiating ShoppingCart, calling methods)
    pass
# Example usage:
# cart = ShoppingCart()
# cart.add_item("apple", 1.0)
# cart.add_item("banana", 0.5)
# print(cart.total_cost())  # Output: 1.5
# cart.remove_item("apple")
# print(cart.total_cost())  # Output: 0.5
    # Example usage:
    cart = ShoppingCart()
    cart.add_item("apple", 1.0)
    cart.add_item("banana", 0.5)
    print(cart.total_cost())  # Output: 1.5
    cart.remove_item("apple")
    print(cart.total_cost())  # Output: 0.5