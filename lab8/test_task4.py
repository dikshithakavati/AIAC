import unittest
from task4 import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("apple", 1.0)
        self.assertIn("apple", self.cart.items)
        self.assertEqual(self.cart.items["apple"], 1.0)

    def test_remove_item(self):
        self.cart.add_item("banana", 0.5)
        self.cart.remove_item("banana")
        self.assertNotIn("banana", self.cart.items)

    def test_total_cost(self):
        self.cart.add_item("apple", 1.0)
        self.cart.add_item("banana", 0.5)
        self.assertEqual(self.cart.total_cost(), 1.5)
        self.cart.remove_item("apple")
        self.assertEqual(self.cart.total_cost(), 0.5)

    def test_remove_nonexistent_item(self):
        self.cart.add_item("apple", 1.0)
        self.cart.remove_item("orange")  # Should not raise error
        self.assertIn("apple", self.cart.items)

    def test_empty_cart_total(self):
        self.assertEqual(self.cart.total_cost(), 0)

if __name__ == "__main__":
    unittest.main()