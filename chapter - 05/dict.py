# in dict we store value in form of key:value pair. key should be immutable like string, tuple, float etc.
# unordered, mutable, dont allow duplicate key
marks = {
    "Deepak" : 100,
    "Aman" : 90,
    "list" : [0, 3, 4],
    (0,4) : "Tuple"
    
}

print(marks, type(marks))
print(marks["Deepak"])
marks["Deepak"] = "Raja"
marks["status"] = "Pass"   # to add new entry
print(marks)