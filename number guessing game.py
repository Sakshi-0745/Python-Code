import random
def number_guessing_game():
    print("welcome to number guessing game")
    print("guess the number in between 1 to 100")
    number=random.randint(1,100)
    attempts=0
    while True:
        guess=int(input("guess the number"))
        attempts+=1
        if guess<number:
            print("guess is low")
        elif guess>number:
            print("guess is high")
        else:
            print("Correct! You guessed the number in", attempts, "attempts.")
            break
number_guessing_game()    