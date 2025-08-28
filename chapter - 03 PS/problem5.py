space = "dee  paaak"
newstr = space.replace("  "," ")
print(len(newstr))
print(newstr)  

# # Strings are immutable in Python (once created, they cannot be changed, only new strings are formed)
print(space)   # original string will never change
print(newstr)  # new string is created after replacing double space with single space