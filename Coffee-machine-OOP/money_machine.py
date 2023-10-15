#!/usr/bin/python3

class MoneyMachine:
    """Class Money machine"""
    profit = 0
    def __init__(self):
        self.CURRENCY = '$'
        self.quarters = 0.25
        self.dimes = 0.1
        self.nickles = 0.05
        self.pennies = 0.01
    
    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")
    
    def calcul(self):
        """Calcul Money"""
        q = input("How many quarters:")
        d = input("How many pennies:")
        n = input("How many nickles:")
        p = input("How many dimes:")
        result = (self.quarters * float(q)) + (self.dimes * float(d)) + \
        (self.nickles * float(n)) + (self.pennies * float(p))
        return result
    
    def make_coffee(self, cost, ord):
        """Return True when payment is accepted, or False if insufficient."""
        if cost < ord.price:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif cost == ord.price:
            return True
        else:
            result = cost - ord.price
            print("Here is ${:.2f} in change.".format(result))
            return True