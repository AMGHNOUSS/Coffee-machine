#!/usr/bin/python3

from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker 
# The main program.
if __name__ == "__main__":
    state = True
    m = Menu()
    cm = CoffeeMaker()
    mm = MoneyMachine()
    while state:
        res = input(f"What would you like? ({m.get_items()}):")
        if res == "off":
            state = False
        elif res == "report":
            cm.report()
        else:
            ord = m.find_coffee(res)
            if ord != 0:
                correct = cm.resources_sufficient(ord)
                if correct:
                    cost = mm.calcul()
                    Cm1 = mm.make_coffee(cost, ord)
                    if Cm1:
                        cm.make_coffee(ord)