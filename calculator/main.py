from config import logo


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


print(logo)


def calculate():
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    is_over = False

    while not is_over:
        operation_choice = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operation_choice](num1, num2)
        print(f"{num1} {operation_choice} {num2} = {answer}")
        num1 = answer
        over = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()

        if over == "y":
            is_over = False
        elif over == "n":
            calculate()
            is_over = True
        else:
            is_over = True


calculate()
