# This will be an AI app that takes a user's voice or text input and returns a response

print("Welcome to Artemis, your personal AI assistant.")
print("Please wait while I load my knowledge base.")

print("Let's begin by selecting your input method.")
print("Type 'voice' to use your voice.")
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