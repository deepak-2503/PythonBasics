# Write a program to find whether a given username contains less than 10
# characters or not
username = input("Enter your username: ")
len_username = len(username)
print(f"{username} has {len_username} character")
if(len_username<10):
    print("It has less than 10 character")
else:
    print("More than 10 character")    
