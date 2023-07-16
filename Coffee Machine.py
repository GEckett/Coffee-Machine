# imports
from Machine_data import MENU
from Machine_data import resources

# TODO 4: Check resources sufficient? (E.g. if Latte requires 200ml water but there is only 100ml left in the machine.
#  It should not continue to make the drink but print: “Sorry there is not enough water.”)


def resource_check(order):
    """Checks to see if there's enough water, milk and coffee to make the chosen drink"""
    drink_water = MENU[order]['ingredients']['water']
    if order == "espresso":
        drink_milk = 0
    else:
        drink_milk = MENU[order]['ingredients']['milk']
    drink_coffee = MENU[order]['ingredients']['coffee']
    if drink_water < resources['water']:
        if drink_milk < resources['milk']:
            if drink_coffee < resources['coffee']:
                return True
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough milk")
    else:
        print("Sorry there is not enough water")

# TODO 5: Process coins (If there are sufficient resources to make the drink selected, then the program should
#  prompt the user to insert coins.Calculate the monetary value of the coins inserted


def insert_coins():
    """The process that lets the user add coins and then returns the total money they added."""
    print("Please insert coins")
    n1 = float(input("how many quarters?:")) * 0.25
    n2 = float(input("how many dimes?:")) * 0.1
    n3 = float(input("how many nickels?:")) * 0.05
    n4 = float(input("how many pennies?:")) * 0.01
    return n1 + n2 + n3 + n4

# TODO 6: Check transaction successful.
#  Check that the user has inserted enough money to purchase the drink they selected.
#  But if the user has inserted enough money, then the cost of the drink gets added to the
#  machine as the profit and this will be reflected the next time.
#  If the user has inserted too much money, the machine should offer change.
#  E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
#  places.

# TODO 7: Make Coffee
#  If the transaction is successful and there are enough resources to make the drink the
#  user selected, then the ingredients to make the drink should be deducted from the
#  coffee machine resources.


def transaction(order, cash_added):
    """Checks user has inserted enough money to purchase the drink they selected.Adds money to machine if true.
    Gives user change if applicable"""
    order_cost = MENU[order]['cost']
    if cash_added < order_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(cash_added - order_cost, 2)
        global money
        money += order_cost
        if order == "espresso":
            resources['water'] -= MENU[order]['ingredients']['water']
            resources['coffee'] -= MENU[order]['ingredients']['coffee']
        else:
            resources['water'] -= MENU[order]['ingredients']['water']
            resources['coffee'] -= MENU[order]['ingredients']['coffee']
            resources['milk'] -= MENU[order]['ingredients']['milk']
        print(f"Here is ${change} in change.\nHere is your {order.title()} ☕️. Enjoy!")

# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino)
# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3: Print report.


off = False
MENU
resources
money = 0
while not off:
    order = input("What would you like? (espresso/latte/cappuccino)").lower()
    if order == "off":
        off = True
    elif order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g"
              f"\nMoney: ${money}")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        ok_to_pour = resource_check(order)
        if ok_to_pour:
            cash_added = round(insert_coins(), 2)
            transaction(order, cash_added)









