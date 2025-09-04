import unittest
from task03 import is_sentence_palindrome

class TestIsSentencePalindrome(unittest.TestCase):
    def test_palindromes(self):
        self.assertTrue(is_sentence_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_sentence_palindrome("madam"))
        self.assertTrue(is_sentence_palindrome("RaceCar"))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_sentence_palindrome(""))
        self.assertTrue(is_sentence_palindrome("     "))
        self.assertTrue(is_sentence_palindrome("!!!"))
        self.assertTrue(is_sentence_palindrome("x"))
        self.assertTrue(is_sentence_palindrome("@#@!"))
        self.assertTrue(is_sentence_palindrome("12321"))

    def test_non_palindromes(self):
        self.assertFalse(is_sentence_palindrome("Hello, World!"))
        self.assertFalse(is_sentence_palindrome("abc"))
        self.assertFalse(is_sentence_palindrome("12345"))

if __name__ == "__main__":
    unittest.main()