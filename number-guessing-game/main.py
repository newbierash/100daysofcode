import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def generate_number():
    number = random.randint(1, 100)
    return number


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
lives = 0
if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5

n = generate_number()
while lives != 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    g = int(input("Make a guess: "))
    if g == n:
        print(f"You got it! The answer was {g}.")
        break
    else:
        if g < n:
            print("Too low.")
        else:
            print("Too high.")
    lives -= 1

if lives == 0:
    print("You've run out of guesses, you lose.")