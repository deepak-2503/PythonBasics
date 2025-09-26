# . Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter a number a : "))
b = int(input("Enter a number b : "))
c = int(input("Enter a number c : "))
d = int(input("Enter a number d : "))

if(a>=b and a>=c and a>=d):
    print(f"{a} is greatest")

elif(b>=a and b>=c and b>=d):
    print(f"{b} is greatest")

elif(c>=b and c>=a and c>=d):
    print(f"{c} is greatest")        
else:
    print(f"{d} is greatest")    