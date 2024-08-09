from data import menu, resources
is_over = False


def check(storage, coffee):
    # to make espresso we need at least 50ml water and 18g coffee
    # to make latte we need at least 200ml water, 24g coffee and 150ml milk
    # to make cappuccino we need at least 250ml water, 24g coffe and 100ml milk
    water_amount = storage['water']
    coffee_amount = storage['coffee']
    milk_amount = storage['milk']

    if coffee == 'espresso' or coffee == 'latte' or coffee == 'cappuccino':
        if water_amount >= menu[coffee]['ingredients']['water']:
            return True
        elif water_amount < menu[coffee]['ingredients']['water']:
            print("Sorry, there is not enough water.")
            return False
        elif coffee_amount >= menu[coffee]['ingredients']['coffee']:
            return True
        elif coffee_amount < menu[coffee]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee.")
            return False
        elif milk_amount >= menu[coffee]['ingredients']['milk']:
            return True
        else:
            print("Sorry, there is not enough milk.")
            return False


profit = 0


def calculate(coffee):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    if money >= menu[coffee]['cost']:
        if money > menu[coffee]['cost']:
            print(f"Here is ${format(money - menu[coffee]['cost'], ".2f")} in change.")
        return True
    else:
        return False


while not is_over:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_over = True
        break
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if check(resources, choice):
            if calculate(choice):
                print(f"Here is your {choice} ☕ Enjoy!")
                profit += menu[choice]['cost']
                for key in resources:
                    resources[key] -= menu[choice]['ingredients'][key]
            else:
                print("Sorry, that's not enough money. Money refunded.")

