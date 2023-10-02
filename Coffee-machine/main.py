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

# Function for if there are enough resources to make that drink.
def check_resources(drink):
    water = Menu[drink]['component']['water']
    milk = Menu[drink]['component']['milk']
    coffee = Menu[drink]['component']['coffee']
    if (water > resources['water']):
        print('Sorry there is not enough water')
        return (0)
    elif (milk > resources['milk']):
        print('Sorry there is not enough milk.')
        return (0)
    elif (coffee > resources['coffee']):
        print('Sorry there is not enough coffee.')
        return (0)
    else:
        return (1)

# Function for calculate the monetary value of the coins inserted.
def process_coins():
    quarters = input("How many quarters:")
    dimes = input("How many pennies:")
    nickles = input("How many nickles:")
    pennies = input("How many dimes:")
    result = (0.25 * float(quarters)) + (0.10 * float(dimes)) + \
        (0.05 * float(nickles)) + (0.01 * float(pennies))
    return (result)

# Function Check that the user has inserted enough money 
# #to purchase the drink they selected.
def check_transaction(drink, reslt):
    if reslt < Menu[drink]['component']['price']:
        print("Sorry that's not enough money. Money refunded.")
    elif reslt == Menu[drink]['component']['price']:
        make_cofffe(drink)
        print(f"Here is your {drink} ☕️. Enjoy!")
    else:
        result = reslt - Menu[drink]['component']['price']
        make_cofffe(drink)
        print(f"Here is your {drink} ☕️. Enjoy!")
        print("Here is ${:.2f} in change.".format(result))

# Function to make a coffee 
def make_cofffe(drink):
    resources['water'] = resources['water'] - Menu[drink]['component']['water']
    resources['milk'] = resources['milk'] - Menu[drink]['component']['milk']
    resources['coffee'] = resources['coffee'] - Menu[drink]['component']['coffee']
    resources['price'] = resources['price'] + Menu[drink]['component']['price']

# The main program.
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
        elif (res in ['espresso', 'latte', 'cappuccino']):
            if check_resources(res):
                coins = process_coins()
                check_transaction(res, coins)