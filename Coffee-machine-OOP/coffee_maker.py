#!/usr/bin/python3

from menu import Menu
class CoffeeMaker:
    """Class coffeeMaker"""
    def __init__(self):
        self.resources = {
            'water': 300,
            'milk': 200,
            'coffee': 100,
            'price': 0
        }
    
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['price']}")
    
    def resources_sufficient(self, ord):
        water = ord.component['water']
        milk = ord.component['milk']
        coffee = ord.component['coffee']
        if (water > self.resources['water']):
            print('Sorry there is not enough water')
            return (0)
        elif (milk > self.resources['milk']):
            print('Sorry there is not enough milk.')
            return (0)
        elif (coffee > self.resources['coffee']):
            print('Sorry there is not enough coffee.')
            return (0)
        else:
            return (1)
    
    def make_coffee(self, ord):
        """Deducts the required ingredients from the resources."""
        self.resources['water'] -= ord.component['water']
        self.resources['milk'] -= ord.component['milk']
        self.resources['coffee'] -= ord.component['coffee']
        self.resources['price'] += ord.price
        print(f"Here is your {ord.name} ☕️. Enjoy!")