import wikipedia
import webbrowser

print("What method do you want to use? Type 'google' for google search, 'wiki' for wikipedia search, and 'bing' for bing search.")
method = input("Method: ")

if method == "google":
    print("What do you want to search for?")
    search = input("Search: ")
    webbrowser.open("https://www.google.com/search?q=" + search)

elif method == "wiki":
    print("What do you want to search for?")
    search = input("Search: ")
    wikipedia.summary(search)

elif method == "bing":
    print("What do you want to search for?")
    search = input("Search: ")
    webbrowser.open("https://www.bing.com/search?q=" + search)

else:
    print("Invalid method.")
    print("Please try again.")
    print("Exiting...")
    exit()