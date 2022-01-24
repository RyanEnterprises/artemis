# This will be an AI app that takes a user's voice or text input and returns a response

print("Welcome to Artemis, your personal AI assistant.")
print("Please wait while I load my knowledge base.")

#randomness
numbers = ["1", "2", "3", "4", "5","6","7","8","9","10"]
letters = ["a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
coin = ["Heads", "Tails"]


# Imports
import os
import sys
import time
import random
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
        print("Hello, how are you today?")
        command = input("Command: ")

    if command == "help":
        print("Here is a list of commands:")
        print("'flip' - flips a coin")
        print("'Hello' - Say hello to me.")
        print("'help' - Shows a list of avalible commands")
        print("'open' - Opens a website.")
        print("'quit' - Quits the program.")
        print("'random' - Gives a random number.")
        command = input("Command: ")

    if command == "give me a random number" or command == "give me a random number between 1 and 10" or command == "I want a random number" or command == "I want a random number between 1 and 10" or command == "random":
        print(random.choice(numbers))
        command = input("Command: ")

    if command == "Flip a Coin" or command == "flip a coin" or command == "flip a coin for me" or command == "flip coin" or command == "flip":
        print(random.choice(coin))
        command = input("Command: ")
    
    else:
        print("I'm sorry, I don't understand that command yet. However, I am always growing")
        command = input("Command: ")

