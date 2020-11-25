class Customer :
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
 
 #Customer buys drink from pub
    def decrease_customer_wallet(self, drink):
        self.wallet -= drink.price
        


       