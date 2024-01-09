from data import *





# TODO: 1. print the report of all coffe machine resource, when the users enter "report"

def report():
    #accedo a cada clave el diccionario
    for ingredient in resources:
        
        #imprimo la clave junto con su valor por medio del metodo de dicc para acceder al valor del diccionario
        print(f"{ingredient}:  {resources[ingredient]}")
  

# TODO When the user ask for a coffee, we need to check if there are enough resources to make the drink      
def check_resources(user_order):

    # print(MENU["espresso"])
        
    # ciclo para acceder a los valores del diccionario "resources"
    for ingredient in resources:
        
        #Comparo la cantidad de ingrediente que se necesita para preparar el espresso con la que actualmente hay en la maquina
        if ingredient == "water": 
            #comparo la cantidad de agua actual dentro de la maquina, con la que necesitamos para preparar el espreso
            if resources[ingredient]>MENU[user_order]["ingredients"]["water"]:
                print("enough water")
                
            else:
                print(f"sorry there is not enough {ingredient}")
        
        if ingredient == "coffee": 
            #comparo la cantidad de leche actual dentro de la maquina, con la que necesitamos para preparar el espreso
            if resources[ingredient]>MENU[user_order]["ingredients"]["coffee"]:
                
                print("enough coffee")
            
            else:
                print(f"sorry there is not enough {ingredient}")
        
        if user_order!="espresso":     
               
            if ingredient == "milk": 
                #comparo la cantidad de leche actual dentro de la maquina, con la que necesitamos para preparar el espreso
                if resources[ingredient]>MENU[user_order]["ingredients"]["milk"]:
                    
                    print("enough milk")
                
                
                else:
                    print(f"sorry there is not enough {ingredient}")      

# TODO If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins. "PLease insert coins"
def insert_coins():
    print("Please insert coins.")
    one_yen=int(input("How many 1 yen coins?"))
    five_yen=int(input("How many 5 yen coins?"))
    ten_yen=(input("How many 10 yen coins?"))
    fifty_yen=(input("How many 50 yen coins?"))
    onehundred_yen=(input("How many 100 yen coins?"))
    fivehundred_yen=(input("How many 500 yen coins?"))
    total=one_yen * 1 + five_yen * 5 + ten_yen * 10 + fifty_yen * 50 + onehundred_yen * 100 + fivehundred_yen * 500               
                    
#variable para encender o apagar la maquina 
runing_machine=True

#si es igual a Tru es decir encendida
while runing_machine==True:
    
    # TODO: Ask the user "What would you like? (espresso/latte/cappuccino):"
    user_order = input("What would you like? (espresso/latte/cappuccino): ")   
     
    #si el usuario ingresa "report" mostrar el estado de los ingredientes dentro de la maquina 
    if user_order == "report":
        
        #funcion que muestra el estado de los ingredientes dento de la maquina
        report()
    
       
    elif user_order == "espresso":
        check_resources(user_order)
        
    elif user_order == "latte":
        check_resources(user_order)
        
    elif user_order == "cappuccino":
        check_resources(user_order)
        
            
    




# TODO Calculate the monetary value of the coins inserted.

# TODO: When action is completed and the drink is dispensed, the message "What would you like?... " should show again

# TODO: Turn off the Coffee Machine by entering “off” to the prompt.

