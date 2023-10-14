#!/usr/bin/python3

class MoneyMachine:
    """Class Money machine"""
    def __init__(self):
        self.quarters = 0.25
        self.dimes = 0.1
        self.nickles = 0.05
        self.pennies = 0.01
    
    def calcul(self, q, d, n, p):
        """Calcul Money"""
        result = (self.quarters * float(q)) + (self.dimes * float(d)) + \
        (self.nickles * float(n)) + (self.pennies * float(p))
        return result