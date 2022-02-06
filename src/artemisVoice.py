# this will be a port of artemis using the speech_recognition library

# Variables
#variables

versionNumber = "2.0.0"

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
import speech_recognition as sr
import pyaudio
import os
import time
import random
from bs4 import BeautifulSoup
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

# Audio Definitions
r = sr.Recognizer()
mic = sr.Microphone()


# Main Function

print("Begin by saying something.")
print("TIP: You can always say 'quit' to exit the program.")
print("TIP: You can always say 'help' to see a list of commands.")

with mic as source:
    print("Say something!")
    audio = r.listen(source)
    print("Done!")

r.recognize_google(audio)

while audio != "quit":
    if audio == "":
        print("You cannot say nothing.")
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")
    if audio == "Hello":
        print(random.choice(gretings))
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")
    if audio == "help":
        print("Here is a list of audios:")
        print("'QnA' - Ask a question and get an answer.")
        print("'artemis' - Gives you the current version number.")
        print("'fact' - Gives you a random fact")
        print("'flip' - flips a coin")
        print("'game' - Starts a game")
        print("'Hello' - Say hello to me.")
        print("'help' - Shows a list of avalible audios")
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
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == "give me a random number" or audio == "give me a random number between 1 and 10" or audio == "I want a random number" or audio == "I want a random number between 1 and 10" or audio == "random":
        print(random.choice(numbers))
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == "Flip a Coin" or audio == "flip a coin" or audio == "flip a coin for me" or audio == "flip coin" or audio == "flip":
        print(random.choice(coin))
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == "open":
        print("What website do you want to open?")
        website = input("Website: ")
        webbrowser.open(website)
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == 'artemis' or audio == 'version' or audio == 'version number' or audio == 'version number for me' or audio == 'about':
        print("Artemis" + " " + versionNumber)
        print("Artemis is a personal AI assistant.")
        print("It is a work in progress and is still in development.")
        print("If you have any suggestions or feedback, please let me know.")
        print("Thank you for using Artemis.")
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == "fact":
        print(random.choice(facts))
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == "know":
        import know
        audio = input("audio: ")

    if audio == "play":
        print("What song do you want to play? TIP: It has to be on your computer WITH the file extension. EX: 'Never Gonna Give You Up.mp4'")
        song = input("Song: ")
        os.system("start " + song)
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == "motivate":
        webbrowser.open("https://porkyproductions.github.io/deMotivator/")
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == "game":
        import triviagame
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == "prank":
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == "system":
        import system
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")
    

    if audio == "search":
        print("What do you want to search for?")
        search = input("Search: ")
        webbrowser.open("https://www.google.com/search?q=" + search)
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == "write":
        r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': input("What do you want to write? "),
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    print(r.json()['output'])
    with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")

    if audio == "zen":
        import this
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")
    
    
    else:
        print("I'm sorry, I don't understand that audio yet. However, I am always growing")
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
            print("Done!")
    

