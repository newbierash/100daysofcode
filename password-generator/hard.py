import config
import random
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
chain = []  # here we store the elements of the password
length = nr_letters + nr_symbols + nr_numbers

for i in range(0, length):
    order = random.randint(0, 2)
    if order == 0:
        letter_index = random.randint(0, 51)  # 26 * 2 - 1
        chain.append(config.letters[letter_index])
    elif order == 1:
        symbol_index = random.randint(0, 8)
        chain.append(config.symbols[symbol_index])
    elif order == 2:
        number_index = random.randint(0, 9)
        chain.append(config.numbers[number_index])

for i in range(0, len(chain)):
    print(chain[i], end=""),
