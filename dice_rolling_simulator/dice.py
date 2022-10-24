# import random
import random

# define function to roll the dice
def roll_dice():

    # create a dictionary that will have the dice drawings
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        )
    }

    roll = input("Roll Dice? (Yes or No)")

    # loop if they want to continue
    while roll.lower() == "Yes".lower():
        # generates a random integer between 1 and 6
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice Rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Roll Again? (Yes or No)")


roll_dice()
