import unittest
from datetime import datetime
from person import Person  

class TestPerson(unittest.TestCase):
    def test_namnge_should_set_name_when_valid(self):
        # Arrange 
        person = Person(Birthdate=datetime(1990, 1, 1))
        new_name = "Anna"
        # Act
        result = person.Namnge(new_name)
        # Assert
        self.assertTrue(result)
        self.assertEqual(person.Namn, new_name)

    def test_namnge_should_fail_on_short_name(self):
        # Arrange 
        person = Person(Birthdate=datetime(1990, 1, 1))
        new_name = "A"
        # Act
        result = person.Namnge(new_name)
        # Assert
        self.assertFalse(result)
        self.assertEqual(person.Namn, "") 

    def test_flytta_in_hos_should_copy_address_fields(self):
        # Arrange – den häe funktionen gör det möjligt för en person att flytta in hos en annan person
        #vi testar om så är fallet
        p1 = Person(Birthdate=datetime(1990, 1, 1))
        p2 = Person(
            Birthdate=datetime(1985, 5, 5),
            GatuAddress="Storgatan 1",
            PostNummer=12345,
            Postort="Stockholm"
        )
        # Act
        p1.FlyttaInHos(p2)
        # Assert
        self.assertEqual(p1.GatuAddress, p2.GatuAddress)
        self.assertEqual(p1.PostNummer, p2.PostNummer)
        self.assertEqual(p1.Postort, p2.Postort)