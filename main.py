# TODO: 1. print the report of all coffe machine resource, when the users enter "report"
from data import *

# TODO: Ask the user "What would you like? (espresso/latte/cappuccino):"
user_order = input("What would you like? (espresso/latte/cappuccino): ")

if user_order == "report":
    print(f"""
    Water: {resources["water"]}
    Milk: {resources["milk"]}
    Coffee: {resources["coffee"]}
    Money: {resources["money"]}

    """)

# TODO When the user ask for a coffee, we need to check if there are enough resources to make the drink

# TODO If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins. "PLease insert coins"

# TODO Calculate the monetary value of the coins inserted.

# TODO: When action is completed and the drink is dispensed, the message "What would you like?... " should show again

# TODO: Turn off the Coffee Machine by entering “off” to the prompt.

