marks = {
    "Deepak" : 100,
    "Aman" : 90,
    "list" : [0, 3, 4],
    (0,4) : "Tuple"   
}

print(marks.keys())  # to get list of keys
print(marks.values()) # returns all values


# print(marks.values()) returns all values, if we want to typecast thid into list then,
print(list(marks.values())) 
# if we want to fing=d len of values i.e. total no. of values then
print(len(list(marks.values())))
# same we can do with keys
print(tuple(marks.keys()))
print(len(tuple(marks.keys())))  

# to get all key values we use dict.items it returns in form of tuple
print(marks.items())
print(list(marks.items()))
print(len(list(marks.items())))


# it will update as well as add new key value pair in dict
marks.update({"Aman" : 75, "Tanu" : 99})
print(marks)

# to get corresponding value of key
print(marks.get("Deepak"))


# ques -  what is diff in
print(marks.get("Deepak2"))  # none return
print(marks["Deepak2"])  # error return


marks.pop("Tanu")  # delete any key:value
print(marks)
