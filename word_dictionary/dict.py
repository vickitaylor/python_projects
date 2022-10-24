# using dictionary library, and installed pyDictionary
from PyDictionary import PyDictionary

dict = PyDictionary()

while True:
    word = input("Enter a word:")
    # to break the loop
    if word == "":
        break

    print(dict.meaning(word))


# way to do this with a dictionary you create
# def main():
    # have a python dictionary that has a key value pair that represents a word and its definition
#     word_dict = {
#         'hi': 'A way of greeting',
#         'eyes': 'An organ for seeing',
#         'earth': 'A planet in space'
#     }

#     while True:
    # collect input from the user, input is a word
#         word = input("Enter a word:")
#         if word == "":
#             # breaking the loop
#             break
    # check if the word is in the dictionary
#         if word in word_dict:
    # print the definition
#             print(word, ":", word_dict[word])

# main()
