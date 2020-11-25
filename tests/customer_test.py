import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Beer", 5)
        self.customer = Customer("Guido van Rossum", 200)
    
    
    def test_customer_has_name(self):
        self.assertEqual("Guido van Rossum", self.customer.name)


    def test_customer_has_wallet(self):
        self.assertEqual(200, self.customer.wallet)

    def test_decrease_customer_wallet(self):
        self.customer.decrease_customer_wallet(self.drink)
        self.assertEqual(195, self.customer.wallet)
