# This will be an AI app that takes a user's voice or text input and returns a response

print("Welcome to Artemis, your personal AI assistant.")
print("Please wait while I load my knowledge base.")

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

print("Begin by typing a command or saying something.")
print("TIP: You can always type 'quit' to exit the program.")
command = input("Command: ")

# Begin the main loop
while command != "quit":
    if command == "":
        print("You cannot say nothing.")
        command = input("Command: ")

    if command == "Hello":
        print("Hello, how are you today?")
        command = input("Command: ")
    
    else:
        print("I'm sorry, I don't understand that command.")
        command = input("Command: ")

