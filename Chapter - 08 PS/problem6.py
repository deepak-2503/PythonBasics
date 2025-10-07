# Write a python function which converts inches to cms.
# 1 inch = 2.54 centimeters (cm)
def converter(inch):
    cm = inch*2.54
    return cm

inch = float(input("Enter inch to convert into cm : "))
print(f"{inch} inch = {converter(inch)} cm")