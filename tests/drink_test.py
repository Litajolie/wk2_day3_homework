import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.whisky = Drink("Macallan",20)

    def test_drink_has_name(self):
        self.assertEqual("Macallan",self.whisky.name)

    def test_drink_has_price(self):
        self.assertEqual(20,self.whisky.price)

    def test_drink_price(self):
        expected = 20
        actual = self.drink.price
        self.assertEqual(expected,actual)