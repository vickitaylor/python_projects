# need a dictionary that stores questions and answers
# make a variable that tracks the score of the player
# loop thru the dictionary, using key value pairs
# display each question to the user and allow them to answer
# state if it is correct or not
# show the final result when the quiz is complete

# making the quiz dictionary, key is the question, value is a dictionary of the question and answer
quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of England?",
        "answer": "London"
    },
    "question4": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question5": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question6": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question7": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question8": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    }
}

# staring score
score = 0

# looping thru a dictionary
for key, value in quiz.items():
    print(value['question'])
    answer = input("Enter the Answer:")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1
        print(f"Your score is {str(score)}")

    else:
        print("Wrong!")
        # to print the answer value of the dictionary in the formatted string
        print(f"The answer is: {value['answer']}")
        print(f"Your score is {str(score)}")
        # if you wanted it to stop when they got it wrong could use quit()
        # quit()

print(f"You got {str(score)} out of 8 questions correct!")
print(f"Your percentage is {str(int(score/7*100))}%")
