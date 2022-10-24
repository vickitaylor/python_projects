import random


exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose: rock, paper, scissors, or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game over")
        print(f"Your points: {user_points}")
        print(f"Computer points: {computer_points}")
        exit = True

    elif user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("Its a tie!")
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer Won! 😒")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("You Won! 🤩")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("Its a tie!")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer Won! 😒")
            computer_points += 1
        elif computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You Won! 🤩")
            user_points += 1

    elif user_input == "scissors":
        if computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("Its a tie!")
        elif computer_input == "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer Won! 😒")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You Won! 🤩")
            user_points += 1

    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("Invalid input")
