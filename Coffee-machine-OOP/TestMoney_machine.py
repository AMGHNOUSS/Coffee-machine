
import unittest
from money_machine import MoneyMachine
from menu import MenuItem

class TestMoneyMachine(unittest.TestCase):
    """Class Test for class Money_machine"""

    def setUp(self):
        """Create attribute"""
        self.mm = MoneyMachine()
    
    def test_report(self):
        """Test function report"""
        self.assertEqual(self.mm.report(), None)
    
    def test_calcul(self):
        """Test function calcul"""
        self.assertEqual(self.mm.calcul(), 1.2)
    
    def test_make_coffee_false(self):
        """test function making a coffee."""
        mi = MenuItem("espresso", 1.5, 50, 0, 18)
        self.assertEqual(self.mm.make_coffee(1, mi), False)
    
    def test_make_coffee_true(self):
        """test function making a coffee."""
        mi = MenuItem("espresso", 1.5, 50, 0, 18)
        self.assertEqual(self.mm.make_coffee(1.5, mi), True)