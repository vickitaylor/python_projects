
# function that takes a year and determines if the given year is a leap year.
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year!!!")
            else:
                print("Not a leap year")

        else:
            print("Leap Year!!!")
    else:
        print("Not a leap year")

leap_year(2023)
leap_year(2000)