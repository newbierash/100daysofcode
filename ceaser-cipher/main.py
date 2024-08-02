from config import alphabet, logo


def ceaser(method, user_text, shift_amount):
    cipher_text = ""
    if method == 'decode':
        shift_amount *= -1
    for letter in user_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if position + shift_amount >= len(alphabet):
                new_position = position + shift_amount - 26
            else:
                new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"Your {method}d text is {cipher_text}")


print(logo)
is_game_over = False

while not is_game_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(direction, text, shift)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        is_game_over = True
        print("Goodbye")
