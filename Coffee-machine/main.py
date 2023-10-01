#!/usr/bin/python3
"""Coffee Machine"""
Menu = {
    'espresso': {
        'component': {
            'water': 50,
            'milk': 0,
            'coffee': 18,
            'price': 1.5
        }
    },
    'latte': {
        'component': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
            'price': 2.5
        }
    },
    'cappuccino': {
        'component': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
            'price': 3.0
        }
    }
}

resources = {
            'water': 300,
            'milk': 200,
            'coffee': 100,
            'price': 0
}


if __name__ == "__main__":
    state = True
    while state:
        res = input("What would you like? (espresso/latte/cappuccino):")
        if res == "off":
            state = False
        elif res == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['price']}")