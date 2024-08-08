from data import data
import random
score = 0
is_over = False


def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}."


def compare(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    elif b_followers > a_followers:
        return guess == 'b'


account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)

while not is_over:
    print(f"Compare A: {format_data(account_a)}")
    print("VS")
    print(f"Against B: {format_data(account_b)}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_account = account_a['follower_count']
    b_follower_account = account_b['follower_count']

    is_correct = compare(choice, a_follower_account, b_follower_account)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")

        if choice == 'b':
            account_a = account_b
        account_b = random.choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        is_over = True
    print('\n')
