import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("Steve",200)
        self.drink_1 = Drink("Code Cosmo", 10)
        self.drink_2 = Drink("Method Margarita",12 )
        self.drink_3 = Drink("Python Pina Colada", 12)
        self.pub = Pub("The Prancing Pony", 100.00, [self.drink_1,self.drink_2, self.drink_3 ])

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_drink_count(self):
        self.assertEqual(3, self.pub.pub_drink_count())

    def test_till_has_increased(self):
        self.pub.increase_pub_till(self.drink_1)
        self.assertEqual(110, self.pub.till)
    
    def test_customer_can_buy_drink(self):
        self.pub.sell_drink_to_customer(self.customer_1, self.drink_1)
        self.assertEqual(190, self.customer_1.wallet)
        self.assertEqual(110, self.pub.till)

 

    
    
