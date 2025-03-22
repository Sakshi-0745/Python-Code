import random
while True:
    user_choice=(input("enter your choice: rock paper scissors:"))
    choice=["rock","paper","scissor"]
    computer_choice=random.choice(choice)
    if user_choice==computer_choice:
        print("tie")
    elif user_choice == "rock" and computer_choice == "scissor" or\
        user_choice == "paper" and computer_choice == "scissor" or\
        user_choice == "rock" and computer_choice == "paper":
        print("user wins")
    else: 
        print("computer wins")
        play_again=input("do you want to play again?")
        if play_again != "yes":
            break