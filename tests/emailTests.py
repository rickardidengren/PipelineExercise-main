import unittest
from functions import IsValidEmail


class EmailTests(unittest.TestCase):
    def test_valid_email_with_se_domain_should_be_true(self):
        # Arrange 
        email = "test@example.se"
        # Act
        result = IsValidEmail(email)
        # Assert
        self.assertTrue(result)

    def test_valid_email_with_com_domain_should_be_true(self):
        # Arrange 
        email = "user@mail.com"
        # Act
        result = IsValidEmail(email)
        # Assert
        self.assertTrue(result)

    def test_email_missing_at_sign_should_be_false(self):
        # Arrange – saknar "@"
        email = "userexample.com"
        # Act
        result = IsValidEmail(email)
        # Assert
        self.assertFalse(result)

    def test_email_missing_dot_should_be_false(self):
        # Arrange 
        email = "user@examplecom"
        # Act
        result = IsValidEmail(email)
        # Assert
        self.assertFalse(result)