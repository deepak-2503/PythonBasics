# # Write a program to print multiplication table of a given number using for loop
table = int(input("Enter a number of which you want table : "))
i = 1
while(i<11):
    print(i*table)
    i = i+1
    
  
## For loop
table = int(input("Enter a number of which you want table : "))
print(f"Table of {table} is :-")
for i in range(1,11):
    print(i*table)
  
    