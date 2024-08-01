import random
from words import words
from config import stages, logo

print(logo)
lives = 6
chosen_word = random.choice(words)
display = []
for letter in chosen_word:
    display += '_'

is_game_over = False

while not is_game_over:
    chosen_letter = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == chosen_letter:
            display[position] = chosen_letter

    if chosen_letter not in chosen_word:
        lives -= 1
    print(stages[lives])

    for position in range(len(display)):
        print(display[position], end=" ")

    print("\n")

    if '_' not in display:
        is_game_over = True
        print("You won")
    if lives == 0:
        is_game_over = True
        print("You lost")
