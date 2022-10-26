import unittest
from src.pub import Pub


class TestPub(unittest.TestCase):
    def setUp(self):
        self.my_pub = Pub("The Chanter",100)

    def test_pub_has_name(self):
        self.assertEqual("The Chanter",self.my_pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100,self.my_pub.till)

    def test_pub_can_have_drinks(self):
        self.assertEqual(0,len(self.my_pub.drinks))

    def test_increase_till(self):
        self.my_pub.increase_till(20)
        expected = 120
        actual=self.put.till
        self.assertEqual(expected,actual)








