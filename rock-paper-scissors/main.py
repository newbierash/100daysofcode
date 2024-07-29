import config
import random

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").lower()
computer = str(random.randint(0, 2))
if choice == "0":
    print(config.rock)
elif choice == "1":
    print(config.paper)
elif choice == "2":
    print(config.scissors)

print(f"Computer chose: {computer}")
if computer == "0":
    print(config.rock)
elif computer == "1":
    print(config.paper)
elif computer == "2":
    print(config.scissors)

# win cases
# rock(0) - scissors(2)
# paper(1) - rock(0)
# scissors(2) - paper(1)

if (choice == "0" and computer == "2") or (choice == "1" and computer == "0") or (choice == "2" and computer == "1"):
    print("You win!")
elif choice == computer:
    print("Draw!")
else:
    print("You lose!")
