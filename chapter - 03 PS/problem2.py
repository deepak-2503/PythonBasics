# Write a program to fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
# Way 1
name = input("Enter your name: ")
date = input("Enter today's date: ")
print(f"Dear {name},\nYou are selected!\n{date}")

# Way 2
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)
