# collect the necessary inputs, principal, apr, years of loan
# calculate the monthly payment
# show to the user 

def main():
    print("This is a monthly payment calculator \n")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input the years of the loan: "))

    # gets the rate
    monthly_int_rate = apr / 1200
    # calculates the number of months
    months = years * 12
    # ** used to pass a function with an arbitrary number of positional arguments
    monthly_payment = principal * monthly_int_rate / (1- (1 + monthly_int_rate) ** (-months))

    print("The monthly payment for this loan is: $%.2f " % monthly_payment)

main()
