# This will be an AI app that takes a user's voice or text input and returns a response

print("Welcome to Artemis, your personal AI assistant.")
print("Please wait while I load my knowledge base.")

#variables

versionNumber = "1.0"

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
import sys
import time
import random
from bs4 import BeautifulSoup
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import smtplib
import requests
import json
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *


## Startup Stuff

print("Begin by typing a command or saying something.")
print("TIP: You can always type 'quit' to exit the program.")
print("TIP: You can always type 'help' to see a list of commands.")
command = input("Command: ")

# Begin the main loop
while command != "quit":
    if command == "":
        print("You cannot say nothing.")
        command = input("Command: ")

    if command == "Hello":
        print(random.choice(gretings))
        command = input("Command: ")

    if command == "help":
        print("Here is a list of commands:")
        print("'artemis' - Gives you the current version number.")
        print("'flip' - flips a coin")
        print("'game' - Starts a game")
        print("'Hello' - Say hello to me.")
        print("'help' - Shows a list of avalible commands")
        print("'know' - Gives a summary from wikipedia about a topic")
        print("'open' - Opens a website.")
        print("'play' - Plays a song.")
        print("'prank' - It's a suprise.")
        print("'quit' - Quits the program.")
        print("'random' - Gives a random number.")
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

    if command == "know":
        print("What do you want to know?")
        know = input("HERE: ")
        print(wikipedia.summary(know))
        features="html.parser"
        page = requests.get(wikipedia.page(know).url)
        soup = BeautifulSoup(page.content, features)
        features="html.parser"
        print(soup.get_text())
        command = input("Command: ")

    if command == "play":
        print("What song do you want to play? TIP: It has to be on your computer.")
        song = input("Song: ")
        os.system("mpg321 " + song)
        command = input("Command: ")

    if command == "game":
        import triviagame
        command = input("Command: ")

    if command == "prank":
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        command = input("Command: ")
    
    
    else:
        print("I'm sorry, I don't understand that command yet. However, I am always growing")
        command = input("Command: ")

