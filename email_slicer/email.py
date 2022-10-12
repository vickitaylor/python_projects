# program takes an email address and slices it into username, domain, and the extension.
# first want to get the email from the user
# then split the email on the @ sign as the user name
# then split on the . for the domain
# then the rest is the extension

def slicer():
    print("Welcome to the email slicer!")
    # printing blank line
    print("")

    # input for the user to get the users email address. 
    email_input = input("Enter your email address:")

    # splitting on the @ sign it is being saved to username and domain
    (username, domain) = email_input.split("@")

    # splitting the domain into domain and extension
    (domain, extension) = domain.split(".")

    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")

slicer()
