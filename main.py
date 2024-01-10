from data import *

from Logos import *

from Instructions import *

import os

# TODO: 1. print the report of all coffe machine resource, when the users enter "report"

def report():
    #accedo a cada clave el diccionario
    for ingredient, quantity in resources.items():
        
        #imprimo la clave junto con su valor por medio del metodo de dicc para acceder al valor del diccionario
        print(f"{ingredient}: {quantity}")
  

# TODO: When the user ask for a coffee, we need to check if there are enough resources to make the drink      
def check_resources(user_order):
    
    # Itera a través de los ingredientes y las cantidades requeridas en la receta del café seleccionado
    for ingredient, required_quantity in MENU[user_order]["ingredients"].items():
        # Compara la cantidad de ingredientes en la máquina con la cantidad requerida
        if resources[ingredient] < required_quantity:
            # Imprime un mensaje si no hay suficiente cantidad del ingrediente
            print(f"Sorry, there is not enough {ingredient}.")
            return False  # Retorna False si no hay suficientes recursos

    return True  # Retorna True si hay suficientes recursos para hacer la bebida


        
        

# TODO: If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins. "PLease insert coins"
def insert_coins(user_order):
    
    #el usario inserta laas monedas con que va a pagar respectivamente
    print("Please insert coins.")
    one_yen=int(input("How many 1 yen coins?"))
    
    five_yen=int(input("How many 5 yen coins?"))
    
    ten_yen=int(input("How many 10 yen coins?"))
    
    fifty_yen=int(input("How many 50 yen coins?"))
    
    onehundred_yen=int(input("How many 100 yen coins?"))
    
    fivehundred_yen=int(input("How many 500 yen coins?"))
    
    #calculamos el valor total de dinero insertado por el usuario
    total=one_yen * 1 + five_yen * 5 + ten_yen * 10 + fifty_yen * 50 + onehundred_yen * 100 + fivehundred_yen * 500          
    
    # Actualiza el contador de dinero en los recursos de la máquina
    resources["money"]  = resources["money"]+ MENU[user_order]["cost"]  
    
   
    # Imprime el valor monetario de las monedas insertadas
    print(f"The total value inserted is {total }")
    
    # Si el total es mayor que el costo del café, calcula el cambio y lo imprime
    if total > MENU[user_order]["cost"]:
        
        change_back=total - MENU[user_order]["cost"]  
        
        print(f"The cost of the coffee is {MENU[user_order]['cost']} ￥, Here is {change_back}￥ in change. ")
        print()
        
        paid=True
        #retornamos la variable "paid"
        return paid
        
        
    
    else:
        print("Not enough money")
        paid=False
        #retornamos la variable "paid"
        return paid
             

#TODO: igualmente debe restarse de los ingredientes de la maquina, los ingredientes que se usaron para preparar el cafe

def update_resources(user_order):
    # Itera sobre cada elemento (par clave-valor) en los ingredientes necesarios para la bebida seleccionada.
    # ingredient es la clave (nombre del ingrediente), y required_quantity es el valor (cantidad requerida de ese ingrediente).
    for ingredient, required_quantity in MENU[user_order]["ingredients"].items():
        # Resta la cantidad requerida de cada ingrediente del diccionario de recursos.
        resources[ingredient] -= required_quantity

 
 
def main():                   
    #variable para encender o apagar la maquina 
    runing_machine=True

    #si es igual a Tru es decir encendida
    while runing_machine==True:
        # os.system('cls')#limpiamos la consola
        
        
       
        
        # TODO: Ask the user "What would you like? (espresso/latte/cappuccino):"
        user_order = input("What would you like? (espresso/latte/cappuccino): ")   
        
        #si el usuario ingresa "report" mostrar el estado de los ingredientes dentro de la maquina 
        if user_order == "report":
            
            #funcion que muestra el estado de los ingredientes dento de la maquina
            report()
        
        # TODO: Turn off the Coffee Machine by entering “off” to the prompt.
        elif user_order == "off":
            print("the machine has turned off")
            runing_machine=False
            
        elif user_order in MENU:  
            if check_resources(user_order):  
                
                
                if insert_coins(user_order)==True:
            
                    update_resources(user_order)
                    print(f"Here is your {user_order} ☕️. Enjoy!")
                    print()
        # elif user_order == "espresso":
            
            
        #     if check_resources(user_order) == True:

                
            
        # elif user_order == "latte":
        #     if check_resources(user_order) == True:
        #         insert_coins(user_order)  
        #         update_resources(user_order)
        #         print(f"Here is your {user_order} ☕️. Enjoy!")
        #         print()
                
        # elif user_order == "cappuccino":
        #     if check_resources(user_order) == True:
        #         insert_coins(user_order)  
        #         update_resources(user_order)
        #         print(f"Here is your {user_order} ☕️. Enjoy!")
        #         print()
        

print(titule)
print(logo)
print(instructions)
print()
main()









