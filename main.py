from data import *





# TODO: 1. print the report of all coffe machine resource, when the users enter "report"

def report():
    #accedo a cada clave el diccionario
    for ingredient in resources:
        
        #imprimo la clave junto con su valor por medio del metodo de dicc para acceder al valor del diccionario
        print(f"{ingredient}:  {resources[ingredient]}")
  

# TODO: When the user ask for a coffee, we need to check if there are enough resources to make the drink      
def check_resources(user_order):

    # print(MENU["espresso"])
        
    # ciclo para acceder a los valores del diccionario "resources"
    for ingredient in resources:
        
        #Comparo la cantidad de ingrediente que se necesita para preparar el espresso con la que actualmente hay en la maquina
        if ingredient == "water": 
            #comparo la cantidad de agua actual dentro de la maquina, con la que necesitamos para preparar el espreso
            if resources[ingredient]>MENU[user_order]["ingredients"]["water"]:
                
                #si es correcto esta variable "repare_coffee" sera igual a true y evaluamos  este valor en un condicional para decirle al usuario que ingrese las monedas
                prepare_coffee=True
                

                
            else:
                print(f"sorry there is not enough {ingredient}")
                
        
        if ingredient == "coffee": 
            #comparo la cantidad de cafe actual dentro de la maquina, con la que necesitamos para preparar el espreso
            if resources[ingredient]>MENU[user_order]["ingredients"]["coffee"]:
                
                prepare_coffee=True
                
            else:
                print(f"sorry there is not enough {ingredient}")
                
        #espreso es el unio caffe que no utiliza leche por eso usamos este condicional para verificar el caffe actual es o o no espresso, si es espresso no entrara en el condicional        
        if user_order!="espresso":     
               
            if ingredient == "milk": 
                #comparo la cantidad de leche actual dentro de la maquina, con la que necesitamos para preparar el espreso
                if resources[ingredient]>MENU[user_order]["ingredients"]["milk"]:
                    
                    prepare_coffee=True
                    
                    
                else:
                    print(f"sorry there is not enough {ingredient}")     
    
    return prepare_coffee               
        
        

# TODO: If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins. "PLease insert coins"
def insert_coins():
    
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
    
    #en nuestro diccionario "resources" actualizamos el valor de "money" que seria igual al precio del caffe
    resources["money"]  = resources["money"]+ MENU[user_order]["cost"]  
    
    print(resources)
    
    # TODO: Calculate the monetary value of the coins inserted1
    print(f"The total value inserted is {total }")
    
    if total > MENU[user_order]["cost"]:
        change_back=total - MENU[user_order]["cost"]  
        
        print(f"The cost of the coffee is {MENU[user_order]['cost']} ￥, Here is {change_back}￥ in change. ")
        print()
        
    
    else:
        print("Not enough money")
             
                    
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
        
        
        if check_resources(user_order) == True:
            insert_coins()  
            resources["water"]  = resources["money"]+ MENU[user_order]["cost"]  
        
    elif user_order == "latte":
        if check_resources(user_order) == True:
            insert_coins()  
        
    elif user_order == "cappuccino":
        if check_resources(user_order) == True:
            insert_coins()  
        
            
    








# TODO: Turn off the Coffee Machine by entering “off” to the prompt.

#TODO: agregar al contador de la maquina la cantidad de dinero incertada, el valor de "money" debe actualizarce

#TODO: igualmente debe restarse de los ingredientes de la maquina, los ingredientes que se usaron para preparar el cafe

