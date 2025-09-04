import unittest
from task0 import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator(2, 3, 'add'), 5)
        self.assertEqual(calculator(-1, 1, 'add'), 0)

    def test_subtract(self):
        self.assertEqual(calculator(5, 3, 'subtract'), 2)
        self.assertEqual(calculator(0, 10, 'subtract'), -10)

    def test_multiply(self):
        self.assertEqual(calculator(4, 5, 'multiply'), 20)
        self.assertEqual(calculator(-2, 3, 'multiply'), -6)

    def test_divide(self):
        self.assertEqual(calculator(10, 2, 'divide'), 5)
        self.assertEqual(calculator(9, 3, 'divide'), 3)

    def test_divide_by_zero(self):
        self.assertEqual(calculator(10, 0, 'divide'), "Error: Division by zero")

    def test_unknown_operation(self):
        self.assertEqual(calculator(1, 2, 'mod'), "Error: Unknown operation")
        self.assertEqual(calculator(1, 2, ''), "Error: Unknown operation")
if __name__ == '__main__':
    unittest.main()