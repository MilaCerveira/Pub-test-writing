class Pub():
    def __init__(self, name, till, drinks):
        self.name = name 
        self.till = till
        self.drinks = drinks
    
    def pub_drink_count(self):
        return len(self.drinks)
    
    def increase_pub_till(self, drink):
        self.till += drink.price

    def sell_drink_to_customer(self, customer, drink):
        self.increase_pub_till(drink)
        customer.decrease_customer_wallet(drink)

    
        


# method
    #  def sell_pet_to_customer(self, pet_name, customer):
    #     pet = self.find_pet_by_name(pet_name)
    #     customer.add_pet(pet)
    #     self.remove_pet(pet)
    #     self.increase_pets_sold()
    #     self.increase_total_cash(pet.price)

# test
    #   def test_can_sell_pet_to_customer(self):
    #         customer = Customer("Jack Jarvis", 1000)
    #     self.pet_shop.sell_pet_to_customer("Sir Percy", customer)
    #     self.assertEqual(1, customer.pet_count())
    #     self.assertEqual(1, self.pet_shop.stock_count())
    #     self.assertEqual(1, self.pet_shop.pets_sold)
    #     self.assertEqual(1500, self.pet_shop.total_cash)
    

