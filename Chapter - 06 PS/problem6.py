# Write a program to find out whether a given post is talking about “Harry” or not.
post = input("Enter post link to know whether it is about harry or not: ")
if("Harry" in post or "harry" in post):
    print("This post is about Harry")
else:
    print("Not about harry")    