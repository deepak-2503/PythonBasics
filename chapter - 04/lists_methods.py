friends = ["deepak", "harry", 24.5, "shubham", 45, True]
print(friends)

# to add something in the last of the list
friends.append("lastname")
print(friends)

# insert function insert value at desired place
friends.insert(1,"coder")  # 1 tells that where you want to insert it
print(friends)

# insert multiple datatype in list
friends.extend(["tanu, radha"])
print(friends)

# to remove any element
friends.remove("deepak")
print(friends)

# to short any list
l1 = [23, 5, 42, 34.4, 34.41,0]
l1.sort()
print(l1)

# to reverse list
l2 = [23, 4, 22, 777.53, 3]
l2.reverse()
print(l2)

# to remove any particular index value
l3 = ["rohan", 52, 71, 2.3, "deep"]
l3.pop(1)  # remove 1 index (52)
print(l3)