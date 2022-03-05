# This will be an AI app that takes a user's voice or text input and returns a response

print("Welcome to Artemis, your personal AI assistant.")
print("Please wait while I load my knowledge base.")

import random

greetings = [
    "What's up?",
    "Hello",
    "Nice to meet you",
    "How is your day going?",
    "Lovely to meet you",
    "Sup",
    "Hi"
]

print("Let's begin by getting to know you a bit")

username = input("What is your name? ")
print("Hello " + username + "!")
print("Is this what you want me to call you?")
answerToNameQuestion = input("y/n ")
if answerToNameQuestion == "y":
    print("PERFECT! Let's continue, " + username)
    print(random.choice(greetings) + ", " + username)
elif answerToNameQuestion == "n":
    username = input("What should I call you? ")
    print(random.choice(greetings) + ", " + username)
else:
    print("Sorry. That is not a valid response. Please type 'n' for no, and 'y' for yes")


print("The next step is to name me! The default name is artemis, but you can call me whatever you want.")
artemisUGName = input("What do you want to call me? Leave blank if you want artemis. ")
if artemisUGName == "" or aretemisUGName == " ":
    artemisUGName = "artemis"
print("Are you sure you want to call me " + artemisUGName + "?")
answerToArtemisRename = input("y/n ")


print("Type 'voice' to use your voice. TIP: Only use this if you have the PyAudio module installed.")
print("Type 'text' to type your input.")

inputMethod = input("Input method: ")

if inputMethod == "voice":
    print("Voice input selected.")
    print("Is this what you wanted?")
    print("Type 'yes' to continue.")
    print("Type 'no' to cancel.")
    voiceInput = input("Input: ")
    if voiceInput == "yes":
        import artemisVoice
    elif voiceInput == "no":
        print("Canceled.")
        exit()

elif inputMethod == "text":
    print("Text input selected.")
    print("Is this what you wanted?")
    print("Type 'yes' to continue.")
    print("Type 'no' to cancel.")
    textInput = input("Input: ")
    if textInput == "yes":
        import artemisText
    elif textInput == "no":
        print("Canceled.")
        exit()