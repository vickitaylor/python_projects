# Binary search is an algorithm that works by repeatedly splitting data in half until the target
# value is found =>Takes the list of data & has a target, and keeps splitting the list in half
# until the target is found.

# function that takes a list and target parameter
# 2 parameters (list and target)
# multiple variables, middle, start, end, and steps.  Steps the amount of time it has split
# either using recursion or while loop. increase steps each time split is done
# conditions to track target position

def binary_search(list, element):
    # defining variables
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    # loop runs until the start is less than or equal to the end value
    while start <= end:
        print(f"Step: {steps} : {str(list[start:end+1])}")

        # increase the step count
        steps += 1
        # assigning the middle variable, using // is floor division to not return a float
        # (/ auto defaults to float) Start in the 1st exp is 0, end is 9, middle is 4.5 (floor 4)
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 2

binary_search(my_list, target)

my_list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target_a = 12

binary_search(my_list_a, target_a)
