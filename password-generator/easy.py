import random
import config
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
chain = []  # here we store the elements of the password

for i in range(0, nr_letters):
    letter_index = random.randint(0, 51)  # 26 * 2 - 1
    chain.append(config.letters[letter_index])
for i in range(0, nr_symbols):
    symbol_index = random.randint(0, 8)
    chain.append(config.symbols[symbol_index])
for i in range(0, nr_numbers):
    number_index = random.randint(0, 9)
    chain.append(config.numbers[number_index])

for i in range(0, len(chain)):
    print(chain[i], end=""),
