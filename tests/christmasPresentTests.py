import unittest
from christmasPresent import Person, ChristmasPresent  

class TestPersonPresents(unittest.TestCase):

    def test_add_present_should_store_present(self):
        # Arrange
        person = Person("Anna")
        present = ChristmasPresent("Bok", 150.0)
        # Act
        person.AddPresent(present)
        # Assert
        self.assertIn(present, person.Presenter)

    def test_get_total_should_sum_prices(self):
        # Arrange
        person = Person("Nisse")
        p1 = ChristmasPresent("Game", 299.0)
        p2 = ChristmasPresent("Socks", 49.0)
        person.AddPresent(p1)
        person.AddPresent(p2)
        # Act
        total = person.GetTotal()
        # Assert
        self.assertEqual(total, 348.0)

    def test_get_total_should_be_zero_if_no_presents(self):
        # Arrange
        person = Person("Karl")
        # Act
        total = person.GetTotal()
        # Assert
        self.assertEqual(total, 0.0)