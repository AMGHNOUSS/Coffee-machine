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
    
    def reportt(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['price']}")
    
    def ressources_sufficient(self, name):
        for item in self.menu:
            if name == item.name:
                water = item.component['water']
                milk = item.component['milk']
                coffee = item.component['coffee']
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