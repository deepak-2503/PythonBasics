# do same as question 2 but the problem is -
letter = '''
Dear <|Name|>,

We are pleased to confirm your appointment for the role of <|Role|>.
Your joining date is <|Date|> and your employee ID is <|ID|>.

We look forward to working with you.

Sincerely,
<|Company|>'''

name = input("Enter your name: ")
role = input("Enter your role: ")
id= input("Enter your id: ")
date = input("Enter today's date: ")
company = input("Enter your company: ")

letter = letter.replace("<|Name|>" ,name)
letter = letter.replace("<|Role|>" ,role)
letter = letter.replace("<|ID|>" ,id)
letter = letter.replace("<|Date|>" ,date)
letter = letter.replace("<|Company|>" ,company)

print(letter)
