import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.kaija = Customer("Kaija",50)

    def test_customer_has_name (self):
        self.assertEqual("Kaija",self.kaija.name)

    def test_customer_cash(self):
     self.assertEqual(20,self.customer.wallet)

     def test_customer_can_buy_drink(self):
         drink= Drink("Macallan", 20)
         self.customer.buy_drink(drink)
         self.asserEqual(30,self.customer.wallet)

    

