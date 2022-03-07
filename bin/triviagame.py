print("Let's play a game!")
print("I will ask you a question and you have to answer it.")
print("If you answer correctly, you get to keep the question.")
print("If you answer incorrectly, you lose the question.")
print("If you answer incorrectly twice, you lose the game.")
print("If you answer correctly twice, you win the game.")

# Variables
correct = 0
incorrect = 0
incorrect2 = 0
questions = 0
# Question 1
print("Question 1")
print("What is the capital of France?")
print("A) Paris")
print("B) London")
print("C) Rome")
print("D) Berlin")
answer = input("Answer: ")
if answer == "A" or answer == "a":
    print("Correct!")
    correct = correct + 1
    questions = questions + 1
else:
    print("Incorrect!")
    incorrect = incorrect + 1
    questions = questions + 1
print("You have " + str(correct) + " correct answers.")
print("You have " + str(incorrect) + " incorrect answers.")
print("You have " + str(incorrect2) + " incorrect answers.")
print("You have " + str(questions) + " questions.")
print("")

# Question 2
print("Question 2")
print("What is the capital of Germany?")
print("A) Paris")
print("B) London")
print("C) Rome")
print("D) Berlin")
answer = input("Answer: ")
if answer == "D" or answer == "d":
    print("Correct!")
    correct = correct + 1
    questions = questions + 1
else:
    print("Incorrect!")
    incorrect = incorrect + 1
    questions = questions + 1
print("You have " + str(correct) + " correct answers.")
print("You have " + str(incorrect) + " incorrect answers.")
print("You have " + str(incorrect2) + " incorrect answers.")
print("You have " + str(questions) + " questions.")
print("")

# Question 3
print("Question 3")
print("What is the capital of the United Kingdom?")
print("A) Paris")
print("B) London")
print("C) Rome")
print("D) Berlin")
answer = input("Answer: ")
if answer == "B" or answer == "b":
    print("Correct!")
    correct = correct + 1
    questions = questions + 1
else:
    print("Incorrect!")
    incorrect = incorrect + 1
    questions = questions + 1
print("You have " + str(correct) + " correct answers.")
print("You have " + str(incorrect) + " incorrect answers.")
print("You have " + str(incorrect2) + " incorrect answers.")
print("You have " + str(questions) + " questions.")
print("")

# Question 4
print("Question 4")
print("What is the capital of Italy?")
print("A) Paris")
print("B) London")
print("C) Rome")
print("D) Berlin")
answer = input("Answer: ")
if answer == "C" or answer == "c":
    print("Correct!")
    correct = correct + 1
    questions = questions + 1
else:
    print("Incorrect!")
    incorrect = incorrect + 1
    questions = questions + 1
    print("You have " + str(correct) + " correct answers.")
    print("You have " + str(incorrect) + " incorrect answers.")
    print("You have " + str(incorrect2) + " incorrect answers.")
    print("You have " + str(questions) + " questions.")
    print("")