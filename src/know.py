import wikipedia

print("What do you want to know?")
print("HINT: It has to be the title of a wikipedia article.")

know = input("HERE: ")
print(wikipedia.summary(know))