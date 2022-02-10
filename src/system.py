print ("Welcome to system mode.")
print ("System mode is for doing tasks for your operating system with Artemis Magic")
print ("Type 'exit' to exit system mode.")
print ("Type 'help' for help.")
print ("Let's get started!")

# IMPORTS
import os
import random
import time
import sys
import speech_recognition as sr
import webbrowser
import requests
import json
import chalk

sysCommand = input("Type a command: ")


while sysCommand != "exit":
    if sysCommand == "" or sysCommand == " ":
        print (chalk.red("You cannot say nothing."))
        sysCommand = input("Type a command: ")
    if sysCommand == "help":
        print ("Here are the commands you can use:")
        print ("'exit' - Exits the program.")
        print ("'explorer' - Opens the default file manager on windows")
        print ("'help' - Displays this message.")
        print ("'registry' - Opens the registry.")
        print ("'system' - Opens the system.")
        print ("'network' - Opens the network.")
        print ("'security' - Opens the security.")
        print ("'power' - Opens the power.")
        print ("'sound' - Opens the sound.")
        print ("'calculator' - Opens the calculator.")
        print ("'email' - Opens the email.")
        print ("'facebook' - Opens the facebook.")
        print ("'twitter' - Opens the twitter.")
        print ("'youtube' - Opens the youtube.")
        print ("'twitch' - Opens the twitch.")
        print ("'reddit' - Opens the reddit.")
        print ("'google' - Opens the google.")
        print ("'wikipedia' - Opens the wikipedia.")
        print ("'bing' - Opens the bing.")
        print ("'search' - Opens the search.")
        print ("'news' - Opens the news.")
        print ("'calendar' - Opens the calendar.")
        print ("'notepad' - Opens the notepad.")
        print ("'paint' - Opens the paint.")
        print ("'messenger' - Opens the messenger.")
        sysCommand = input("Type a command: ")
    if sysCommand == "registry":
        print ("Opening registry...")
        os.system("start regedit")
        sysCommand = input("Type a command: ")
    if sysCommand == "system":
        print ("Opening system...")
        os.system("start msconfig")
        sysCommand = input("Type a command: ")
    if sysCommand == "network":
        print ("Opening network...")
        os.system("start control")
        sysCommand = input("Type a command: ")
    if sysCommand == "security":
        print ("Opening security...")
        os.system("start control")
        sysCommand = input("Type a command: ")
    if sysCommand == "power":
        print ("Opening power...")
        os.system("start control")
        sysCommand = input("Type a command: ")
    if sysCommand == "explorer":
        print("Opening Explorer")
        os.system("start explorer")
        sysCommand = input("Type a command: ")
    if sysCommand == "sound":
        print ("Opening sound...")
        os.system("start control")
        sysCommand = input("Type a command: ")
    if sysCommand ==  "calculator":
        print ("Opening calculator...")
        os.system("start calc")
        sysCommand = input("Type a command: ")
    if sysCommand == "email":
        print ("Opening email...")
        os.system("start outlook")
        sysCommand = input("Type a command: ")
    if sysCommand == "facebook":
        print ("Opening facebook...")
        webbrowser.open("https://www.facebook.com")
        sysCommand = input("Type a command: ")
    if sysCommand == "twitter":
        print ("Opening twitter...")
        webbrowser.open("https://www.twitter.com")
        sysCommand = input("Type a command: ")
    if sysCommand == "youtube":
        print ("Opening youtube...")
        webbrowser.open("https://www.youtube.com")
        sysCommand = input("Type a command: ")
    if sysCommand == "twitch":
        print ("Opening twitch...")
        webbrowser.open("https://www.twitch.tv")
        sysCommand = input("Type a command: ")
    if sysCommand == "reddit":
        print ("Opening reddit...")
        webbrowser.open("https://www.reddit.com")
        sysCommand = input("Type a command: ")
    if sysCommand == "google":
        print ("Opening google...")
        webbrowser.open("https://www.google.com")
        sysCommand = input("Type a command: ")
    if sysCommand == "wikipedia":
        print ("Opening wikipedia...")
        webbrowser.open("https://www.wikipedia.org")
        sysCommand = input("Type a command: ")
    if sysCommand == "bing":
        print ("Opening bing...")
        webbrowser.open("https://www.bing.com")
        sysCommand = input("Type a command: ")
    if sysCommand == "search":
        print ("Opening search...")
        webbrowser.open("https://www.google.com/search")
        sysCommand = input("Type a command: ")
    if sysCommand == "news":
        print ("Opening news...")
        webbrowser.open("https://www.google.com/news")
        sysCommand = input("Type a command: ")
    if sysCommand == "calendar":
        print ("Opening calendar...")
        webbrowser.open("https://www.google.com/calendar")
        sysCommand = input("Type a command: ")
    if sysCommand == "notepad":
        print ("Opening notepad...")
        os.system("start notepad")
        sysCommand = input("Type a command: ")
    if sysCommand == "paint":
        print ("Opening paint...")
        os.system("start mspaint")
        sysCommand = input("Type a command: ")
    if sysCommand == "messenger":
        print ("Opening messenger...")
        os.system("start outlook")
        sysCommand = input("Type a command: ")
    if sysCommand == "exit":
        print ("Exiting...")
        import artemisText
    if sysCommand != "exit" and sysCommand != "help":
        print (chalk.red("COMMAND NOT RECOGNIZED"))
        sysCommand = input("Type a command: ")