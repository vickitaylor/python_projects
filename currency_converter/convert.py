def main():
    print("This program converts USD to GBP")
    print()

    dollars = eval(input("Enter amount in US Dollars: "))

    pounds = convert_to_pounds(dollars)

    print(f"That is {pounds} GBP")

convert_to_pounds = lambda dollars: dollars * 0.89

main()
