import unittest
from utils import validate_isalnum

class TestValidateIsalnum(unittest.TestCase):
    def test_valid_alphanumeric_string(self):
        self.assertTrue(validate_isalnum("abc123"))

    def test_valid_non_alphanumeric_string(self):
        self.assertFalse(validate_isalnum("abc_123"))

    def test_empty_string(self):
        self.assertFalse(validate_isalnum(""))

    def test_whitespace_string(self):
        self.assertFalse(validate_isalnum("   "))

    def test_special_characters_string(self):
        self.assertFalse(validate_isalnum("!@#$%^&*()"))

if __name__ == '__main__':
    unittest.main()