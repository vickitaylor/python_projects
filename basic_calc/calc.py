# defining a functions to build the calculator, add, sum, mul, div.
# the the options will be printed to the user.
# ask for values
# call the functions
# add while loop to continue the program, until the user wants to exit.

def add(num1, num2):
    """ function adds 2 numbers

    Args:
        num1 (int): first integer to be added
        num2 (int): second integer to be added
    """

    answer = num1 + num2
    # print string per example
    # print(str(num1) + ' + ' + str(num2) + ' = ' + str(answer))
    # rather use the f string to print the statement
    # break (\n) added for better visual in the terminal
    print(f"{num1} + {num2} = {answer} \n")


def sub(num1, num2):
    """ function subtracts 2 numbers

    Args:
        num1 (int): first integer to be subtracted
        num2 (int): second integer to be subtracted
    """

    answer = num1 - num2
    print(f"{num1} - {num2} = {answer} \n")


def mul(num1, num2):
    """ function multiples 2 numbers

    Args:
        num1 (int): first integer to be multiplied
        num2 (int): second integer to be multiplied
    """

    answer = num1 * num2
    print(f"{num1} * {num2} = {answer} \n")


def div(num1, num2):
    """ function divides 2 numbers

    Args:
        num1 (int): first integer to be divided
        num2 (int): second integer to be divided
    """

    answer = num1 / num2
    print(f"{num1} / {num2} = {answer} \n")


# adding while loop for the functions to keep looping until quit function is called.
while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit \n")

    # making the variable name choice equal to an input
    choice = input("Input your choice: ")

    # then if statement to determine which function to use based on the user selection, and
    # determines what is printed and which function is ran based on the selection.
    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Enter your first number:"))
        b = int(input("Enter second number:"))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Enter your first number:"))
        b = int(input("Enter second number:"))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Enter your first number:"))
        b = int(input("Enter second number:"))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Divide")
        a = int(input("Enter your first number:"))
        b = int(input("Enter second number:"))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Calculator done")
        quit()
