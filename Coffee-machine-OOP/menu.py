#!/usr/bin/python3

class MenuItem:
    """Class MenuItem"""
    def __init__(self, name, price, water, milk, coffee):
        self.name = name
        self.price = price
        self.component = {
            'water': water,
            'milk': milk,
            'coffee': coffee
        }

class Menu:
    """Class Menu"""
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 1.5, 50, 0, 18),
            MenuItem("latte", 2.5, 200, 150, 24),
            MenuItem("cappuccino", 3.0, 250, 100, 24)
        ]
    
    def get_items(self):
        options = ""
        for item in self.menu:
            options += item.name + "/"
        return options

    def find_coffee(self, name_coffee):
        for item in self.menu:
            if name_coffee == item.name:
                return item
            print("This coffee was not available.")