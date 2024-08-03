from config import logo
members = {}
is_game_over = False
print(logo)
print("Welcome to the secret auction program.")

while not is_game_over:
    name = input("What is your name: ")
    bid = int(input("What's your bid?: $"))
    members[name] = bid
    restart = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if restart == "no":
        is_game_over = True

highest_bid = 0
winner = "nobody"
for key in members:
    if members[key] > highest_bid:
        highest_bid = members[key]
        winner = key

print(f"The winner is {winner} with a bid of ${highest_bid}.")