from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def start_machine():
    menu = Menu()
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    running = True

    while running:
        user_request = input("What would you like? ")

        if user_request == 'report':
            money_machine.report()
            coffee_maker.report()

        elif user_request == 'off':
            print('Shutting off...')
            running = False

        else:
            drink = menu.find_drink(user_request)
            if drink:
                can_make = coffee_maker.is_resource_sufficient(drink)
                if can_make:
                    enought_money = money_machine.make_payment(drink.cost)
                    if enought_money:
                        coffee_maker.make_coffee(drink)


start_machine()
