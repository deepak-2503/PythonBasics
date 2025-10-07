# Write a program using functions to find greatest of three number
def greatest_of_three(a = 0,b = 0,c = 0):
    a = float(input("Enter a number: "))
    b = float(input("Enter a number: "))
    c = float(input("Enter a number: "))
    print(max(a,b,c))

greatest_of_three()