# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

trans = {
    "Madad" : "help",
    "gaadi" : "Vehicle",
    "aag" : "Fire"
    
}
word = input("Enter a word of ehich you want to know meaning : ").title()
print(trans.get(word))