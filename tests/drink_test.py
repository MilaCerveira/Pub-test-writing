import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Code Cosmo", 10)
        self.drink_2 = Drink("Method Margarita",12 )
        self.drink_3 = Drink("Python Pina Colada", 12)

    def test_drink_has_name(self):
        self.assertEqual("Code Cosmo", self.drink_1.name)
    
    def test_drink_has_price(self):
        self.assertEqual(10, self.drink_1.price)