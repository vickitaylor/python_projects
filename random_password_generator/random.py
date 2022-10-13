# ask the user if they want to generate a password
# if yes ask for the password length
# generate a password
# print the password
# if no exit the program

# 🦖🦖 this runs correctly in the debugger, having issues running in the terminal, not sure why
# the random import is not working correctly, tried from random import shuffle, but no luck🐍🐍


import string
import random

# defining variable characters that will be used in the password, variable is a list
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# defining function
def generate_password():
    password_length = int(input("How long do you want the password to be? "))

    # to get a random assortment of characters in the list
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        # going to take random characters and put them in the password list
        password.append(random.choice(characters))

        # randomly shuffling the password list to make more random
        random.shuffle(password)

        # converting the list to a string
        password_str = "" .join(password)

        print(password_str)


option = input("Do you want make a random password? (Yes/No)")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program Ended")
    quit()
else:
    print("Input not valid, please use Yes or No")
