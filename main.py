menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def enough_resources(orde_ingredients):
    for k in resources:
        if resources[k] < orde_ingredients[k]:
            print(f"sorry there is not enough {k}")
            return False
    return True


def enough_money(money, coffe_cost):
    if money >= coffe_cost:
        print(f"Here is your {choice}. Enjoy!")
        global profit
        profit += coffe_cost
        for k in resources:
            resources[k] -= menu[choice]['ingredients'][k]
    else:
        print('Sorry thats not enough money')


start = True
while start:
    choice = input("What would you like? espresso/latte/cappuccino: ").lower()
    if choice == 'off':
        print('Thank You')
        start = False
    elif choice == 'report':
        for k,v in resources.items():
            print(f"{k}: {v}ml")
        print(f"profit: {profit}$")
    elif choice in menu:
        drink = menu[choice]
        if enough_resources(drink['ingredients']):
            money = float(input(f"please pay {menu[choice]['cost']}$: "))
            enough_money(money,drink['cost'])
    else:
        print("please provide proper choice")





