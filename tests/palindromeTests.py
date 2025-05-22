import unittest

from functions import IsPalindrom

class TestPalindrom(unittest.TestCase):
    def test_palindrom_anna_should_be_true(self):
        # Arrange
        input = "Anna"
        expected = True
        # Act
        result = IsPalindrom(input)
        # Assert
        self.assertEqual(result, expected)

    def test_palindrom_test_should_be_false(self):
        # Arrange
        input = "test"
        expected = False

        # Act
        result = IsPalindrom(input)

        # Assert
        self.assertEqual(result, expected)

    def test_palindrom_with_spaces_should_be_true(self):
        # Arrange
        input = "nurses run"
        expected = True
        # Act
        result = IsPalindrom(input)
        # Assert
        self.assertEqual(result, expected)

    def test_palindrom_mixed_case_should_be_true(self):
        # Arrange
        input = "RaCeCaR"
        expected = True
        # Act
        result = IsPalindrom(input)
        # Assert
        self.assertEqual(result, expected)