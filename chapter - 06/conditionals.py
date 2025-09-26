a = int(input("Enter your age: "))

if(a>=100):
    print(f"{a} is not a real age")
elif(a==0):
    print("Age must be greater than 0")
elif(a<18):
    print("Enter a positive age")
elif(a>=18):
    print(f"Yeah your age is {a} you can vote !")
    
print("Thank you, Please visit again")    