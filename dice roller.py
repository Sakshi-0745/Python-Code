import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice...")
    print("You rolled a", roll_dice())
    again = input("Roll again? (y/n): ")
    if again.lower() != 'y':
        break
