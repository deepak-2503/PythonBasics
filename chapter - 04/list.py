friends = ["deepak", "harry", 24.5, "shubham", 45, True]
print(friends)

# unlike strings, lists are mutable.
friends[0] = "deepika"
print(friends[0])
print(friends)  # print updated list
print(friends[0:3]) # slicing of list
print(friends[0:5:2]) # skip value in lists
print(friends[0:6])
print(friends[-6:])

