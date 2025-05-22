import unittest

from functions import canIBuyBeer


class TestAlcoholPurchase(unittest.TestCase):
    def test_underage_at_krogen_should_be_false(self):
        # Arrange 
        age = 17
        location = "K"
        promille = 0.5
        # Act
        result = canIBuyBeer(age, location, promille)
        # Assert
        self.assertFalse(result)

    def test_legal_age_at_krogen_and_under_promille_limit_should_be_true(self):
        # Arrange
        age = 18
        location = "K"
        promille = 0.5
        # Act
        result = canIBuyBeer(age, location, promille)
        # Assert
        self.assertTrue(result)

    def test_underage_at_systemet_should_be_false(self):
        # Arrange 
        age = 18
        location = "S"
        promille = 0.5
        # Act
        result = canIBuyBeer(age, location, promille)
        # Assert
        self.assertFalse(result)

    def test_legal_age_at_systemet_and_under_promille_limit_should_be_true(self):
        # Arrange 
        age = 20
        location = "S"
        promille = 0.5
        # Act
        result = canIBuyBeer(age, location, promille)
        # Assert
        self.assertTrue(result)

    def test_legal_age_and_high_promille_should_be_false_at_krogen(self):
        # Arrange 
        age = 25
        location = "K"
        promille = 1.2
        # Act
        result = canIBuyBeer(age, location, promille)
        # Assert
        self.assertFalse(result)

    def test_legal_age_and_high_promille_should_be_false_at_systemet(self):
        # Arrange 
        age = 25
        location = "S"
        promille = 1.2
        # Act
        result = canIBuyBeer(age, location, promille)
        # Assert
        self.assertFalse(result)