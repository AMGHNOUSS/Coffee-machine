
import unittest
from coffee_maker import CoffeeMaker
from menu import MenuItem

class TestCoffeeMarker(unittest.TestCase):

    def setUp(self):
        """Initialize attribute"""
        self.cm = CoffeeMaker()
    
    def test_report(self):
        """Test function report"""
        self.assertEqual(self.cm.report(), None)
    
    def test_resources_sufficient(self):
        """Test function resources sufficient"""
        mi = MenuItem("espresso", 1.5, 50, 0, 18)
        self.assertEqual(self.cm.resources_sufficient(mi), 1)