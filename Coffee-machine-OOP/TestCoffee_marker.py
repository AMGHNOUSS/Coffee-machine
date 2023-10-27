
import unittest
from coffee_maker import CoffeeMaker

class TestCoffeeMarker(unittest.TestCase):

    def setUp(self):
        """Initialize attribute"""
        self.cm = CoffeeMaker()
    
    def test_report(self):
        """Test function report"""
        self.assertEqual(self.cm.report(), None)