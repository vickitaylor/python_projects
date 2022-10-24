# import urllib, using as and renaming so do not have to type urllib.request each time
import urllib.request as urllib


def main(url):

    print("Checking connectivity...")

    # use urllib.request to get the data from the url, stored in a response
    response = urllib.urlopen(url)

    print("Connected to", url, "successfully")
    print("The response code was:", response.getcode())

print("This is a site connecitvy checker program.")
input_url = input("Input the url of the site you want to check:")

main(input_url)
