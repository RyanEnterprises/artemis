#variables

versionNumber = "3.0.0"

facts = [
    "I was created by a programmer named Ryan.",
    "I was created in 2022.",
    "The world's oldest wooden wheel has been around for more than 5,000 years",
    "Dead skin cells are a main ingredient in household dust",
    "Sudan has more pyramids than any country in the world",
    "The average person walks the equivalent of three times around the world in their lifetime",
    "The bumblebee bat is the world's smallest mammal",
    "The circulatory system is more than 60,000 miles long",
    "There are parts of Africa in all four hemispheres",
    "The cornea is one of only two parts of the human body without blood vessels",
    "The world's first animated feature film was made in Argentina",
    "German chocolate cake was invented in Texas",
    "The Philippines consists of 7,641 islands",
    "A one-way trip on the Trans-Siberian Railway involves crossing 3,901 bridges",
    "There's enough gold inside Earth to coat the planet",
    "Cleveland was once the country's fifth-largest city",
    "The brand name Spam is a combination of “spice” and “ham",
    "The first person to walk on the moon was Buzz Aldrin",
    "It takes a drop of water 90 days to travel the entire Mississippi River",
    "Lemons float, but limes sink"

]

jokes = [
    "What do you call a fake noodle? An Impasta.",
    "Why did the python cross the road? To eat the chicken.",
]

gretings = [
    "Hello",
    "Hi",
    "Hey",
    "Howdy",
    "Greetings",
    "Good day",
    "Good morning",
    "Good afternoon",
    "Good evening",
    "Good night",
    "Good luck",
    "Good luck on your journey",
    "May the force be with you",
    "How are you doing today?",
    "How are you doing?",
    "How are you?",
]

numbers = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]

letters = [
    "a",
    "b",
    "c", 
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
]
coin = [
    "Heads",
    "Tails"
]


# Imports
import os
import time
import random
from bs4 import BeautifulSoup
from artemis import username as un
from artemis import artemisUGName as AUGN
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import requests
import json
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import chalk

print("Begin by typing a command or saying something.")
print("TIP: You can always type 'quit' to exit the program.")
print("TIP: You can always type 'help' to see a list of commands.")
command = input("Command: ")

# Begin the main loop
while command != "quit":
    if command == "" or command == " ":
        print(chalk.red("You cannot say nothing."))
        command = input("Command: ")

    if command == "hello":
        print(random.choice(gretings) + ", " + un)
        print("My name is " + AUGN + ", how can I help you today?")
        command = input("Command: ")

    if command == "help":
        print("Here is a list of commands:")
        print("'artemis' - Gives you the current version number.")
        print("'fact' - Gives you a random fact")
        print("'flip' - flips a coin")
        print("'game' - Starts a game")
        print("'hello' - Say hello to me.")
        print("'help' - Shows a list of avalible commands")
        print("'know' - Gives a summary from wikipedia about a topic")
        print("'loop' - sends your device into an infinite loop")
        print("'motivate' - Gives you a motivational quote, using our sister service, '(de)Motivator'")
        print("'open' - Opens a website.")
        print("'play' - Plays a song.")
        print("'prank' - It's a suprise.")
        print("'quit' - Quits the program.")
        print("'random' - Gives a random number.")
        print("'search' - Searches google for a topic.")
        print("'system' - Enters system mode")
        print("'zen' - Gives you a very zen poem.")
        command = input("Command: ")

    if command == "give me a random number" or command == "give me a random number between 1 and 10" or command == "I want a random number" or command == "I want a random number between 1 and 10" or command == "random":
        print(random.choice(numbers))
        command = input("Command: ")

    if command == "Flip a Coin" or command == "flip a coin" or command == "flip a coin for me" or command == "flip coin" or command == "flip":
        print(random.choice(coin))
        command = input("Command: ")

    if command == "open":
        print("What website do you want to open?")
        website = input("Website: ")
        webbrowser.open(website)
        command = input("Command: ")

    if command == 'artemis' or command == 'version' or command == 'version number' or command == 'version number for me' or command == 'about':
        print("Artemis" + " " + versionNumber)
        print("Artemis is a personal AI assistant.")
        print("It is a work in progress and is still in development.")
        print("If you have any suggestions or feedback, please let me know.")
        print("Thank you for using Artemis.")
        command = input("Command: ")

    if command == "fact":
        print(random.choice(facts))
        command = input("Command: ")

    if command == "know":
        import know
        command = input("Command: ")

    if command == "play":
        print("What song do you want to play? TIP: It has to be on your computer WITH the file extension. EX: 'Never Gonna Give You Up.mp4'")
        song = input("Song: ")
        os.system("start " + song)
        command = input("Command: ")

    if command == "loop":
        print("WARNING: This will send your device into an infinite loop, and you will need to restart the program to go back to normaal.")
        print("Are you sure you want to do this?")
        print("Type 'yes' to continue.")
        print("Type 'no' to cancel.")
        loop = input("Command: ")
        if loop == "yes":
            while True:
                print(random.choice(gretings) + " " + random.choice(gretings) + " " + random.choice(letters) + " " + random.choice(facts) + " " + random.choice(numbers) + " " + random.choice(coin))
        elif loop == "no":
            print("Canceled.")
            command = input("Command: ")

    if command == "motivate":
        webbrowser.open("https://porkyproductions.github.io/deMotivator/")
        command = input("Command: ")

    if command == "game":
        import triviagame
        command = input("Command: ")

    if command == "prank":
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print(chalk.magenta("GOTCHA ;)"))
        command = input("Command: ")

    if command == "system":
        import system
        command = input("Command: ")
    

    if command == "search":
        print("What do you want to search for?")
        search = input("Search: ")
        webbrowser.open("https://www.google.com/search?q=" + search)
        command = input("Command: ")

    if command == "zen":
        import this
        command = input("Command: ")
    # Uncomment if you want to use this, it only works sometimes
    #if command == "write":
        #r = requests.post(
        #"https://api.deepai.org/api/text-generator",
        #data={
            #'text': input("What do you want to write? "),
        #},
        #headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    #)
    #print(r.json()['output'])
    #command = input("Command: ")
    
    else:
        print("I'm sorry, I don't understand that command yet. However, I am always growing")
        command = input("Command: ")


