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

def check_resources(drink):
    water = Menu[drink]['component']['water']
    milk = Menu[drink]['component']['milk']
    coffee = Menu[drink]['component']['coffee']
    if (water > resources['water']):
        print('Sorry there is not enough water')
        return 0
    if (milk > resources['milk']):
        print('Sorry there is not enough milk.')
        return 0
    if (coffee > resources['coffee']):
        print('Sorry there is not enough coffee.')
        return 0
    return (1)

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