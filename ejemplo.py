from data import *

# ... (otras importaciones)

# TODO: 1. imprimir el informe de todos los recursos de la máquina de café cuando los usuarios ingresan "report"

def report():
    for ingredient, quantity in resources.items():
        print(f"{ingredient}: {quantity}")

# Función para verificar si hay suficientes recursos para hacer la bebida seleccionada
def check_resources(user_order):
    # Itera a través de los ingredientes y las cantidades requeridas en la receta del café seleccionado
    for ingredient, required_quantity in MENU[user_order]["ingredients"].items():
        # Compara la cantidad de ingredientes en la máquina con la cantidad requerida
        if resources[ingredient] < required_quantity:
            # Imprime un mensaje si no hay suficiente cantidad del ingrediente
            print(f"Sorry, there is not enough {ingredient}.")
            return False  # Retorna False si no hay suficientes recursos

    return True  # Retorna True si hay suficientes recursos para hacer la bebida

# TODO: Si hay suficientes recursos para hacer la bebida seleccionada, entonces el programa debe pedir al usuario que inserte monedas. "Por favor, inserta monedas".
def insert_coins(user_order):
    print("Please insert coins.")
    one_yen = int(input("How many 1 yen coins? "))
    five_yen = int(input("How many 5 yen coins? "))
    ten_yen = int(input("How many 10 yen coins? "))
    fifty_yen = int(input("How many 50 yen coins? "))
    onehundred_yen = int(input("How many 100 yen coins? "))
    fivehundred_yen = int(input("How many 500 yen coins? "))

    # Calcula el valor total de las monedas insertadas por el usuario
    total = one_yen * 1 + five_yen * 5 + ten_yen * 10 + fifty_yen * 50 + onehundred_yen * 100 + fivehundred_yen * 500

    # Actualiza el contador de dinero en los recursos de la máquina
    resources["money"] += MENU[user_order]["cost"]

    # Imprime el valor monetario de las monedas insertadas
    print(f"The total value inserted is {total} ¥")

    # Si el total es mayor que el costo del café, calcula el cambio y lo imprime
    if total >= MENU[user_order]["cost"]:
        change_back = total - MENU[user_order]["cost"]
        print(f"The cost of the coffee is {MENU[user_order]['cost']} ¥. Here is {change_back} ¥ in change.")
        return change_back
    else:
        print("Not enough money.")
        return 0

# TODO: igualmente debe restarse de los ingredientes de la máquina, los ingredientes que se usaron para preparar el café
def update_resources(user_order):
    for ingredient, required_quantity in MENU[user_order]["ingredients"].items():
        resources[ingredient] -= required_quantity

def main():
    runing_machine = True

    while runing_machine:
        user_order = input("What would you like? (espresso/latte/cappuccino): ")

        if user_order == "report":
            report()
        elif user_order == "off":
            print("The machine has turned off.")
            runing_machine = False
        elif user_order in MENU:
            if check_resources(user_order):
                change_back = insert_coins(user_order)
                if change_back:
                    update_resources(user_order)

if __name__ == "__main__":
    main()
