MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check(coffee): #check resources to see if there's enough to make selection
    if MENU[coffee]['ingredients']['water'] > resources['water']:
            print("Sorry there is not enough water")
            return False
    if MENU[coffee]['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee")
            return False
    if coffee != 'espresso':
        if MENU[coffee]['ingredients']['milk'] > resources['milk']:
            print("Sorry there is not enough milk")
            return False
    return True

def correct_amount(total, cost): #calculate if user has enough money, if so add profit and return change
    if total < cost:
        print("Sorry, that is not enough money. Money Refunded")
    elif total == cost:
        resources['profit'] += cost
    else:
        refund = round(total - cost,2)
        print(f"Here is ${refund} in change.")
        resources['profit'] += cost

def payment(): #calculate total from user payment
    print("Please insert payment")
    quarters = int(input("How many Quarters?"))
    dimes = int(input("How many Dimes?"))
    nickles = int(input("How many Nickles?"))
    pennies = int(input("How many Pennies?"))
    total = round((quarters*.25)+(dimes*.1)+(nickles*.05)+(pennies*.01),2)
    print(f'${total}')
    return total

def sub_resources(coffee): #subtract selected items ingredients from resources
    resources["water"] -= MENU[coffee]['ingredients']['water']
    resources["coffee"] -= MENU[coffee]['ingredients']['coffee']
    if coffee != 'espresso':
        resources["milk"] -= MENU[coffee]['ingredients']['milk']
    return

def operate(): #main program call
    rerun = True #set rerun to true to allow for more users to order
    resources['profit']=0 #add profit to dictionary
    while rerun:
        coffee = input("What would you like? (espresso/latte/cappuccino): ").lower() #ask for user selection
        if coffee == 'off': #allow for machine to be turned off
            return False
        if coffee == 'report': #run report
            print(resources)
        else:
            if check(coffee): #check if resources are available, if they are proceed
                correct_amount(payment(), MENU[coffee]['cost']) #call function correct amount which passes return from payment function and the selected item cost
                sub_resources(coffee) #call sub resources to subtract from resources
            else:
                return False #if not enough resources exit

operate() #call main function