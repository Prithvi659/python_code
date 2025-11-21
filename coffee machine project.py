# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 10.0,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 20.0,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 30.0,
#     }
# }
#
#
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
# def res():
#     wat=resources["water"]
#     mil=resources["milk"]
#     coff=resources["coffee"]
#     print( f" water={wat}lts , milk={mil}lts ,coffee={coff}grams ")
#
#
# def process_order(drink):
#     ingredient=MENU[drink]["ingredients"]
#     for iteam in ingredient:
#         if ingredient[iteam] < resources[iteam]:
#             print("insufficient  resources",iteam)
#         return False
#     for iteam in ingredient:
#         resources[iteam]-=ingredient[iteam]
#     return True
#
#
#
# def coin():
#     num_ones=int(input("enter the one ruppe coins = "))
#     num_twos=int(input("enter the two ruppe coins = "))
#     num_fives=int(input("enter five ruppe coins = "))
#     coins=(num_ones*1)+(num_twos*2)+(num_fives*5)
#     print("your total value = ",coins)
#     return coins
#
#
#
#
#
# def espresso():
#     print(MENU["espresso"]["cost"])
#     print(f"the cost is above")
#     money=coin()
#     change=0
#
#     if money >= 10:
#         print("thank for the order please wait")
#         change=10-money
#         print("your change is :",change)
#
#     else:
#         print("insufficent money enter again")
#
# def latte():
#     print(MENU["latte"]["cost"])
#     print(f"the cost is above")
#     money=coin()
#     change=0
#     if money >= 20:
#         print("thank for the order please wait")
#         change=20-money
#         print("your change is :",change)
#     else:
#         print("insufficient money enter again")
#
#
# def cappuccino():
#     print(MENU["cappuccino"]["cost"])
#     print(f"the cost is above")
#     money=coin()
#     change=0
#     if money >= 30:
#         print("thank for the order please wait")
#         change=30-money
#         print("your remaining change is :",change)
#     else:
#         print("insufficient money enter again")
#
#
# print("welcome to the coffe machine")
# is_input=True
# while is_input:
#     coffe=input("what do want ( 'espresso' , 'latte' , 'cappuccino', 'Exit' , 'resources' ) \n").lower()
#     if coffe == "espresso":
#         espresso()
#         process_order(espresso())
#     elif coffe == "latte":
#         latte()
#         process_order(latte())
#     elif coffe== "cappuccino":
#         cappuccino()
#         process_order(cappuccino())
#     elif coffe == "exit":
#         is_input=False
#     elif coffe == "resources":
#         res()
#     else:
#         print("invaild input enter again")
#         is_input=False
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 10.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 20.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def res():
    print(f"water = {resources['water']} lts, milk = {resources['milk']} lts, coffee = {resources['coffee']} grams")


def process_order(drink):
    ingredients = MENU[drink]["ingredients"]

    # Check resources
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False

    # Deduct resources
    for item in ingredients:
        resources[item] -= ingredients[item]

    return True


def coin():
    num_ones = int(input("enter the one rupee coins = "))
    num_twos = int(input("enter the two rupee coins = "))
    num_fives = int(input("enter five rupee coins = "))
    coins = (num_ones * 1) + (num_twos * 2) + (num_fives * 5)
    print("your total value =", coins)
    return coins


def make_drink(drink):
    cost = MENU[drink]["cost"]
    print(cost)
    print("the cost is above")

    money = coin()

    if money < cost:
        print("insufficient money, enter again.")
        return

    if not process_order(drink):
        print("Order cancelled, returning money.")
        return

    print("Thank you for the order, please wait...")
    change = money - cost
    print("Your change is:", change)


print("welcome to the coffee machine")
is_input = True

while is_input:
    coffee = input("what do want ( 'espresso' , 'latte' , 'cappuccino', 'Exit' , 'resources' ) \n").lower()

    if coffee in MENU:
        make_drink(coffee)

    elif coffee == "exit":
        is_input = False

    elif coffee == "resources":
        res()

    else:
        print("invalid input, enter again.")
