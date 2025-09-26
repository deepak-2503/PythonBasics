# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the use

# assume each subject is of 100 marks
hindi = int(input("Enter hindi marks: "))
english = int(input("Enter english marks: "))
maths = int(input("Enter maths marks: "))
totalnum = hindi + english + maths
print("Your total number is" ,totalnum)

total_percent =(totalnum*100)/300

if(total_percent>=40 and hindi >= 33 and english >= 33 and maths >= 33):
    print("You are pass")
else:
    print("You are fail")    