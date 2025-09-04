import unittest
from task5 import convert_date_format

class TestConvertDateFormat(unittest.TestCase):
    def test_valid_dates(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
        self.assertEqual(convert_date_format("2000-01-01"), "01-01-2000")
        self.assertEqual(convert_date_format("1999-12-31"), "31-12-1999")
        self.assertEqual(convert_date_format("2024-04-09"), "09-04-2024")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023/10/15")
        with self.assertRaises(ValueError):
            convert_date_format("2023-10")
        with self.assertRaises(ValueError):
            convert_date_format("15-10-2023")
        with self.assertRaises(ValueError):
            convert_date_format("")

if __name__ == "__main__":
    unittest.main()
