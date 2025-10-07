'''"snake, water, gun" game
snake beats water
gun beats snake
water beats gun
snake = 1
water = 2
gun = 3
'''
import random

user = input("Enter first letter of your word: ").lower()
user_dict = {"s" : "snake", "w" : "water", "g" : "gun"}
print(f"You chose {user_dict[user]}")


computer = random.choice([1,2,3])
computer_guess = {1: "snake", 2:"water", 3:"gun"}
print(f"Computer chose {computer_guess[computer]}")

if(user_dict[user] == computer_guess[computer]):
    print("Match Draw ") 
else:
    if(user_dict[user] == "snake" and computer_guess[computer] == "water"):
        print("You won 🥳!! ")
    elif(user_dict[user] == "gun" and computer_guess[computer] == "snake"):
        print("You won 🥳!!")
    elif(user_dict[user] == "water" and computer_guess[computer] == "gun"):
        print("You won 🥳!!") 
    elif(user_dict[user] == "water" and computer_guess[computer] == "snake"):
        print("You Lost 😭")
    elif(user_dict[user] == "snake" and computer_guess[computer] == "gun"):
        print("You Lost 😭!!")
    elif(user_dict[user] == "gun" and computer_guess[computer] == "water"):
        print("You Lost 😭!!")   
    else:
        print("Unknown error occured !")      
        
