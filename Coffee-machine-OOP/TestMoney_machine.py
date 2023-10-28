
import unittest
from money_machine import MoneyMachine
from menu import MenuItem

class TestMoneyMachine(unittest.TestCase):
    """Class Test for class Money_machine"""

    def setUp(self):
        """Create attribute"""
        self.mm = MoneyMachine()