a = (4, 34, 47, "deepak", True)
print(type(a))

# to make tuple with one entry
b = (2,) # must give comma
print(type(b))

# tuple is immutable
friends = ("deepak", "harry", 24.5, "shubham", 45, True, "deepak")
friends[0] = "verma"
print(friends)
print(friends.count("deepak"))