# creating a function that will replace words in a string

def replace_word():
    """function that replaces a word in a string, using the replace method
    """
    # string with words to replace in it
    string = "Hi everyone, I am Vicki! and hi hi hi hi"

    # printing the string so the user can see what they can replace
    print(string)

    # input box for the word in the string that is going to be replaced, (this is case sensitive)
    word_to_replace = input("Want to replace a word? Enter it here: ")

    # input for the replacement word
    word_replacement = input("Enter the word to replace: ")

    # replace method that will replace the selected word with the replacement word
    print(string.replace(word_to_replace, word_replacement))


# invoking the function
replace_word()
