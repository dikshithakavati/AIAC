import unittest
from task01 import is_valid_email

class TestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("john.doe@mail.co.uk"))
        self.assertTrue(is_valid_email("a.b@c.d"))
        self.assertTrue(is_valid_email("a@b.c"))
        self.assertTrue(is_valid_email("user_123@domain.co"))

    def test_missing_at(self):
        self.assertFalse(is_valid_email("userexample.com"))

    def test_missing_dot(self):
        self.assertFalse(is_valid_email("user@examplecom"))

    def test_starts_with_at(self):
        self.assertFalse(is_valid_email("@user.com"))

    def test_ends_with_at(self):
        self.assertFalse(is_valid_email("user.com@"))

    def test_starts_with_dot(self):
        self.assertFalse(is_valid_email(".user@example.com"))

    def test_ends_with_dot(self):
        self.assertFalse(is_valid_email("user@example.com."))

    def test_multiple_at(self):
        self.assertFalse(is_valid_email("user@@example.com"))
        self.assertFalse(is_valid_email("user@ex@ample.com"))

    def test_only_special_characters(self):
        self.assertFalse(is_valid_email("@."))
        self.assertFalse(is_valid_email(""))

    def test_at_and_dot_at_ends(self):
        self.assertFalse(is_valid_email("@user.com."))

if __name__ == "__main__":
    unittest.main()