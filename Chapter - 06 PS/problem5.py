# Write a program which finds out whether a given name is present in a list or not
name_list = ["Deepak" ,"Aman", "Tanu", "Adii", "Raja"]
name = input("Enter name you want to check in list: ").title()

if(name in name_list):
    print(f" ✅ {name} is present in {name_list}")
else:
    print(f"🚫 {name} is not present in {name_list}")    
