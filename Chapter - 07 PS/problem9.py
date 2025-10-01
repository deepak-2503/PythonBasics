# print table in revere order
n = int(input("Enter a number: "))
l =[10,9,8,7,6,5,4,3,2,1]
for i in l:
    print(f"{n} X {i} = {n*i}")
    
    
## Way 2
n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} X {11 - i} = {n*(11 - i)}")   