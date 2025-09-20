'''Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.'''
emptydict = {}

name1 = input("Enter your name: ")
lang1 = input("Enter your lang: ")
emptydict.update({name1 : lang1})

name2 = input("Enter your name: ")
lang2 = input("Enter your lang: ")
emptydict.update({name2 : lang2})

name3 = input("Enter your name: ")
lang3 = input("Enter your lang: ")
emptydict.update({name3 : lang3})

name4 = input("Enter your name: ")
lang4 = input("Enter your lang: ")
emptydict.update({name4 : lang4})

print(emptydict)



'''If the names of 2 friends are same; what will happen to the program in problem
6?'''
# jo end me add krege value vo store ho jayegi